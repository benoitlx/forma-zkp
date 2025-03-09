---
title: "**Zero-Knowledge Proof**"
sub_title: Rézoléo 
author: "@benoitlx"
date: 13-03-2025 
theme:
  override:
    footer:
      style: template
      center:
        image: assets/rezo.png
      left: "@benoitlx - ZKP"
      height: 3 
---

<!-- jump_to_middle -->

Intuition
===

<!-- end_slide-->

Dragibus
===

<!-- end_slide -->

Sudoku
===

<!-- end_slide-->

<!-- jump_to_middle -->

Formalisme
===

<!-- end_slide -->

Machine de Turing
===

<!-- end_slide -->

Prove Me Wrong
===

Qu'est-ce qu'une *Preuve* ?

<!-- pause -->
<!-- incremental_lists: true -->

- Preuve en Maths
- Preuve en Science
- En droit pénal (L'accusation doit prouver son cas "au-delà de tout doute raisonnable")
- puis définition d'une preuve probabiliste sur L


<!-- 
speaker_note: |
    En *Science* on parle de signification statistique.
-->

<!-- end_slide -->

ZKP
===

# Définition 1

```typst +render
Un système de preuve interactif $(A,B)$ de connaissance du prédicat $P(I,S)$ est dit *à divulgation nulle de connaissance* \
si pour tout vérifieur $tilde(B)$, la famille de variables aléatoires $#text[Vue]_(A,tilde(B))(I,H)$ est parfaitement approximable sur \
$cal(L) = { (I,H)|I in L #text[ et] |H| lt.eq |I|^k }$ pour tout entier $k$ fixé.
```

<!-- end_slide-->

<!-- jump_to_middle -->

Exemples
===

<!-- end_slide -->

ZK-QR
===

<!-- end_slide -->

ZK-HAM
=== 

<!-- end_slide -->

<!-- jump_to_middle -->

Applications
=== 

<!-- end_slide -->

<!-- column_layout: [3, 2, 3] -->


<!-- column: 0 -->

```bash +exec_replace
pokemonsay --think "Oui !"
```
```bash +exec_replace
pokemonsay --think "Oui !"
```

<!-- column: 1 -->

```bash +exec_replace
pokemonsay "Des questions ???" 
```

<!-- column: 2 -->

```bash +exec_replace
pokemonsay --think "Oui !"
```
```bash +exec_replace
pokemonsay --think "Oui !"
```

<!-- end_slide -->

Références
===

# Vidéos

- [Wired](https://www.youtube.com/watch?v=fOGdb1CTu5c&t=1145s)
- [Up and Atom](https://www.youtube.com/watch?v=V5uVKZn3F_4)
- [Passe-Science](https://www.youtube.com/watch?v=OSdcnoAmohs)

# Papiers

# Lien Randoms

- [Pages wikipédia (fr et en)](https://en.wikipedia.org/wiki/Zero-knowledge_proof)
- [Cours ENS](https://www.di.ens.fr/~granboul/enseignement/crypto/MPRI1-Crypto-ZeroKnowledge.pdf)
- [Cours ENS (bis)](https://www.irif.fr/~carton/Enseignement/Complexite/ENS/Redaction/2009-2010/ludovic.patey.pdf)
- [Cours du MIT](https://courses.csail.mit.edu/6.857/2018/files/L22-ZK-Boaz.pdf)

# Lien vers la présentation

- [Repo github](https://github.com/benoitlx/forma-zkp)
- [Drive Rézo](#todo)
