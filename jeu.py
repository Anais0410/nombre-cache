"""
Jeu du nombre caché
-------------------
L'ordinateur choisit un nombre au hasard, le joueur doit le deviner.
À chaque essai, le programme indique si le nombre caché est plus grand
ou plus petit. Les meilleurs scores sont sauvegardés dans un fichier JSON.

Auteur : Anaïs Billaud - BTS SIO option SLAM
"""

import json
import random
from pathlib import Path

# Fichier où sont enregistrés les meilleurs scores
FICHIER_SCORES = Path(__file__).parent / "scores.json"

# Chaque niveau définit : la borne maximale et le nombre d'essais autorisés
NIVEAUX = {
    "1": {"nom": "Facile", "max": 50, "essais": 10},
    "2": {"nom": "Moyen", "max": 100, "essais": 8},
    "3": {"nom": "Difficile", "max": 500, "essais": 9},
}


# ---------------------------------------------------------------------------
# Logique du jeu (fonctions "pures", faciles à tester)
# ---------------------------------------------------------------------------

def tirer_nombre(maximum):
    """Retourne un nombre entier aléatoire entre 1 et maximum (inclus)."""
    return random.randint(1, maximum)


def comparer(proposition, secret):
    """
    Compare la proposition du joueur au nombre secret.
    Retourne "plus" si le secret est plus grand,
             "moins" s'il est plus petit,
             "gagne" si le joueur a trouvé.
    """
    if proposition < secret:
        return "plus"
    if proposition > secret:
        return "moins"
    return "gagne"


def valider_saisie(texte, maximum):
    """
    Vérifie que la saisie est un entier compris entre 1 et maximum.
    Retourne l'entier si la saisie est valide, sinon None.
    """
    texte = texte.strip()
    if not texte.lstrip("-").isdigit():
        return None
    nombre = int(texte)
    if 1 <= nombre <= maximum:
        return nombre
    return None


def est_meilleur_score(nb_essais, ancien_record):
    """Indique si le nombre d'essais bat le record (None = pas encore de record)."""
    return ancien_record is None or nb_essais < ancien_record


# ---------------------------------------------------------------------------
# Sauvegarde des scores
# ---------------------------------------------------------------------------

def charger_scores(fichier=FICHIER_SCORES):
    """Lit les meilleurs scores depuis le fichier JSON (dictionnaire vide si absent)."""
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def sauvegarder_scores(scores, fichier=FICHIER_SCORES):
    """Écrit les meilleurs scores dans le fichier JSON."""
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Interface console
# ---------------------------------------------------------------------------

def choisir_niveau():
    """Affiche le menu des niveaux et retourne le niveau choisi."""
    print("\nChoisis un niveau :")
    for cle, niveau in NIVEAUX.items():
        print(f"  {cle}. {niveau['nom']} (1 à {niveau['max']}, {niveau['essais']} essais)")
    while True:
        choix = input("Ton choix : ").strip()
        if choix in NIVEAUX:
            return NIVEAUX[choix]
        print("Choix invalide, tape 1, 2 ou 3.")


def jouer_partie(niveau, scores):
    """Déroule une partie complète. Retourne True si le joueur a gagné."""
    secret = tirer_nombre(niveau["max"])
    essais_restants = niveau["essais"]
    nb_essais = 0

    print(f"\nJ'ai choisi un nombre entre 1 et {niveau['max']}. À toi de jouer !")

    while essais_restants > 0:
        saisie = input(f"[{essais_restants} essai(s) restant(s)] Ta proposition : ")
        proposition = valider_saisie(saisie, niveau["max"])

        if proposition is None:
            print(f"Merci d'entrer un nombre entier entre 1 et {niveau['max']}.")
            continue  # une saisie invalide ne coûte pas d'essai

        nb_essais += 1
        essais_restants -= 1
        resultat = comparer(proposition, secret)

        if resultat == "gagne":
            print(f"Bravo ! Tu as trouvé {secret} en {nb_essais} essai(s).")
            record = scores.get(niveau["nom"])
            if est_meilleur_score(nb_essais, record):
                print("Nouveau record pour ce niveau !")
                scores[niveau["nom"]] = nb_essais
                sauvegarder_scores(scores)
            return True

        print("C'est plus !" if resultat == "plus" else "C'est moins !")

    print(f"Perdu... Le nombre caché était {secret}.")
    return False


def afficher_scores(scores):
    """Affiche les records de chaque niveau."""
    print("\n--- Meilleurs scores ---")
    for niveau in NIVEAUX.values():
        record = scores.get(niveau["nom"])
        texte = f"{record} essai(s)" if record else "pas encore de record"
        print(f"  {niveau['nom']} : {texte}")


def main():
    """Point d'entrée du programme : boucle principale du menu."""
    print("=== Jeu du nombre caché ===")
    scores = charger_scores()

    while True:
        print("\n1. Jouer\n2. Voir les meilleurs scores\n3. Quitter")
        choix = input("Ton choix : ").strip()
        if choix == "1":
            jouer_partie(choisir_niveau(), scores)
        elif choix == "2":
            afficher_scores(scores)
        elif choix == "3":
            print("À bientôt !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
