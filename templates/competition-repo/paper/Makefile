.PHONY: draft release tree clean build help
TEX=xelatex
BUILD=build

all: draft release

build:
	mkdir -p $(BUILD)

draft: build tree
	$(TEX) -halt-on-error -jobname=draft -output-directory=$(BUILD) "\\def\\CoachDraftMode{1}\\input{main.tex}"
	- bibtex $(BUILD)/draft
	$(TEX) -halt-on-error -jobname=draft -output-directory=$(BUILD) "\\def\\CoachDraftMode{1}\\input{main.tex}"
	$(TEX) -halt-on-error -jobname=draft -output-directory=$(BUILD) "\\def\\CoachDraftMode{1}\\input{main.tex}"

release: build tree
	$(TEX) -halt-on-error -jobname=release -output-directory=$(BUILD) main.tex
	- bibtex $(BUILD)/release
	$(TEX) -halt-on-error -jobname=release -output-directory=$(BUILD) main.tex
	$(TEX) -halt-on-error -jobname=release -output-directory=$(BUILD) main.tex

# 生成供附录/审计使用的版本控制文件树，不依赖 tree 命令
tree:
	@{ echo "Tracked source files:"; git -C .. ls-files src results figures 2>/dev/null || true; } > sections/support-tree.txt

clean:
	rm -rf $(BUILD)/*
	rm -f sections/support-tree.txt

help:
	@echo "make draft   - build draft PDF with TODO notes"
	@echo "make release - build release-candidate PDF without TODO notes"
	@echo "make tree    - regenerate tracked support file list"
	@echo "make clean   - remove generated build files"
