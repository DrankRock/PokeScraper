#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:44:33 2021

@author: mat
"""
import requests
import re
import sys
import os.path
from bs4 import BeautifulSoup
#-##############################-#
# ---------- ✖︎ TODO ✔︎ -----------#
#  		✖︎ - Finish the PyDoc	 #
#		✖︎ - Make a GUI			 #
#		✖︎ - Manage Exceptions    #
#		✖︎ - Do the Git Doc       #
#		✖︎ - Add tools to track $ #
#-##############################-#

def usage():
	print("Usage : python pokeScrap.O.1.py [link to cardmarket page of card in french or english]")


"""
PokeScraper is a scraping project with the objective to facilitate the use of CardMarket
for Pokemon when tracking prices of single cards.
Argument is either a link to a cardmarket page of a pokemon single card, or a file containing a bunch of https adresses.

Output currently is a cvs format in the terminal, but tends to be inside a file.
I will make it for a terminal use but will make a GUI for other users when I have the time.

    Usage : python pokeScrap.O.1.py [link to cardmarket page of card] or [file containing links]

"""
"""
	PokeScraper() is the main class
	:param url: the url of the card to scrape
"""
class PokeScraper():
	def __init__(self, url):
		self.url = url

	"""
	scrape the parameters and output them in the cvs format
	"""
	def paramScrap(self):
		"""
		for each parameters, get only the value
		:param parameter: the index of the parameter in the parameters list
		:param paramString: a string containing the name of the parameter as used in cardmarket's url
		"""
		def singleParamScrap(parameter, paramString):
			if parameter >= 0:
				content = self.params[parameter]
				splitted_content = content.split("=")
				splitted_content = str(splitted_content[1]).replace(",",";")
				self.paramliste.append(splitted_content)
			else:
				content = 'None'
				self.paramliste.append(content)
		# get the list of all the parameters in the url
		self.params = self.params_ref.split("&")
		self.paramliste = []
		# these are the interesting parameters, that we will put in the cvs output, we want to get their values
		language = self.index_containing_substring(self.params, "language")
		sellerType = self.index_containing_substring(self.params, "sellerType")
		minCondition = self.index_containing_substring(self.params, "minCondition")
		isSigned = self.index_containing_substring(self.params, "isSigned")
		isFirstEd = self.index_containing_substring(self.params, "isFirstEd")
		isPlayset = self.index_containing_substring(self.params, "isPlayset")
		isAltered = self.index_containing_substring(self.params, "isAltered")
		# make use of singleParamScrap to update paramliste with only the values
		singleParamScrap(language, "language")
		singleParamScrap(sellerType, "sellerType")
		singleParamScrap(minCondition, "minCondition")
		singleParamScrap(isSigned, "isSigned")
		singleParamScrap(isFirstEd, "isFirstEd")
		singleParamScrap(isPlayset, "isPlayset")
		singleParamScrap(isAltered, "isAltered")
		# No need of a return, we can use self.paramliste

	def index_containing_substring(self, the_list, substring):
	    for i, s in enumerate(the_list):
	        if substring in s:
	              return i
	    return -1

	def Main(self):
		splitted_URL = self.url.split("/")
		langage = splitted_URL[3]
		jeu = splitted_URL[4]
		extension_ref = splitted_URL[7]
		name_ref = splitted_URL[8]
		name_ref_split = name_ref.split("?")
		if len(name_ref_split) == 1 :
			self.params_ref = ''
		else:
			self.params_ref = name_ref_split[1]
		name_ref = name_ref_split[0]

		page = requests.get(self.url)
		soup = BeautifulSoup(page.content, "html.parser")
		name_uncut = soup.find_all("div", class_="flex-grow-1")
		name = re.search('><h1>(.*)<span', str(name_uncut))
		name = name.group(1)
		extension_uncut = soup.find_all("a", class_="mb-2")
		extension = re.search('">(.*)</a',str(extension_uncut))
		extension = extension.group(1)
		Prices_uncut = soup.find_all("dd", class_="col-6 col-xl-7")
		Prices_uncut = Prices_uncut[5:]
		allPrices = []
		for item in Prices_uncut:
		    allPrices.append(re.search('>(\d.*€)<', str(item)).group(1))

		print(allPrices)
		#print("mean30 uncut = ",mean30)
		out = [extension, name, allPrices[0].replace(",","."), allPrices[2].replace(",",".")]
		self.paramScrap()
		self.paramliste.append(self.url)
		return out+self.paramliste

def MultiPokeScrapURL(file):
	print("extension,name,min_price,mean30d_price,language,sellerType,minCondition,isSigned,isFirstEd,isPlayset,isAltered,url")
	file1 = open(file, 'r')
	Lines = file1.readlines()
	for line in Lines:
	    currentline = str(line.strip())
	    pk = PokeScraper(currentline)
	    print(', '.join(pk.Main()))

if len(sys.argv) == 2:
	arg = sys.argv[1]
	if arg.startswith("https://www.cardmarket.com/fr/Pokemon/Products/Singles/") or arg.startswith("https://www.cardmarket.com/en/Pokemon/Products/Singles/"):
		pk = PokeScraper(sys.argv[1])
		print(', '.join(pk.Main()))
	elif os.path.isfile(arg):
		MultiPokeScrapURL(arg)
	else:
		usage()
else:
	usage()