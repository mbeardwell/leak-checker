#!/bin/python3

import requests
import urllib.parse

DDG_URL = 'https://duckduckgo.com/?q='


def generate_url(engine, query_str):

	if engine == 'duckduckgo':
		params = urllib.parse.urlencode({'q': query_str})
		return DDG_URL + params

	return None

url = generate_url('duckduckgo', 'site:pastebin.com Hello.com')
request = requests.get(url)
print(request.status_code)
print(request.text)
