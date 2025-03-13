term := "/home/bleroux/Documents/presenterm_fork/presenterm/target/release/presenterm"

theme := `cat tmp/theme`
pres := term+" --theme "+theme+" zkp.md"

default:
    @just --list

theme:
    @{{ term }} --list-themes 2> tmp/theme

present:
    kitty --start-as=fullscreen {{ pres }} --publish-speaker-notes -x -X & {{ pres }} --listen-speaker-notes

deps:
    cargo install --locked presenterm
    cargo install --locked typst
    npm install @mermaid-js/mermaid-cli ./node_modules/.bin/mmdc -h
    python -m venv .venv
    .venv/bin/pip install -r requirements.txt
