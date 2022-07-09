import pandas as pd


def compute_balance_error(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute balance error

    :param df: transactional dataframe
    :return: dataframe with balances error features
    """
    df_ = df.copy()
    df_['errorBalanceOrig'] = df['newBalanceOrig'] + df['amount'] - df['oldBalanceOrig']
    df_['errorBalanceDest'] = df['oldBalanceDest'] + df['amount'] - df['newBalanceDest']

    return df_


def compute_hours_and_days(df: pd.DataFrame) -> pd.DataFrame:
    """
    Deduce hour of the day & day of the week using 'step' features

    :param df: transactional dataframe
    :return: dataframe with datetime features
    """
    df_ = df.copy()
    df_['hourOfDay'] = df['step'] % 24
    df_['dayOfWeek'] = df['step'] % 7

    return df_


def fix_null_balances(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fix null balances when transaction amount is not null

    :param df: transactional dataframe
    :return: dataframe with balances error features
    """
    df_ = df.copy()
    df_.loc[(df_['oldBalanceDest'] == 0) & (df_['newBalanceDest'] == 0) & (df_['amount'] != 0),
            ['oldBalanceDest', 'newBalanceDest']] = -1
    df_.loc[(df_['oldBalanceOrig'] == 0) & (df_['newBalanceOrig'] == 0) & (df_['amount'] != 0),
            ['oldBalanceOrig', 'newBalanceOrig']] = -1

    return df_
