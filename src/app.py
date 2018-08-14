"""
	Author: Igor Assuncao
	Date: 8/13/2018
"""

import requests

def getTargetInput():
	target = str(input('Target (domain.com for example): '))
	return target

def getWordlist():
	wordlist = str(input('Wordlist (you can leave blank if you want to use our default): '))
	if wordlist == '':
		wordlist = './wordlist/wordlist.txt'
	return wordlist

def mountUrl(target_url, wordlist_item):
	url_prefix = 'http://'
	mountedUrl = '{}{}.{}' .format(url_prefix, wordlist_item, target_url)
	return mountedUrl

def makeRequest(target_url):
	try:
		req = requests.get(target_url)
		if req.status_code == 200 or req.status_code == 301 or req.status_code == 302:
			print('Subdomain found: {}' .format(target_url))
	except:
		print('Subdomain "{}" not found' .format(target_url))
	

def main():
	target = getTargetInput()
	wordlist = getWordlist()
	wordlistFile = open(wordlist, "r")
	for wordlist_item in wordlistFile:
		wordlist_item = wordlist_item.rstrip()
		target_url = mountUrl(target, wordlist_item)
		makeRequest(target_url)

	wordlistFile.close()
		

if __name__ == '__main__':
	main()