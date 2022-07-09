# -*- coding: utf-8 -*-
import logging

import typer
import os
from dotenv import find_dotenv, load_dotenv
from pathlib import Path
import pandas as pd
import numpy as np
import xgboost as xgb


app = typer.Typer()

filename: str = typer.Argument("data", help="dataset filename")
target_column: str = "isFraud"
hyperparameters: dict = {}


@app.command()
def main(filename=filename):
    """
    Predict frauders using machine learning model stored in (outputs/models/),
    cleaned data without fraud label in (data/processed/) & save predictions in (outputs/predictions/).
    """
    logger = logging.getLogger(__name__)
    DIR_DATA_PROCESSED = Path(os.getenv("DIR_DATA_PROCESSED"))
    DIR_OUTPUTS = Path(os.getenv("DIR_OUTPUTS"))

    logger.info('Loading cleaned data & model')
    X = pd.read_csv(f"{DIR_DATA_PROCESSED}/{filename}.csv")

    # to facilitate usage
    if target_column in X.columns:
        X = X.drop(columns=target_column)

    clf = xgb.XGBClassifier()
    clf.load_model(f"{DIR_OUTPUTS}/models/model.pkl")

    logger.info('Predicting using machine learning model')
    y_pred = clf.predict_proba(X)

    np.savetxt(f"{DIR_OUTPUTS}/predictions/predictions.csv", y_pred)
    logger.info('Predictions saved in (outputs/predictions/)')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(), override=True)

    app()

