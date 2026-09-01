param(
    [ValidateSet('draft','release','tree','clean')]
    [string]$Target = 'draft'
)

$ErrorActionPreference = 'Stop'
$Build = Join-Path $PSScriptRoot 'build'
$Tree = Join-Path $PSScriptRoot 'sections/support-tree.txt'

if ($Target -eq 'clean') {
    if (Test-Path $Build) { Get-ChildItem $Build -Force | Remove-Item -Recurse -Force }
    if (Test-Path $Tree) { Remove-Item $Tree -Force }
    exit 0
}

if ($Target -eq 'tree') {
    Push-Location (Join-Path $PSScriptRoot '..')
    try {
        "Tracked source files:" | Set-Content $Tree -Encoding UTF8
        git ls-files src results figures | Add-Content $Tree -Encoding UTF8
    } finally { Pop-Location }
    exit 0
}

& $PSCommandPath tree
New-Item -ItemType Directory -Path $Build -Force | Out-Null
Push-Location $PSScriptRoot
try {
    if ($Target -eq 'draft') {
        $input = '\def\CoachDraftMode{1}\input{main.tex}'
        xelatex -halt-on-error -jobname=draft -output-directory=build $input
        bibtex build/draft 2>$null
        xelatex -halt-on-error -jobname=draft -output-directory=build $input
        xelatex -halt-on-error -jobname=draft -output-directory=build $input
    } else {
        xelatex -halt-on-error -jobname=release -output-directory=build main.tex
        bibtex build/release 2>$null
        xelatex -halt-on-error -jobname=release -output-directory=build main.tex
        xelatex -halt-on-error -jobname=release -output-directory=build main.tex
    }
} finally { Pop-Location }
