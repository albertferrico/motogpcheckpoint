#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import IntegrityError
from django.core.management.base import BaseCommand
import requests, threading
from bs4 import *
import feedparser
from noticias.models import Noticia



class Command(BaseCommand):
	# ··························································#
	def handle(self, *args, **options):
	#	def tiempo_repetir():
			srcCode = requests.get("http://as.com/tag/moto_gp/a/",headers={"content-type":"text"})
			#srcCodeMarca = requests.get("http://www.marca.com/motor/motogp.html")
			srcCodeEurosport = requests.get("http://www.eurosport.es/motociclismo/")
			#srcCodeMotorsport = requests.get("http://es.motorsport.com/category/moto-gp/news/")
			srcCodeMCN = requests.get("http://www.motorcyclenews.com/sport/motogp/")
			srcCodeMotociclismoEs = requests.get("http://www.motociclismo.es/mundial-motogp")
			srcCodeMotoblogIt = requests.get("http://www.motoblog.it/categoria/motogp-motomondiale")
			#srcCodeRepubblicaIt = requests.get("http://www.repubblica.it/sport/moto-gp/")
			srcCodeMoto1pro = requests.get("http://www.moto1pro.com/tags/motogp")
			#srcCodeCrashNet = requests.get("http://www.crash.net/motogp/news_archive/1/content/",verify=False)
			srcCodeGpOne = requests.get("http://www.gpone.com/en/category/motogp",headers={"content-type":"text"})
			srcCodeSportEs = requests.get("http://www.sport.es/es/moto-gp/")
			srcCodeMotorionlineIt = requests.get("http://motograndprix.motorionline.com/category/motogp/")
			#las de frances habilitarlas cuando tenga el filtro por idioma
			#srcCodeGPinsideFr = requests.get("http://www.gp-inside.com/motogp")

			# RSS version of getting the news

			#feedAs = feedparser.parse('https://motor.as.com/rss/motor/motociclismo.xml')
			feedMarca = feedparser.parse('http://estaticos.marca.com/rss/motor/motogp.xml')
			#feedEurosport no tiene RSS
			feedMotorsport = feedparser.parse('https://es.motorsport.com/rss/category/moto-gp/news/')
			#MCN tampoco tiene RSS
			#motociclismo.es tampoco tiene buen RSS
			#motoblog.it tampoco tiene RSS
			feedRepubblicaIt = feedparser.parse('http://www.repubblica.it/rss/sport/motogp/rss2.0.xml')
			#moto1pro.com tampoco tiene RSS
			feedCrashNet = feedparser.parse('https://www.crash.net/rss/motogp')
			#gpone.com no tiene RSS
			#sport.es parece que lo tiene vacio
			#motograndprix.motorionline.com no tiene RSS
			feedGPinsideFr = feedparser.parse('http://www.gp-inside.com/news/rss')
			feedMundoDeportivo = feedparser.parse('http://www.mundodeportivo.com/feed/rss/motor/motogp')			
			feedSuperdeporte = feedparser.parse('http://www.superdeporte.es/elementosInt/rss/21')			
			feedAutoRacingPt = feedparser.parse('http://www.autoracing.com.br/corrida/motogp/feed/')
			feedAutosport = feedparser.parse('https://www.autosport.com/rss/feed/motogp')
			feedPaddockGPFr = feedparser.parse('http://www.paddock-gp.com/feed/')
			feedBikeSportNews = feedparser.parse('http://www.bikesportnews.com/feeds/motogp-news')
			feedGazzettaIt = feedparser.parse('https://www.gazzetta.it/rss/motociclismo.xml')

			noticias_links = []
			noticias_enteras ={}
			for i in range(9):
    				noticias_enteras["ENG - " + feedCrashNet.entries[i].title] = str(feedCrashNet.entries[i].link)
				noticias_enteras["ESP - " + feedMarca.entries[i].title] = str(feedMarca.entries[i].link)
				noticias_enteras["ESP - " + feedMotorsport.entries[i].title] = str(feedMotorsport.entries[i].link)
	 			noticias_enteras["IT - " + feedRepubblicaIt.entries[i].title] = str(feedRepubblicaIt.entries[i].link)
				noticias_enteras["ESP - " + feedMundoDeportivo.entries[i].title] = str(feedMundoDeportivo.entries[i].link)
				noticias_enteras["ESP - " + feedSuperdeporte.entries[i].title] = str(feedSuperdeporte.entries[i].link)
				noticias_enteras["PT - " + feedAutoRacingPt.entries[i].title] = str(feedAutoRacingPt.entries[i].link)
				noticias_enteras["FR - " + feedGPinsideFr.entries[i].title] = str(feedGPinsideFr.entries[i].link)
				noticias_enteras["ENG - " + feedAutosport.entries[i].title] = str(feedAutosport.entries[i].link)
				noticias_enteras["FR - " + feedPaddockGPFr.entries[i].title] = str(feedPaddockGPFr.entries[i].link)
				noticias_enteras["ENG - " + feedBikeSportNews.entries[i].title] = str(feedBikeSportNews.entries[i].link)
				noticias_enteras["IT - " + feedGazzettaIt.entries[i].title] = str(feedGazzettaIt.entries[i].link)
			 
			plainText = srcCode.text
			#plainTextMarca = srcCodeMarca.text
			plainTextEurosport = srcCodeEurosport.text
			#plainTextMotorsport = srcCodeMotorsport.text
			plainTextMCN = srcCodeMCN.text
			plainTextMotociclismoEs = srcCodeMotociclismoEs.text
			plainTextMotoblogIt = srcCodeMotoblogIt.text
			#plainTextRepubblicaIt = srcCodeRepubblicaIt.text
			plainTextMoto1pro = srcCodeMoto1pro.text
			#plainTextCrashNet = srcCodeCrashNet.text
			plainTextGpOne = srcCodeGpOne.text
			plainTextSportEs = srcCodeSportEs.text
			plainTextMotorionlineIt = srcCodeMotorionlineIt.text
			#plainTextGPinsideFr = srcCodeGPinsideFr.text

			soup = BeautifulSoup(plainText)
			#soupMarca = BeautifulSoup(plainTextMarca)
			soupEurosport = BeautifulSoup(plainTextEurosport)
			#soupMotorsport = BeautifulSoup(plainTextMotorsport)
			soupMCN = BeautifulSoup(plainTextMCN)
			soupMotociclismoEs = BeautifulSoup(plainTextMotociclismoEs)
			soupMotoblogIt = BeautifulSoup(plainTextMotoblogIt)
			#soupRepubblicaIt = BeautifulSoup(plainTextRepubblicaIt)
			soupMoto1pro = BeautifulSoup(plainTextMoto1pro)
			#soupCrashNet = BeautifulSoup(plainTextCrashNet)
			soupGpOne = BeautifulSoup(plainTextGpOne)
			soupSportEs = BeautifulSoup(plainTextSportEs)
			soupMotorionlineIt = BeautifulSoup(plainTextMotorionlineIt)
			#soupGPinsideFr = BeautifulSoup(plainTextGPinsideFr)


			url_limpias = []
			titulos_limpios = []

			for div in soup.findAll('div', {'class': 'pntc-txt'}, limit=10):
				for each in div.findAll('a'):      #get all elements with 'a' tag
					href = each.get('href')
					#print (href)          #print href
					#print (each.string)   #print the text in tags
					#print (each)          #print whole tag
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append("ESP - " + each.string)

			#for h3 in soupMarca.findAll('h3', {'class': 'mod-title'}, limit=10):
			#	for each in h3.findAll('a'):      #get all elements with 'a' tag
			#		href = each.get('href')
					#print (href)          #print href
					#print (each.string)   #print the text in tags
					#print (each)          #print whole tag
			#		if each.string:
			#			url_limpias.append(href)
			#			titulos_limpios.append("ESP - " + each.string)

			for div in soupEurosport.findAll('div', {'class': 'storylist-container__main-title'}, limit=10):
				for each in div.findAll('a'):      #get all elements with 'a' tag
					href = "http://www.eurosport.es" + each.get('href')
					#print (href)          #print href
					#print (each.string)   #print the text in tags
					#print (each)          #print whole tag
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append("ESP - " + each.string)

                       # for div in soupMotorsport.findAll('div', {'class': 'article'}, limit=10):
                       #         for each in div.findAll('h3'):
                       #                 for each in div.findAll('a'):      #get all elements with 'a' tag
                       #                         href = "http://es.motorsport.com" + each.get('href')
                                                #print (href)          #print href
                                                #print (each.string)   #print the text in tags
                                                #print (each)          #print whole tag
			#			if each.string:
                         #                       	url_limpias.append(href)
                          #                      	titulos_limpios.append("ESP - " + each.string)

			for h3 in soupMCN.findAll('h3', {'class': 'title'}, limit=10):
				for each in h3.findAll('a'):
					href = "http://www.motorcyclenews.com" + each.get('href')
					# print (href)
					# print (each.string)
					# print (each)
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append("ENG - " + each.string)

			for div in soupMotociclismoEs.findAll('div', {'class': 'noticia'}, limit=10):
				for each in div.findAll('h2'):
					for each in div.findAll('a'):
						href = "http://www.motociclismo.es" + each.get('href')
						if each.string:
							url_limpias.append(href)
							titulos_limpios.append("ESP - " + each.string)

			for div in soupMotoblogIt.findAll('div', {'class': 'item-list-post'}, limit=10):
				for each in div.findAll('h2'):
					for each in div.findAll('a'):
						href = each.get('href')
						if each.string:
							url_limpias.append(href)
							titulos_limpios.append("IT - " + each.string)

			#for article in soupRepubblicaIt.findAll('article', limit=10):
			#	for each in article.findAll('h1'):
			#		for each in article.findAll('a'):
			#			href = each.get('href')
			#			if each.string:
			#				url_limpias.append(href)
			#				titulos_limpios.append("IT - " + each.string)

			for div in soupMoto1pro.findAll('div', {'class': 'titulo-01-interiores'}, limit=10):
				for each in div.findAll('h2'):
					for each in div.findAll('a'):
						href = "http://www.moto1pro.com" + each.get('href')
						if each.string:
							url_limpias.append(href)
							titulos_limpios.append("ESP - " + each.string)
			
			#for div in soupCrashNet.findAll('div', {'class': 'views-field-title'}, limit=10):
			#	for each in div.findAll('a'):
			#		href = "https://www.crash.net" + each.get('href')
			#		if each.string:
			#			url_limpias.append(href)
			#			titulos_limpios.append("ENG - " + each.string)

			for h1 in soupGpOne.findAll('h1', {'class': 'title'}, limit=10):
				for each in h1.findAll('a'):
					href = "https://www.gpone.com" + each.get('href')
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append("ENG - " + each.string)

			for h2 in soupSportEs.findAll('h2', {'class': 'title'}, limit=10):
				for each in h2.findAll('a'):
					href = each.get('href')
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append("ESP - " + each.string)

			for h1 in soupMotorionlineIt.findAll('h1', {'class': 'titleArticle'}, limit=10):
				for each in h1.findAll('a'):
					href = each.get('href')
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append("IT - " + each.string)
		
			#for div in soupGPinsideFr.findAll('div', {'class': 'description'}, limit=10):
			#	for each in div.findAll('a', {'class': 'title'}):
			#		href = "http://www.gp-inside.com" + each.get('href')
			#		if each.string:
			#			url_limpias.append(href)
			#			titulos_limpios.append("FR - " + each.string)


			#print (url_limpias)
			#print (titulos_limpios)

			parejas_limpias = list(zip(titulos_limpios,url_limpias))

			#print(parejas_limpias)

			for key, value in noticias_enteras.items():
				try:
					n = Noticia.objects.get(url_noticia=value)
				except Exception as e:
                                	print (str(e))
                                	n = Noticia()
                                	n.titulo = key
                                	n.url_noticia = value
					n.idioma = key.split(" ",1)[0]
					#print n.idioma
                                	n.save()
			
			for pl in parejas_limpias:
				try:
					n = Noticia.objects.get(url_noticia=pl[1])
					#print ("Noticia ya esta creada")
				except Exception as e:
					print (str(e))
					n = Noticia()
					n.titulo = pl[0]
					n.url_noticia = pl[1]
					n.idioma = pl[0].split(" ",1)[0]
					n.save()
					#print ("Guardando noticia %s " % pl[0]) 
					#threading.Timer(1800, tiempo_repetir).start()

		#tiempo_repetir()

			#conn = sqlite3.connect('db.sqlite3')
			#cur = conn.cursor()
			#cur.executemany('insert or replace into noticias_noticia (titulo, url_noticia) values (?,?)',parejas_limpias)
			#conn.commit()
			#conn.close()
