import requests
from bs4 import BeautifulSoup
headers = {
    'authority': 'ost.ecosoftbd.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://ost.ecosoftbd.com',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://ost.ecosoftbd.com/Login?ReturnUrl=%2f',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.2.2029686924.1619799079; _fbp=fb.1.1619799080382.1929135909; _hjid=478ca560-7bc4-4f2a-9c6c-481f95ebc30e; _fw_crm_v=0d75dab8-66e9-4efa-be89-070a1d7955b7; _gid=GA1.2.1431901167.1619930111; _hjTLDTest=1; _hjAbsoluteSessionInProgress=0; LastLoginId=arif0171; LastUserName=arif0171 [Arifur Rahman]; tz=360; .ASPXAUTH=C138CB4599C3C597C4F30AC09EB874F3458589F8E4A8239A155A40937828CCCBAB1C171F43F0D7FA0846DB89DB98975007095AD2DE61C6E1041BA674A29908EE5A54EEF1317375162AA6E726091DE30010157ACC99B2B1B1CF43D116F1C11A858748454A4C4BE7CBD8A833AB7839B0185ECE24CC9DE21EBFF9FB4ABE057D3481718D1D171A1EF189; arp_scroll_position=1060',
}

params = (
    ('ReturnUrl', '/'),
)

data = {
  'ReturnUrl': '/',
  'LoginId': 'arif0171',
  'Password': '12341234'
}
s = requests.Session()
response = s.post('https://ost.ecosoftbd.com/Login', headers=headers, params=params, data=data)
print(response.status_code)

analysis_data = s.get("https://ost.ecosoftbd.com/Analysis")
print(analysis_data.status_code)

soup = BeautifulSoup(analysis_data.text, 'html.parser')

print(soup.prettify())