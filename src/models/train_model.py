# -*- coding: utf-8 -*-
import logging
import os
from pathlib import Path

import pandas as pd

import typer
from dotenv import find_dotenv, load_dotenv
from xgboost.sklearn import XGBClassifier

app = typer.Typer()

filename: str = typer.Argument("data", help="dataset filename")
target_column: str = "isFraud"
hyperparameters: dict = {}


@app.command()
def main(filename=filename):
    """
    Train machine learning model using cleaned data (saved in ../processed)
    & save model as .pkl file in (outputs/models/).
    """
    logger = logging.getLogger(__name__)
    DIR_DATA_PROCESSED = Path(os.getenv("DIR_DATA_PROCESSED"))
    DIR_OUTPUTS = Path(os.getenv("DIR_OUTPUTS"))

    logger.info("Loading cleaned data")
    df = pd.read_csv(f"{DIR_DATA_PROCESSED}/{filename}.csv")
    X = df.drop(columns=target_column)
    y = df[target_column]

    logger.info("Training machine learning model")
    clf = XGBClassifier(**hyperparameters)

    clf.fit(X, y)

    clf.save_model(f"{DIR_OUTPUTS}/models/model.pkl")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(), override=True)

    app()
