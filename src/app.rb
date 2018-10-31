=begin
	Author: Igor Assuncao
	Date: 10/23/2018
=end

require 'uri'
require 'net/http'

def getTargetInput
	print 'Target (domain.com for example): '
	target = gets.to_s.chomp
	return target
end

def getWordlist
	print 'Path to Wordlist (you can leave blank if you want to use our default): '
	wordlist = gets.to_s.chomp
	if wordlist.empty?
		wordlist = './wordlist/wordlist.txt'
	end
	return wordlist
end

def mountDomainUrl(target_url)
	url_prefix = 'http://'
	mounted_url = url_prefix.concat(target_url)
	mounted_url = mounted_url.gsub('\n', '')
	return mounted_url
end

def checkDomain(target_domain_url)
	target_domain_url = target_domain_url.strip
	uri = URI(target_domain_url)
	response = Net::HTTP.get_response(uri)
	case response
	when Net::HTTPSuccess then
		response
	when Net::HTTPRedirection then
		location = response['location']
		warn 'redirected to ' + location
		checkDomain(location)
	else
		response.values
	end
	rescue
		print "Domain #{target_domain_url} not found!"
	
end

def main
	targetDomain = getTargetInput
	wordlist = getWordlist
	targetDomainUrl = mountDomainUrl(targetDomain)
	checkDomain(targetDomainUrl)
end

if __FILE__ == $0
	main
end