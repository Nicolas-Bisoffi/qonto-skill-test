Qonto Skill Test
==============================

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `create_environment`
    ├── README.md          <- The top-level README for developers using this project which also explain the project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── outputs
    │   ├── models      <- Trained and serialized models, model predictions, or model summaries
    │   │
    │   └── reports     <- Generated analysis as HTML, PDF, LaTeX, etc.
    │      └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── docs               <- A default Mkdocs project
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── pyproject.toml   <- The file containing the build system requirements of Python projects.
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   └──  models         <- Scripts to train models and then use trained models to make
    │       │                 predictions
    │       ├── predict.py
    │       └── train_model.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

# Instructions

    1. Afin d'éviter un maximum de frictions, je vous invite à lancer le projet dans un workspace Gitpod (.gitpod.yml décrit les quelques étapes de paramètrages néessaires lors de la 1ère utilisation du répertoire).
    2. Sur gitpod, le .venv est créé automatiquement. En local, le créer (make create_environment).
    2. Activer le .venv créé lors de l'étape 1 (source .venv/bin/activate). 
    3. Renseigner le nom d'utilisateur et le mot de passe de votre compte Kaggle dans le fichier .secrets à la racine du projet.
    3. Téléchargement des données depuis Kaggle (depuis la racine du projet: python3 src/data/download_data.py)
    4. Nettoyage des données (depuis la racine du projet: python3 src/data/make_dataset.py <OPTIONNAL data_to_be_cleaned_filename>)
    5. Entraînement du modèle de machine learning (depuis la racine du projet: python3 src/models/train_model.py <OPTIONNAL training_filename>)
    6. Prédiction des données (depuis la racine du projet: python3 src/models/predict.py <predict_filename>)
    
    Optionnel:
        - Créer un .venv-dev python3.8.10 à l'aide de requirements-dev.txt, et utiliser notebooks/auto-ds.ipynb
        - A l'aide de .venv, utiliser notebooks/modeling.ipynb, notebooks/eda.ipynb ou notebooks/visualizations.ipynb

 
