#  ssNA Inverse Folding – Générateur de séquences avec contraintes de structure

Ce mini-projet simule un problème simplifié de **repliement inverse** (inverse folding) d’acides nucléiques simple brin (ssNA).  
Il s’inspire d’une problématique réelle en biologie computationnelle : **comment trouver une séquence d’ADN qui se replie selon une structure secondaire cible ?**

---

## Objectif

L’objectif est de :
1. Générer automatiquement des **séquences d’ADN** (composées de A, T, G, C),
2. Vérifier si elles respectent une **structure secondaire cible** donnée sous forme de notation `dot-bracket`, comme par exemple :

Dans cet exemple, les `(` et `)` indiquent les bases qui doivent être appariées (formant des "ponts" dans la structure), et les `.` indiquent des bases libres.

---

## Fonctionnement

Le projet comprend :
- Un **générateur** de séquences avec un pourcentage de GC contrôlable (`generator.py`),
- Un **validateur** qui évalue la compatibilité de la séquence avec la structure cible (`validator.py`),
- Un **notebook interactif** (`notebook_demo.ipynb`) pour tester les deux modules ensemble.

---

##  Exemple

```txt
Structure cible : (((...)))
Séquence générée : AGCTTTCGA
Appariements valides : 3 sur 3


