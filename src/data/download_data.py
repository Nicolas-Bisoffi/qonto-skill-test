import logging
import os
from pathlib import Path

import typer
from dotenv import find_dotenv, load_dotenv

KAGGLE_FILENAME: str = "ealaxi/paysim1"

app = typer.Typer()


@app.command()
def main():
    """
    Authenticate on Kaggle using the .env file or ~/.kaggle/kaggle.json file & download data
    """
    # Kaggle check if username & token are in env variables, or in ~/.kaggle/kaggle.json, at the import ...
    # But .secrets is not yet loaded, then this import is made here ...
    from kaggle.api.kaggle_api_extended import KaggleApi

    logger = logging.getLogger(__name__)
    DIR_DATA_RAW = Path(os.getenv("DIR_DATA_RAW"))

    logger.info("Authenticate on the Kaggle API")
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()

    logger.info("Download data & store in the raw data folder")
    kaggle_api.dataset_download_files(KAGGLE_FILENAME, path=DIR_DATA_RAW, unzip=True)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(), override=True)
    load_dotenv(find_dotenv(".secrets"), override=True)

    app()
