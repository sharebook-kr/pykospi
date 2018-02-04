import requests
import urllib
import json
from pandas import DataFrame


def request_daily_stock_price(date, bid, uid):
    """
    Get daily stock price data including some of financial data from the KRX

    Parameters
    ----------
    date : string, e.g. '2018-02-02' or '20180202'
    bid : bid for each screen number
    uid : uid for each screen number

    Returns
    -------
    ret : DataFrame
    """
    inquiry_date = date.replace('-', '')

    # generate OTP
    url = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx"
    payload = {
        "bld": "MKD/02/0206/%s/mkd%s" % (bid, bid),
        "name": "form",
        "_": uid
    }
    resp = requests.get(url, params=payload)
    otp = resp.text

    # request market data
    url2 = "http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx"
    params = {
        "schdate": inquiry_date,
        "pagePath":"/contents/MKD/02/0206/%s/MKD%s.jsp" % (bid, bid),
        "code": otp
    }

    encode_params = urllib.parse.urlencode(params)
    r = requests.post(url=url2, params = encode_params)

    data = json.loads(r.content)
    table = data['block1']

    df = DataFrame(table)
    return df


def request_10049(date):
    bid = "02060101"
    uid = "1517409064676"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10056(date):
    bid = "02060202"
    uid = "1517744237249"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10057(date):
    bid = "02060203"
    uid = "1517744237253"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10058(date):
    bid = "02060204"
    uid = "1517744237257"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10059(date):
    bid = "02060205"
    uid = "1517744237261"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10060(date):
    bid = "02060206"
    uid = "1517744237265"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10061(date):
    bid = "02060207"
    uid = "1517744237269"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10062(date):
    bid = "02060208"
    uid = "1517744237273"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10063(date):
    bid = "02060209"
    uid = "1517744237277"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


def request_10064(date):
    bid = "02060210"
    uid = "1517744237281"
    ret = request_daily_stock_price(date, bid, uid)
    return ret


if __name__ == "__main__":
    #df = request_10049("2018-02-02")
    #df = request_10056("2018-02-02")
    df = request_10064("2018-02-02")
    print(df)
