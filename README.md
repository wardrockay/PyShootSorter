# 📦 Trieur - Organisateur de Photos et Vidéos

Trieur est un script Python qui organise automatiquement vos photos et vidéos en les classant dans des dossiers par date de création. Il extrait les métadonnées (EXIF pour les photos, métadonnées pour les vidéos) et déplace les fichiers dans des dossiers nommés selon la date de prise de vue.

## ✅ Prérequis

* Python 3.x installé sur votre système (vérifiez avec `python --version`)
* Les bibliothèques suivantes (installables via pip):
  * `exifread` - Pour extraire les métadonnées EXIF des photos
  * `hachoir` - Pour extraire les métadonnées des fichiers vidéo
  * `tqdm` - Pour afficher des barres de progression

---

## 🔧 Étapes

### 1. Créer un environnement virtuel

Dans votre terminal (CMD ou PowerShell), placez-vous dans le dossier de votre projet, puis exécutez :

```bash
python -m venv venv
```

Cela créera un dossier `venv/` contenant l’environnement virtuel.

### 2. Activer l’environnement virtuel

Sous **Windows** :

* Avec **CMD** :

  ```bash
  venv\Scripts\activate.bat
  ```

* Avec **PowerShell** :

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

Une fois activé, vous verrez le nom de l’environnement (souvent `(venv)`) au début de votre ligne de commande.

### 3. Installer les dépendances

Assurez-vous que le fichier `requirements.txt` est bien présent, puis exécutez :

```bash
pip install -r requirements.txt
```

### 4. Désactiver l’environnement virtuel (optionnel)

Pour sortir de l’environnement virtuel :

```bash
deactivate
```

---

## 📁 Structure du projet (exemple)

```
mon-projet/
├── venv/               # Environnement virtuel (ne pas versionner)
├── script.py           # Votre script principal
├── requirements.txt    # Liste des dépendances
└── README.md           # Ce fichier
```

---

## 🔒 Bonnes pratiques

* Ajoutez `venv/` dans votre `.gitignore` si vous utilisez Git.
* Utilisez toujours un environnement virtuel pour isoler les dépendances de votre projet.

---

## 📎 Ressources

* [Documentation officielle Python – venv](https://docs.python.org/3/library/venv.html)

---

## 📋 Fonctionnalités

* **Organisation automatique** - Trie les photos et vidéos depuis un dossier source vers des dossiers de destination organisés par date
* **Extraction de métadonnées** - Utilise les données EXIF pour les photos et les métadonnées pour les vidéos
* **Formats supportés**:
  * Photos: jpg, jpeg, png, tif, tiff, nef, dng
  * Vidéos: mp4, mov, avi, mkv
* **Barres de progression** - Affiche l'avancement du traitement avec le nom du fichier en cours
* **Gestion des erreurs** - Traitement robuste des erreurs et possibilité d'interrompre proprement avec Ctrl+C
* **Vérification de placement** - Mode de vérification pour s'assurer que les fichiers sont dans les bons dossiers

## 🚀 Utilisation

1. Exécutez le script:
   ```bash
   python trieur.py
   ```

2. Choisissez l'une des options suivantes:
   * **1: Trie des fichiers** - Pour organiser les fichiers du dossier source vers les dossiers de destination
   * **2: Vérification de l'emplacement des photos** - Pour vérifier si les photos sont correctement placées
   * **3: Quitter** - Pour quitter le programme

## ⚙️ Configuration

Les chemins des dossiers sont définis au début du script:

```python
SOURCE_FOLDER = 'Z:\\bucket'        # Dossier source contenant les fichiers à trier
VIDEO_DEST = 'Z:\\Video'           # Destination pour les vidéos
PHOTO_DEST = 'Z:\\Photo\\RAW'      # Destination pour les photos
```

Modifiez ces variables selon votre configuration.

## 🔍 Structure des dossiers de destination

Les fichiers sont organisés dans des sous-dossiers nommés selon le format `AAAAMMJJ` (année, mois, jour).

Exemple:
```
Z:\Photo\RAW\20250727\photo1.jpg
Z:\Video\20250726\video1.mp4
```
