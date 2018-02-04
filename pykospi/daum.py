import pandas as pd
from datetime import datetime


def get_daily_data(name, start="2010-01-01", end=None, modify=1):
    """
    Get dailay open/high/low/close/volume data from Data Finanace

    Parameters
    ----------
    name : string of ticker, e.g. '000660'
    start : string, e.g. '2010-01-01'
    end : string, e.g. '2018-01-31'
    modify : int
        0: close
        1: adj close

    Returns
    -------
    ret : DataFrame
    """
    start = datetime.strptime(start, "%Y-%m-%d")

    if end is None:
        end = datetime.now()

    frames = []
    page= 1

    while True:
        url_form = "http://finance.daum.net/item/quote_yyyymmdd_sub.daum?page=%d&code=%s&modify=%d"
        url = url_form % (page, name, modify)
        page += 1
        dfs = pd.read_html(url, header=0)
        df = dfs[0]

        if df.empty:
            break

        # delete N/A rows
        df = df.dropna()

        date = pd.to_datetime(df['일자'], format="%y.%m.%d")
        df = df.drop(['일자', '전일비', '등락률'], axis=1)
        df.set_index(date, inplace=True)

        df.index.names = ['Date']
        df = df.rename(index=str, columns={"시가": "Open", "고가": "High", "저가": "Low", "종가": "Close", "거래량": "Volume"})
        frames.append(df)

        if date.iloc[-1] <= start:
            break

    df = pd.concat(frames)
    date = pd.to_datetime(df.index, format="%Y-%m-%d %H:%M:%S")
    df.set_index(date, inplace=True)

    end_dtime = datetime.strptime(end, "%Y-%m-%d")
    df = df.iloc[::-1]
    ret = df[start:end_dtime]
    return ret


df = get_daily_data("000020", start="2017-12-25", end="2018-01-13")
print(df)
