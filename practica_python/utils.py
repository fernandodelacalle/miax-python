import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from mpl_finance import candlestick_ohlc


def plot_candle(df_ohlc,
                width=.5,
                figsize=(10, 7),
                tick_formater='%Y-%m'):
    """Realiza una figura de velas, necesitas tener el modulo mpl_finance
    installado: pip install mpl_finance

    Parameters
    ----------
    df_ohlc : pd.DataFrame
        Dataframe con columnas: open, high, low, close y el
        indice como DatetimeIndex. No puede tener NaN.
    width : float, optional
        Ancho de las velas, ajustar segun intervalo de tiempo,
        by default .5
    figsize : tuple, optional
        Size de la figura, by default (10, 7)
    tick_formater : str, optional
        Formato de los ticks del eje x, para years '%Y',
        para meses '%Y-%m' y para dias '%Y-%m-%d', by default '%Y-%m'

    Returns
    -------
    (fig, ax): (matplotlib.figure.Figure,
                matplotlib.axes._subplots.AxesSubplot)
        Tupla con la figura y el axes donde se ha pintado.

    Example
    -------
    data_close, data_ibex = utils.read_data()
    """
    assert 'open' in df_ohlc.columns, 'no open in input'
    assert 'high' in df_ohlc.columns, 'no high in input'
    assert 'low' in df_ohlc.columns, 'no low in input'
    assert 'close' in df_ohlc.columns, 'no close in input'
    assert not df_ohlc.isnull().values.any(), 'NaN in the input'
    err_datetime = 'index is not a DatetimeIndex'
    assert isinstance(df_ohlc.index, pd.DatetimeIndex), err_datetime

    m_data = df_ohlc[['open', 'high', 'low', 'close']].values
    days_m_dates_format = mdates.date2num(df_ohlc.index.values)
    data_plot = np.column_stack((days_m_dates_format, m_data))

    fig, ax_candle = plt.subplots(figsize=figsize)
    _ = candlestick_ohlc(ax_candle,
                         data_plot,
                         width=width,
                         colorup='green',
                         colordown='red')
    tick_formater = mdates.DateFormatter(tick_formater)
    _ = ax_candle.xaxis.set_major_formatter(tick_formater)
    return fig, ax_candle


def read_data(file_path='data_close.csv',
              file_path_ibex='ibex_div_data_close.csv',
              from_date='2004'):
    """Lee los datos necesarios para el ejercico 2.

    Parameters
    ----------
    file_path : str, optional
        path del csv data_close.csv, by default 'data_close.csv'
    file_path_ibex: str, optional
        path del csv ibex_div_data_close.csv,
        by default 'ibex_div_data_close.csv'
    from_date : str, optional
        Fecha a partir la que empieza el df, by default '2004'

    Returns
    -------
    (df_close, ibex_div): (pd.Dataframe, pd.Dataframe)
        df_close: df con el cierre de cada uno de los activos como columna
                  fecha como indice. NaN indica que el activo no estaba
                  en el indice
        ibex_div: Serie del cierre del ibex con dividendos.

    Example
    -------
    data_close, ibex_div = utils.read_data()
    """
    df_close = pd.read_csv(file_path, parse_dates=True, index_col=0)
    df_close = df_close[from_date:]

    ibex_div = pd.read_csv(file_path_ibex, parse_dates=True, index_col=0)
    ibex_div = ibex_div[from_date:]

    return df_close, ibex_div
