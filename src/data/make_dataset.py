# -*- coding: utf-8 -*-
import logging

import typer
import os
from dotenv import find_dotenv, load_dotenv
from pathlib import Path
import pandas as pd
from typing import List
from src.features.build_features import (
    compute_balance_error,
    compute_hours_and_days,
    fix_null_balances,
)


app = typer.Typer()

FRAUD_TYPES: List[str] = ["TRANSFER", "CASH_OUT"]
USELESS_FEATURES: List[str] = ["nameOrig", "nameDest", "isFlaggedFraud"]
filename: str = typer.Argument(
    "PS_20174392719_1491204439457_log", help="dataset filename"
)


@app.command()
def main(filename=filename):
    """
    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready for modeling (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    DIR_DATA_RAW = Path(os.getenv("DIR_DATA_RAW"))
    DIR_DATA_PROCESSED = Path(os.getenv("DIR_DATA_PROCESSED"))

    logger.info("Making final data set from raw data")
    df = pd.read_csv(f"{DIR_DATA_RAW}/{filename}.csv")
    df = df.rename(
        columns={
            "oldbalanceOrg": "oldBalanceOrig",
            "newbalanceOrig": "newBalanceOrig",
            "oldbalanceDest": "oldBalanceDest",
            "newbalanceDest": "newBalanceDest",
        }
    )

    df = df.loc[df["type"].isin(FRAUD_TYPES)]

    # Eliminate columns shown to be irrelevant for analysis in the EDA
    df = df.drop(USELESS_FEATURES, axis=1)

    # Binary-encoding of labelled data in 'type'
    df.loc[df["type"] == "TRANSFER", "type"] = 0
    df.loc[df["type"] == "CASH_OUT", "type"] = 1
    df["type"] = df["type"].astype(int)  # convert dtype('O') to dtype(int)

    df = fix_null_balances(df)
    df = compute_balance_error(df)
    df = compute_hours_and_days(df)

    df.to_csv(f"{DIR_DATA_PROCESSED}/data.csv", index=False)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(), override=True)

    app()
