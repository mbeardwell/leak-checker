#!/bin/python3

import requests
from bs4 import BeautifulSoup

class Result():
	def __init__(self, title, url, description):
		self.title = title
		self.url = url
		self.description = description

	def print(self):
		print('=== Result ===')
		print(f'\t Title: {self.title}')
		print(f'\t URL: {self.url}')
		print(f'\t Description: {self.description}')

	def get_title(self):
		return self.title

	def get_url(self):
		return self.url

	def get_description(self):
		return self.description

def parse_results(html):
	TITLE_CLASS = 'result__a'
	URL_CLASS = 'result__url'
	DESCRIPTION_CLASS = 'result__snippet'

	soup = BeautifulSoup(html, 'html.parser')

	results_html = soup.find_all("div", class_="result")
	results = []

	for html in results_html:
		title = html.find('a', class_=TITLE_CLASS).text.strip()
		url = html.find('a', class_=URL_CLASS).text.strip()
		description = html.find('a', class_=DESCRIPTION_CLASS).text.strip()
		results.append(Result(title, url, description))

	for r in results:
		r.print()

	return results

USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
DDG_URL = 'https://duckduckgo.com/html/?'

query = 'test'
headers = {'user-agent': USER_AGENT}
request = requests.get(DDG_URL + f'q={query}', headers=headers)

print(request.status_code)
print(request.url)

results = parse_results(request.text)
