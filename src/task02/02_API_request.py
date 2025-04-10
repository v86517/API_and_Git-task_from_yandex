import requests
from bs4 import XMLParsedAsHTMLWarning, BeautifulSoup as bs
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

mytext = 'sky'
translate_lang = 'en-ru'
interface = 'ru'

URL = "https://dictionary.yandex.net/api/v1/dicservice/lookup"  #это адрес для обращения к API
KEY = "dict.1.1.20250403T232543Z.4ed7189b9dd293bd.ca948be992d9c3e4f79744f8a4934a334ffb5ccb" #Это ваш API ключ

def get_API_response(mytext):
    params = {
        "key": KEY,
        "text": mytext,
        "lang": translate_lang,
        "ui" : interface
    }
    response = requests.get(URL ,params=params)
    return response

response_xml = get_API_response(mytext)
soup= bs(response_xml.text,"lxml")

with open("02_API_response_python.xml", "w", encoding='utf-8') as file:
    file.write(str(soup.prettify()))


#################################################
#resp_xml_content = get_API_response(mytext).content
#print(type(resp_xml_content))
#print(f"{resp_xml_content}")

################################################
'''response_xml = get_API_response(mytext).text
print(type(response_xml))
print(response_xml)
tree = ET.XML(response_xml)
with open('res.xml', 'wb') as file:
    file.write(ET.tostring(tree))'''

