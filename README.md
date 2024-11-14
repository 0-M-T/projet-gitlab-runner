# Rapport : Mise en place d'un pipeline CI/CD avec GitLab et Hatch

## 1. Création du projet avec Hatch
La première étape a consisté à créer un projet Python avec **Hatch**, un gestionnaire d'environnements pour les projets Python. En exécutant la commande hatch new my-arithmetic-$USER, la structure du projet a été générée correctement, incluant les répertoires nécessaires tels que src/ et tests/.

**Problème rencontré :**
Aucun problème rencontré durant cette étape.

---

## 2. Implémentation de la fonction PGCD
J'ai ensuite implémenté une fonction qui calcule le Plus Grand Commun Diviseur (PGCD) de deux nombres. La fonction a été ajoutée dans le fichier gcd.py situé dans le dossier src/my_arithmetic/.

**Code de la fonction :**

python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



**Problème rencontré :**
Aucun problème rencontré lors de l'implémentation de cette fonction.

---

## 3. Création des tests unitaires
J'ai créé un fichier de tests, test_gcd.py, dans le dossier tests/ pour vérifier que la fonction PGCD fonctionne correctement. Plusieurs cas de test ont été ajoutés pour couvrir différents scénarios (valeurs positives, zéro, etc.).

**Code des tests :**

python
import unittest
from my_arithmetic.gcd import gcd

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 10), 1)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(7, 0), 7)
        self.assertEqual(gcd(0, 5), 5)

if __name__ == "__main__":
    unittest.main()



**Problème rencontré :**
Aucun problème rencontré lors de la création et de l'exécution des tests unitaires.

---

## 4. Exécution des tests avec Hatch
Une fois les tests créés, j'ai activé l'environnement virtuel avec Hatch et exécuté les tests via les commandes suivantes :

bash
hatch shell
hatch test


Les tests ont été exécutés avec succès et tous les tests ont passé sans erreur.

**Problème rencontré :**
Aucun problème rencontré lors de l'exécution des tests.

---

## 5. Installation et configuration de GitLab Runner
L'installation de **GitLab Runner** a causé un problème initial : la commande gitlab-runner n'était pas reconnue car le chemin d'installation n'était pas ajouté au PATH.

**Solution :**
J'ai ajouté le dossier d'installation de GitLab Runner au PATH du système, ce qui a permis de résoudre ce problème.

---

## 6. Liaison de GitLab Runner avec le projet
Après l'installation de GitLab Runner, j'ai tenté de le lier à mon projet GitLab en utilisant la commande suivante :

bash
.\gitlab-runner.exe register --url https://gitlab.univ-lr.fr --token glrt-t3_NeUqYyFpe1F5GzsB-GxL


Une erreur liée à la commande git non reconnue est apparue.

**Solution :**
J'ai installé Git et ajouté son dossier au PATH. J'ai ensuite configuré Git avec les commandes :

bash
git config --global user.name "TonNom"
git config --global user.email "TonEmail@example.com"



---

## 7. Création du fichier .gitlab-ci.yml
Le fichier .gitlab-ci.yml a été créé pour configurer le pipeline CI/CD et exécuter les tests unitaires à chaque modification de code. Voici le contenu du fichier :

yaml
image: python:3.11

stages:
  - test

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

before_script:
  - pip install --upgrade pip
  - pip install hatch

test_job:
  stage: test
  script:
    - hatch env create
    - hatch run test



**Problème rencontré :**
Aucun problème rencontré lors de la création et de la configuration du fichier .gitlab-ci.yml.

---

## 8. Pousser les modifications sur GitLab
Une fois le fichier .gitlab-ci.yml créé, j'ai ajouté, commité et poussé les modifications vers le dépôt GitLab avec les commandes :

bash
git add .gitlab-ci.yml
git commit -m "Ajout du fichier .gitlab-ci.yml pour exécution des tests unitaires"
git push origin main



**Problème rencontré :**
Initialement, la commande git n'était pas reconnue. Cela a été résolu après l'installation de Git et la mise à jour du PATH.

---

## 9. Vérification du pipeline sur GitLab
Après avoir poussé les modifications, j'ai vérifié que le pipeline CI/CD était correctement exécuté dans GitLab, sous **CI/CD > Pipelines**. Les tests unitaires ont été lancés automatiquement et ont réussi sans erreur.

---
---

## 10. Ajout de badge
J'ai commencé à tester l'ajout de badge mais je n'ai malheureusement pas réussi d'ou mes dernières erreurs.

---
---

## 11. Mirroir gitlab et github
J'ai réussi à lier Gitlab et Github pour que chaque maj sur Gitlab soit envoyée sur Github.

---

## Conclusion
### Problèmes rencontrés :
- Git n'était pas installé correctement sur Windows, ce qui a empêché l'exécution des commandes Git et la liaison de GitLab Runner au projet.
- Le chemin d'installation de GitLab Runner n'était pas ajouté au PATH, causant des erreurs lors de l'enregistrement du runner.

### Solutions apportées :
- Installation correcte de Git et ajout au PATH.
- Ajout du chemin d'installation de GitLab Runner au PATH.

### Résultat :
Le pipeline CI/CD fonctionne désormais correctement et exécute les tests unitaires à chaque modification de code, comme prévu.

---
[![coverage report](https://gitlab.univ-lr.fr/tmaucote/projet-gitlab-runner/badges/main/coverage.svg)](https://gitlab.univ-lr.fr/tmaucote/projet-gitlab-runner/-/commits/main)