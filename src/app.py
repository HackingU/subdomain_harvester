"""
	Author: Igor Assuncao
	Date: 8/13/2018
"""

import requests

def getTargetInput():
	text = 'Target (domain.com for example): '
	target = str(input(text))
	return target

def getWordlist():
	text = 'Path to Wordlist (you can leave blank if you want to use our default): '
	wordlist = str(input(text))
	if wordlist == '':
		wordlist = './wordlist/wordlist.txt'
	return wordlist

def mountDomainUrl(target_url):
	url_prefix = 'http://'
	mountedUrl = '{}{}' .format(url_prefix, target_url)
	return mountedUrl

def checkDomain(target_domain_url):
	try:
		statusCodes = [200, 201, 202, 204, 206, 301, 302, 401, 403]
		req = requests.get(target_domain_url)
		if req.status_code in statusCodes:
			print('Domain found: {} - status_code: {}' .format(target_domain_url, req.status_code))
	except:
		print('Domain "{}" not found' .format(target_domain_url))

def mountSubdomainUrl(target_url, wordlist_item):
	url_prefix = 'http://'
	mounted_url = '{}{}.{}' .format(url_prefix, wordlist_item, target_url)
	return mounted_url

def makeRequest(target_url):
	statusCodes = [200, 301, 302, 401, 403]
	try:
		req = requests.get(target_url)
		if req.status_code in statusCodes:
			print('Subdomain "{}" found - status_code: {}' .format(target_url, req.status_code))
	except:
		print('Subdomain "{}" not found' .format(target_url))
	

def main():
	targetDomain = getTargetInput()
	wordlist = getWordlist()
	targetDomainUrl = mountDomainUrl(targetDomain)
	checkDomain(targetDomainUrl)
	print('-' * 25)
	if checkDomain(targetDomainUrl):
		wordlistFile = open(wordlist, "r")
		for wordlist_item in wordlistFile:
			wordlist_item = wordlist_item.rstrip()
			target_url = mountSubdomainUrl(targetDomainUrl, wordlist_item)
			makeRequest(target_url)

		wordlistFile.close()
		

if __name__ == '__main__':
	main()
