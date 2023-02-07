import requests

cookies = {
    'MGH_TOKEN': '3edc8677-6921-43cf-90a8-3ae50e1080a8_1661820649593',
    '_gcl_au': '1.1.659570131.1661820668',
    '_mkto_trk': 'id:128-SJW-347&token:_mch-mheducation.com-1661820667820-24936',
    '_hjSessionUser_1239839': 'eyJpZCI6IjBhMmExMjQyLWEwNWItNTYyMC05NTE1LWMzN2U5MzQxMzUxNCIsImNyZWF0ZWQiOjE2NjE4MjA2Njg0NDQsImV4aXN0aW5nIjp0cnVlfQ==',
    '_uetvid': 'd597913027fd11ed8339bbb68daa5ad8',
    '_clck': '1qt1vg9|1|f5l|0',
    '_tt_enable_cookie': '1',
    '_ttp': '1cbe0ebf-ca48-4bb6-9aa3-eb1419a5f013',
    '_scid': '7275bc0a-1c6b-4801-85d3-b8e84ea0d91b',
    '_sctr': '1|1665374400000',
    'QSI_SI_eff3Q59oqYYGsIt_intercept': 'true',
    'AMCV_C5E7148954EA18A10A4C98BC%40AdobeOrg': '-432600572%7CMCIDTS%7C19307%7CMCMID%7C01896487790972647584072608935657864784%7CMCAAMLH-1668644725%7C7%7CMCAAMB-1668644725%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1668047125s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2',
    'mbox': 'PC#f3e87c19c89f4972abcab39097c5c04a.34_0#1731284726|session#1047a5863808455cbac2dbb7f331030a#1668041786',
    's_vnum': '1670631926142%26vn%3D1',
    '_hjSessionUser_1047156': 'eyJpZCI6IjE5YzIzNWU5LWYzMWQtNTIzYS05ZGQzLTMxYmU5OGViYzRhNyIsImNyZWF0ZWQiOjE2NjU0MzUzMTM4NTYsImV4aXN0aW5nIjp0cnVlfQ==',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Nov+09+2022+19%3A25%3A27+GMT-0500+(Eastern+Standard+Time)&version=6.26.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A0%2CC0003%3A0%2CC0001%3A1%2CC0002%3A0&AwaitingReconsent=false',
    'lastVisitDays': '1668039932315',
    's_nr': '1668039932316-New',
    'WT_FPC': 'id=2f03844b642d2441ce71668039955727:lv=1668039955727:ss=1668039955727',
    '_ga_PLHBV8JW7L': 'GS1.1.1668039937.1.1.1668039968.0.0.0',
    '_ga': 'GA1.2.1401296639.1661820668',
    'ssoCookie': 'true',
    '_gid': 'GA1.2.2042844784.1668366415',
    }

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    'Referer': 'https://ezto.mheducation.com/ext/map/index.html?_con=con&external_browser=0&launchUrl=https%253A%252F%252Flms.mheducation.com%252Fmghmiddleware%252Fmheproducts%252FlmsCloseWindow.htm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


response = requests.get('https://ezto.mheducation.com/api/caa/item/render/kEZASsBkEPuPUnsPhrXUIG1vNj5BpY5SdEDBsvH0OIOexSVjZJu0RLS3aYv4AEb1dQaFv32PFlrq_4GEWjLNfPn0Dd5Fi_qM25f3Riu5FbL1liONFeQXkw', cookies=cookies, headers=headers)
response = requests.get('https://ezto.mheducation.com/api/caa/item/render/kEZASsBkEPuPUnsPhrXUIG1vNj5BpY5SdEDBsvH0OIOexSVjZJu0RKLSb2HjWMtFKQKib6Sp2Y0U8JSSC2u5tMIlA8UDbtZdKLvlubM5iTNKNcUtEq8lIA'
                        
print(response.text)