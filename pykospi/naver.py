from bs4 import BeautifulSoup
import requests
import json


def get_per(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("[id=_per]")

    try:
        per = tags[0].text
        per = per.replace(",", "")
        per = float(per)
    except:
        per = 0

    return per


def get_pbr(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("[id=_pbr]")

    try:
        pbr = tags[0].text
        pbr= pbr.replace(",", "")
        pbr = float(pbr)
    except:
        pbr = 0

    return pbr


def get_code_list():
    url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
    text = requests.get(url).content
    code_dic = json.loads(text)

    ret = {}
    for item in code_dic['Co']:
        code = item['cd']
        name = item['nm']
        ret[code] = name

    return ret
