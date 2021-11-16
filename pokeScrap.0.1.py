#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:44:33 2021

@author: mat
"""
import requests
import re
import sys
from bs4 import BeautifulSoup


def PokeScraper(url):
	def paramScrap():
		def singleParamScrap(parameter, paramString):
			if parameter >= 0:
				content = params[parameter]
				splitted_content = content.split("=")
				paramliste.append(splitted_content)
			else:
				content = [paramString,'None']
				paramliste.append(content)


		params = params_ref.split("&")
		paramliste = []
		#https://www.cardmarket.com/fr/Pokemon/Products/Singles/Jungle/Pikachu-V1-JU60?sellerType=0,1&language=1,2&minCondition=3&isSigned=N&isFirstEd=Y&isPlayset=N&isAltered=N
		language = index_containing_substring(params, "language")
		sellerType = index_containing_substring(params, "sellerType")
		minCondition = index_containing_substring(params, "minCondition")
		isSigned = index_containing_substring(params, "isSigned")
		isFirstEd = index_containing_substring(params, "isFirstEd")
		isPlayset = index_containing_substring(params, "isPlayset")
		isAltered = index_containing_substring(params, "isAltered")
		singleParamScrap(language, "language")
		singleParamScrap(sellerType, "sellerType")
		singleParamScrap(minCondition, "minCondition")
		singleParamScrap(isSigned, "isSigned")
		singleParamScrap(isFirstEd, "isFirstEd")
		singleParamScrap(isPlayset, "isPlayset")
		singleParamScrap(isAltered, "isAltered")
		#print(str(paramliste))
		return paramliste
		#print("Params :\nlan={}\nseller={}\nminCond={}\nsign={}\n1ed={}\nPlayset={}\nalter={}".format(langage,sellerType,minCondition,isSigned,isFirstEd,isPlayset,isAltered))

	def index_containing_substring(the_list, substring):
	    for i, s in enumerate(the_list):
	        if substring in s:
	              return i
	    return -1

	splitted_URL = url.split("/")
	#print("Splitted URL : ",splitted_URL)
	langage = splitted_URL[3]
	jeu = splitted_URL[4]
	extension_ref = splitted_URL[7]
	name_ref = splitted_URL[8]
	params_ref = name_ref.split("?")[1]
	name_ref = name_ref.split("?")[0]

	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	name_uncut = soup.find_all("div", class_="flex-grow-1")
	name = re.search('><h1>(.*)<span', str(name_uncut))
	name = name.group(1)
	extension_uncut = soup.find_all("a", class_="mb-2")
	extension = re.search('">(.*)</a',str(extension_uncut))
	extension = extension.group(1)
	prices = soup.find_all("span", class_="font-weight-bold color-primary small text-right text-nowrap")
	price_uncut = prices[0]
	#print(str(price_uncut))
	min_price = re.search('>(.*)<',str(price_uncut)).group(1)
	#print("uncut = ",price_uncut,"\ncut = ",min_price)
	out = [extension, name, min_price]
	#print("extension ref = {}\nname ref = {}\nparam ref = {}\nname = {}\nextension = {}\nmin price = {}".format(extension_ref, name_ref,params_ref,name,extension,min_price))
	paramliste = paramScrap()
	return out+paramliste




if len(sys.argv) == 2:
	pk = PokeScraper(sys.argv[1])
else:
	pk = PokeScraper("https://www.cardmarket.com/fr/Pokemon/Products/Singles/Jungle/Pikachu-V1-JU60?language=2&minCondition=3&isFirstEd=Y")
print(str(pk))	


#PokeScraper("https://www.cardmarket.com/fr/Pokemon/Products/Singles/Jungle/Pikachu-V1-JU60?language=2&minCondition=3&isFirstEd=Y")

