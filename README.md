# 🎯 Jeu du nombre caché

Jeu en console développé en **Python** dans le cadre de mon BTS SIO option SLAM.
L'ordinateur choisit un nombre au hasard, et le joueur doit le deviner en un nombre d'essais limité.

## ✨ Fonctionnalités

- **3 niveaux de difficulté** : Facile (1 à 50), Moyen (1 à 100), Difficile (1 à 500)
- **Indices** à chaque essai : « C'est plus ! » / « C'est moins ! »
- **Contrôle des saisies** : un texte ou un nombre hors limites est refusé sans faire perdre d'essai
- **Meilleurs scores** sauvegardés dans un fichier `scores.json` et conservés entre deux parties
- **Tests unitaires** sur toute la logique du jeu

## 🚀 Lancer le jeu

Prérequis : Python 3.8 ou plus récent, sans aucune bibliothèque à installer.

```bash
python jeu.py
```

## 🧪 Lancer les tests

```bash
python -m unittest discover tests -v
```

## 🗂️ Organisation du code

```
nombre-cache/
├── jeu.py            # le programme
├── tests/
│   └── test_jeu.py   # les tests unitaires
└── README.md
```

Le code sépare deux parties :

| Partie | Fonctions | Rôle |
|---|---|---|
| Logique | `tirer_nombre`, `comparer`, `valider_saisie`, `est_meilleur_score` | Règles du jeu, sans affichage : faciles à tester |
| Sauvegarde | `charger_scores`, `sauvegarder_scores` | Lecture et écriture du fichier JSON |
| Interface | `choisir_niveau`, `jouer_partie`, `afficher_scores`, `main` | Menus et échanges avec le joueur |

## 📚 Notions utilisées

Variables, conditions (`if / elif / else`), boucles (`while`, `for`), fonctions, dictionnaires,
gestion des exceptions (`try / except`), lecture et écriture de fichiers JSON, tests unitaires avec `unittest`.

## 👩‍💻 Autrice

**Anaïs Billaud**, étudiante en BTS SIO option SLAM
