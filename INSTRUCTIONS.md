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

    1. In order to avoid any frictions I advise you to run this project using Gitpod. The repository is public so
    you can just build a workspace from it. If you want to run it localy on your device you need to have 
    python 3.8 installed, poetry and pyenv or you can use the make commands to download everything needed. 
    For the next steps I assume that you will run it from Gitpod but the comands and steps remain the same if you 
    choose the local way.
    2. Activate the virtual env automatically created at the start of the instance using source .venv/bin/activate
    3. Put your Kaggle username and password in the .secrets file.
    4. Download the data from Kaggle using python3 src/data/download_data.py
    5. Create the cleaned dataset useful in the next steps using python3 src/data/make_dataset.py
    6. Time to train the model using python3 src/models/train_model.py
    7. You can run the predictions using python3 src/models/predict.py
    The predictions are made from the same file used for the training but you can use any file with the right format
    just by placing it in the data/processed/ folder then adding the name of the file at the end of the command. 

    Optional :
        - Create a .venv-dev using the requirements-dev.txt to run the notebook auto-ds
        - You can run all the other notebooks in the regular virtual environment
  