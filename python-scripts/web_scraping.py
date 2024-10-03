import  requests
from bs4 import BeautifulSoup

link_site = "https://www.grammy.com/awards"
request = requests.get(link_site)

site = BeautifulSoup(request.text, "html.parser")