import requests
import urllib
import json

def request_10049(inquiry_date):
    url = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx"
    payload = {
        "bld": "MKD/02/0206/02060101/mkd02060101",
        "name":"form",
        "_":"1517409064676"
    }

    resp = requests.get(url, params=payload)
    otp = resp.text
    #print(otp)

    # data
    url2 = "http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx"
    params = {
        "schdate":"20180131",
        "pagePath":"/contents/MKD/02/0206/02060101/MKD02060101.jsp",
        "code":otp
    }

    encode_params = urllib.parse.urlencode(params)
    r = requests.post(url=url2, params = encode_params)
    #print(r.content)

    data = json.loads(r.content)
    table = data['block1']
    print(table)


