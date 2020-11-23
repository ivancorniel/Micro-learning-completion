from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as uReq

URL = 'https://thd.earlyconnect.com'
login_route = '/Account/'

s_headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', 'origin': URL, 'referer': 'https://thd.earlyconnect.com/Account/'}

session = requests.session()

login_info = {'companyId': 'THD', 'userId': 'Jose.cornielhiciano@alorica.com','passwd': 'sjwVbXX6'}

login_req = session.post(URL + login_route, headers = s_headers, data = login_info)

cookies = login_req.cookies


articles_page = bs(session.get('http://thd.earlyconnect.com/Admin/Report/ArticleList.aspx').text, 'html.parser')

articles  = articles_page.findAll("div")

for article in articles:
    print(article.text)
