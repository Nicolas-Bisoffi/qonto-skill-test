from kaggle.api.kaggle_api_extended import KaggleApi

import logging

import typer
import os
from dotenv import find_dotenv, load_dotenv
from pathlib import Path

KAGGLE_FILENAME: str = 'ealaxi/paysim1'

app = typer.Typer()


def kaggle_authentication() -> 'KaggleApi':
    """
    Authenticate on Kaggle.

    :return: KaggleApi object used to download data
    """
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()
    return kaggle_api


def download_data(kaggle_api: 'KaggleApi', kaggle_filename: str, data_path: Path) -> None:
    """
    Download data from Kaggle.

    :param kaggle_api: Kaggle API object already authenticated
    :param kaggle_filename: filename on Kaggle
    :param data_path: folder path where data are stored after download
    :return: None
    """
    kaggle_api.dataset_download_files(kaggle_filename, path=data_path, unzip=True)


@app.command()
def main():
    logger = logging.getLogger(__name__)
    DIR_DATA_RAW = Path(os.getenv("DIR_DATA_RAW"))

    logger.info(
        "Authenticate on the Kaggle API"
    )
    kaggle_api = kaggle_authentication()

    logger.info(
        "Download data & store in raw data folder"
    )
    download_data(kaggle_api, KAGGLE_FILENAME, DIR_DATA_RAW)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(), override=True)

    app()
