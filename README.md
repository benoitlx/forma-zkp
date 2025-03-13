# Introduction aux preuves à divulgation nulle de connaissance

Pour faire cette forma tu aura besoin :
- de deux gobelets opaques
- de dragibus
- de quelques personnes
- du pdf (dispo dans les releases, soon tm)
- et c'est tout !

Attention toutefois pour un maximum de **flow**, il est recommandé de faire cette présentation directement depuis un terminal !

## Présentation depuis un terminal

Il faut clone le repo puis faire un `just deps` (attention il faut `cargo` et `npm`) pour installer les dépendances nécéssaires.

Cela va installer :
- [`presenterm`](https://github.com/mfontanini/presenterm) pour run la présentation
- [`typst`](https://github.com/typst/typst) pour le rendu des figures faisant intervenir des maths
- [`mmdc`](https://github.com/mermaid-js/mermaid-cli) pour le rendu des diagrammes séquences

Dans un environnement python :
- [`networkx`](https://networkx.org/) pour gérer les graphes 
- [`matplotlib`](https://matplotlib.org/) pour le rendu des graphes
- [`presenterm-export`](https://github.com/mfontanini/presenterm-export) pour l'export en pdf

Optionnel :
- [`onefetch`](https://github.com/o2sh/onefetch)
- [`pokemonsay`](https://github.com/possatti/pokemonsay)

## TODO

- faire une issue sur presenterm pour retourner le thème sélectionné à partir de `presenterm --list-themes`
- faire un justfile pour choisir le thème, lancer la présentation avec les différents modes
