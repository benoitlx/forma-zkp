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

Si vous voyez des `typos`, n'hésitez pas à faire une PR sur le repo de la forma, c'est encore plus drole en live.

<!-- new_line -->
https://github.com/benoitlx/forma-zkp

<!-- pause -->
Il y a un bonus si je merge un truc qui éteind mon ordi à la fin de la forma (oui c'est possible 🙃)

<!-- end_slide -->

<!-- jump_to_middle -->

Intuition
===

<!-- end_slide-->

Dragibus®
===

![image:width:40%](assets/dragibus.jpg)

<!-- pause -->

Trouvez un protocol me permettant de prouver que j'ai choisis des `bonbons` de différentes couleurs, sans que vous puissiez savoir lesquels.

<!-- end_slide -->

Sudoku
===

```python +exec +line_numbers
/// import sys
/// sys.path.append('/home/bleroux/Documents/forma-zkp/')
/// 
/// from random import seed
seed(73)

from sudoku import *

print_board(board)
```

<!-- end_slide-->

Sudoku
===

```python {5-7|9-11} +exec +line_numbers
/// import sys
/// sys.path.append('/home/bleroux/Documents/forma-zkp/')
/// 
/// from random import seed, sample 
/// from time import sleep
/// shuffle = lambda x: sample(x, len(x))
seed(73)

from sudoku import *

# P ask for verification of the line 3
# V send a shuffled version of line 3 of his solution
line = shuffle(solution[2])

# P verify that the constraints are respected
print(line)
print(all(line.count(n) == 1 for n in range(1, 9)))
```
<!-- 
speaker_note: |
    Pb1: peut-etre que V peut remonter à des infos si il sait comment shuffle est implémenté
    Pb2: un ordi ne peut pas suivre du regard les données que P lui envoit, il ne peut pas s'assurer de la provenance des données que P envoit
-->

<!-- pause -->

```python +exec
/// import sys
/// sys.path.append('/home/bleroux/Documents/forma-zkp/')
/// 
/// from random import seed, sample 
/// from time import sleep
/// shuffle = lambda x: sample(x, len(x))
/// seed(73)
/// 
/// from sudoku import *
/// 
print(solution[2])
```

<!-- pause -->
```typst +render
#image("../assets/74.jpg")
#align(center)[xkcd: 74]
```

<!-- end_slide-->

Kururugi Sudoku
===

```mermaid +render
sequenceDiagram
    autonumber
    actor P as Alice alias Prover 
    actor V as Bob alias Verifier
    Note over V: a = random
    V ->> P: a 
    Note over P: b = random<br/>key = a@b<br/>answer=$$\sigma_{key}(line)$$
    P ->> V: answer 
    Note over V: vérification
    P ->> V: key
    Note over V: vérification de la clé avec a
```

<!-- end_slide -->

<!-- jump_to_middle -->

Formalisme
===

<!-- end_slide -->

Algo quoi ??
===

# Qu'est-ce qu'un Algorithme ?

<!-- pause -->

> Algorithm does not have a generally accepted formal definition. Researchers[1] are actively working on this problem.

[From](https://en.wikipedia.org/wiki/Algorithm_characterizations)

<!-- pause -->

Pleins de modèle de calcul différents :
<!-- incremental_lists: true -->
- automate fini
- automate à pile
- lambda-calcul
- machines à registres
- automates cellulaires
- **Machine de Turing**

<!-- pause -->

# Définition 1 - Machine de Turing

```typst +render
Une *machine de Turing* est un 7-uplet $(Sigma, Q, sigma, delta, Delta, q_0, F)$ où :
- $Sigma$ est un ensemble de symboles appelé alphabet, avec un symbole particulié noté $\#$.
- $Q$ est un ensemble non vide fini d'états.
- $sigma : Q times Sigma arrow.r.long Sigma$ est une fonction d'*impression*.
- $delta: Q times Sigma arrow.r.long Q$ est une fonction de *transition*.
- $Delta: Q times Sigma arrow.r.long {-1, 1}$ est une fonction de *déplacement*.
- $q_0$ l'état initial de la machine.
- $F$ l'ensemble des états finaux.
```

<!-- pause -->

## [Fonctionnement](https://turingmachine.io/)

```typst +render
À chaque étape, la machine se trouve dans un état $q$ et lit un symbole $a$, puis suit les instructions suivantes :
- écrit le symbole $sigma(q,a)$ sur le ruban.
- déplace la tête de lecture en fonction de $Delta(q, a)$.
- passe de l'état $q$ à l'état $delta(q, a)$.
```

<!-- end_slide -->

<!-- jump_to_middle -->
```typst +render
$
"BB"(5) = 47" "176" "870" "#emoji.heart
$
```

<!-- end_slide -->

Machine de Turing interactive
===

<!-- new_lines: 10 -->

![Machine de Turing Interactive](assets/interactive_turing_machine.png)

<!-- end_slide -->

Prove Me Wrong
===

<!-- column_layout: [3, 2] -->

<!-- column: 0 -->
# Qu'est-ce qu'une *Preuve* ?

<!-- pause -->
<!-- incremental_lists: true -->

- en Maths => preuve comme séquence statique de symboles
- en Science => accumulation statistique de preuves
- En droit pénal => L'accusation doit prouver son cas "au-delà de tout doute raisonnable"
- En info, c'est ...

<!-- pause -->

# Définition 2 - Système de Preuve interactif

```typst +render
Soit $cal(L)$ un langage sur ${0,1}$ ($cal(L) subset.eq {0,1}^*$). \ On appel *système de preuve interactif pour $cal(L)$* \ toute paire de *machine de turing interactive* $(P,V)$,\ avec $V$ qui termine en $cal(O)(n^k)$ étapes, $k in NN$, \ ($n$ étant la taille du nombre sur le ruban de données initiales), vérifiant :
- *Complétude*: $forall (x, w) in cal(L), #h(0.3cm) cal(P)(P(x circle.filled.tiny w) arrows.rl V(x) = 1) gt.eq.slant 0.9$ 
- *Robustesse*: $forall P^* in cal(M)_"int", #h(0.3cm) forall (x, w) in.not cal(L), #h(0.3cm) cal(P)(P^*(x circle.filled.tiny w) arrows.rl V(x) = 1) lt.eq.slant 0.1$ 
```

<!-- column: 1 -->
<!-- pause -->
```typst +render
#image("../assets/1153.png")
#align(center)[xkcd: 1153]
```


<!-- 
speaker_note: |
    En *Science* on parle de signification statistique.
-->

<!-- end_slide -->

ZKP
===

# Définition 3 - Preuve à divulgation nulle de connaissance

```typst +render
Un *système de preuve interactif* $(P, V)$ *sur* $cal(L)$ est dit à *divulgation nulle de connaissance* si \ pour toute stratégie de vérification efficace (s'exécutant en tps polynomial) $V^*$, il existe un algorithme probabiliste efficace $S^*$, \ tel que pour tout $(x, w) in cal(L)$ les variables aléatoires suivantes sont calculatoirement indiscernable :
- Le transcripte des interactions de $P$ et $V^*$ sur l'entrée $x$ ($P$ disposant de $w$)
- La sortie de $S^*$ sur l'entrée $x$.
```

<!-- pause -->

# Résumé

- complétude
- robustesse
- divulgation nulle de connaissance

<!-- end_slide-->

<!-- jump_to_middle -->

Exemples
===

<!-- end_slide -->

Protocole de Fiat-Shamir
===

![image:width:70%](assets/proto.png)

<!-- pause -->

=> système d'authentification

<!-- end_slide -->

ZK-HAM
=== 

graphe

<!-- end_slide -->

ZK-HAM
=== 

permutation

<!-- end_slide -->

ZK-HAM
=== 

face cachée

<!-- end_slide -->

ZK-HAM
=== 

Le vérifieur décide de vérifier l'isomorphisme de graphe

<!-- end_slide -->

ZK-HAM
=== 

Le vérifieur décide de vérifier que P connait un cycle Hamiltonien pour H

<!-- end_slide -->

<!-- jump_to_middle -->

Applications
=== 

<!-- end_slide -->

<!-- column_layout: [3, 2, 3] -->


<!-- column: 0 -->

<!-- pause -->
```bash +exec_replace +no_background
pokemonsay "Des questions ???" 
```

<!-- column: 1 -->

<!-- pause -->
```bash +exec_replace +no_background
pokemonsay --think "Oui !"
```
<!-- pause -->
```bash +exec_replace +no_background
pokemonsay --think "Oui !"
```

<!-- column: 2 -->

<!-- pause -->
```bash +exec_replace +no_background
pokemonsay --think "Oui !"
```
<!-- pause -->
```bash +exec_replace +no_background
pokemonsay --think "Oui !"
```

<!-- end_slide -->

Meta
===

```bash +exec_replace +no_background
git pull
sleep 2
onefetch -T prose programming
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
- [TD ENS](https://www.di.ens.fr/brice.minaud/cours/2018/TD4.pdf)
- [Cours du MIT](https://courses.csail.mit.edu/6.857/2018/files/L22-ZK-Boaz.pdf)
- [StackExchange Crypto](https://crypto.stackexchange.com)

# Lien vers la présentation

- [Repo github](https://github.com/benoitlx/forma-zkp)
- [Drive Rézo](#todo)

# Misc.

- [`presenterm`](https://github.com/mfontanini/presenterm)
- [`typst`](https://github.com/typst/typst)
- [`pokemonsay`](https://github.com/possatti/pokemonsay)
- [`onefetch`](https://github.com/o2sh/onefetch)
- [`mmdc`](https://github.com/mermaid-js/mermaid-cli)
