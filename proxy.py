
from requests import get
from bs4 import BeautifulSoup as parser
import re

# variabel data
prox = []

# dump proxy
def proxy():
	try:
		link = parser(get("https://hidemy.name/en/proxy-list/?country=IRRUUS&type=5#list",headers={"user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}).text, "html.parser")
		for x in re.findall("<tr><td>(.*?)</td><td>(.*?)</td><td>",str(link)):
			if 'IP' in str(x):
				pass
			else:
				prox.append(x[0]+':'+x[1])
	except requests.exceptions.ConnectionError:
		exit(" tidak ada koneksi internet")
	return prox

print (proxy())


