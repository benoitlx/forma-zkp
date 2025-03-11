pres := "presenterm --theme catppuccin-frappe zkp.md"

default:
    @just --list

themes:
    presenterm --list-themes

present:
    kitty --start-as=fullscreen {{ pres }} --publish-speaker-notes -x -X & {{ pres }} --listen-speaker-notes
