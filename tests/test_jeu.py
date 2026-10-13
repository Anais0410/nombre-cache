"""Tests unitaires du jeu du nombre caché (lancer avec : python -m unittest)."""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import jeu  # noqa: E402


class TestComparer(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(jeu.comparer(10, 42), "plus")

    def test_moins(self):
        self.assertEqual(jeu.comparer(80, 42), "moins")

    def test_gagne(self):
        self.assertEqual(jeu.comparer(42, 42), "gagne")


class TestValiderSaisie(unittest.TestCase):
    def test_saisie_valide(self):
        self.assertEqual(jeu.valider_saisie("25", 100), 25)

    def test_espaces_ignores(self):
        self.assertEqual(jeu.valider_saisie("  7 ", 100), 7)

    def test_bornes_incluses(self):
        self.assertEqual(jeu.valider_saisie("1", 100), 1)
        self.assertEqual(jeu.valider_saisie("100", 100), 100)

    def test_hors_bornes(self):
        self.assertIsNone(jeu.valider_saisie("0", 100))
        self.assertIsNone(jeu.valider_saisie("101", 100))
        self.assertIsNone(jeu.valider_saisie("-5", 100))

    def test_texte_invalide(self):
        self.assertIsNone(jeu.valider_saisie("abc", 100))
        self.assertIsNone(jeu.valider_saisie("", 100))
        self.assertIsNone(jeu.valider_saisie("4.5", 100))


class TestTirerNombre(unittest.TestCase):
    def test_dans_l_intervalle(self):
        for _ in range(1000):
            self.assertTrue(1 <= jeu.tirer_nombre(50) <= 50)


class TestRecord(unittest.TestCase):
    def test_premier_score(self):
        self.assertTrue(jeu.est_meilleur_score(5, None))

    def test_record_battu(self):
        self.assertTrue(jeu.est_meilleur_score(3, 5))

    def test_record_non_battu(self):
        self.assertFalse(jeu.est_meilleur_score(5, 5))
        self.assertFalse(jeu.est_meilleur_score(7, 5))


class TestScores(unittest.TestCase):
    def test_sauvegarde_puis_chargement(self):
        with tempfile.TemporaryDirectory() as dossier:
            fichier = os.path.join(dossier, "scores.json")
            jeu.sauvegarder_scores({"Facile": 4}, fichier)
            self.assertEqual(jeu.charger_scores(fichier), {"Facile": 4})

    def test_fichier_absent(self):
        self.assertEqual(jeu.charger_scores("fichier_inexistant.json"), {})


if __name__ == "__main__":
    unittest.main()
