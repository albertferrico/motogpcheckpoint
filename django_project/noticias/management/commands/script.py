#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import IntegrityError
from django.core.management.base import BaseCommand
import requests, threading
from bs4 import *
from noticias.models import Noticia



class Command(BaseCommand):
	# ··························································#
	def handle(self, *args, **options):
	#	def tiempo_repetir():
			srcCode = requests.get("http://as.com/tag/moto_gp/a/")
			srcCodeMarca = requests.get("http://www.marca.com/motor/motogp.html")
			srcCodeEurosport = requests.get("http://www.eurosport.es/motociclismo/")
			srcCodeMotorsport = requests.get("http://es.motorsport.com/category/moto-gp/news/")
			srcCodeMCN = requests.get("http://www.motorcyclenews.com/sport/motogp/")
			srcCodeMSMagazine = requests.get("http://www.motorsportmagazine.com/motogp")
			srcCodeMotociclismoEs = requests.get("http://www.motociclismo.es/mundial-motogp")
			srcCodeMotoblogIt = requests.get("http://www.motoblog.it/categoria/motogp-motomondiale")
			srcCodeRepubblicaIt = requests.get("http://www.repubblica.it/sport/moto-gp/")
			srcCodeMoto1pro = requests.get("http://www.moto1pro.com/tags/motogp")
			
			plainText = srcCode.text
			plainTextMarca = srcCodeMarca.text
			plainTextEurosport = srcCodeEurosport.text
			plainTextMotorsport = srcCodeMotorsport.text
			plainTextMCN = srcCodeMCN.text
			plainTextMSMagazine = srcCodeMSMagazine.text
			plainTextMotociclismoEs = srcCodeMotociclismoEs.text
			plainTextMotoblogIt = srcCodeMotoblogIt.text
			plainTextRepubblicaIt = srcCodeRepubblicaIt.text
			plainTextMoto1pro = srcCodeMoto1pro.text

			soup = BeautifulSoup(plainText)
			soupMarca = BeautifulSoup(plainTextMarca)
			soupEurosport = BeautifulSoup(plainTextEurosport)
			soupMotorsport = BeautifulSoup(plainTextMotorsport)
			soupMCN = BeautifulSoup(plainTextMCN)
			soupMSMagazine = BeautifulSoup(plainTextMSMagazine)
			soupMotociclismoEs = BeautifulSoup(plainTextMotociclismoEs)
			soupMotoblogIt = BeautifulSoup(plainTextMotoblogIt)
			soupRepubblicaIt = BeautifulSoup(plainTextRepubblicaIt)
			soupMoto1pro = BeautifulSoup(plainTextMoto1pro)


			url_limpias = []
			titulos_limpios = []

			for div in soup.findAll('div', {'class': 'pntc-txt'}, limit=10):
				for each in div.findAll('a'):      #get all elements with 'a' tag
					href = "http:" + each.get('href')
					#print (href)          #print href
					#print (each.string)   #print the text in tags
					#print (each)          #print whole tag
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append(each.string)

			for h3 in soupMarca.findAll('h3', {'class': 'mod-title'}, limit=10):
				for each in h3.findAll('a'):      #get all elements with 'a' tag
					href = each.get('href')
					#print (href)          #print href
					#print (each.string)   #print the text in tags
					#print (each)          #print whole tag
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append(each.string)

			for div in soupEurosport.findAll('div', {'class': 'storylist-container__main-title'}, limit=10):
				for each in div.findAll('a'):      #get all elements with 'a' tag
					href = "http://www.eurosport.es" + each.get('href')
					#print (href)          #print href
					#print (each.string)   #print the text in tags
					#print (each)          #print whole tag
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append(each.string)

                        for div in soupMotorsport.findAll('div', {'class': 'article'}, limit=10):
                                for each in div.findAll('h3'):
                                        for each in div.findAll('a'):      #get all elements with 'a' tag
                                                href = "http://es.motorsport.com" + each.get('href')
                                                #print (href)          #print href
                                                #print (each.string)   #print the text in tags
                                                #print (each)          #print whole tag
						if each.string:
                                                	url_limpias.append(href)
                                                	titulos_limpios.append(each.string)

			for h3 in soupMCN.findAll('h3', {'class': 'title'}, limit=10):
				for each in h3.findAll('a'):
					href = "http://www.motorcyclenews.com" + each.get('href')
					# print (href)
					# print (each.string)
					# print (each)
					if each.string:
						url_limpias.append(href)
						titulos_limpios.append(each.string)

			for div in soupMSMagazine.findAll('div', {'class': 'teaser'}, limit=10):
				for each in div.findAll('div', {'class': 'content_container'}):
                                	for each in div.findAll('a'):      #get all elements with 'a' tag
                                        	href = "http://www.motorsportmagazine.com/motogp" + each.get('href')
                                        	#print (href)          #print href
                                        	#print (each.string)   #print the text in tags
                                        	#print (each)          #print whole tag
                                        	if each.string:
                                                	url_limpias.append(href)
                                                	titulos_limpios.append(each.string)

			for div in soupMotociclismoEs.findAll('div', {'class': 'noticia'}, limit=10):
				for each in div.findAll('h2'):
					for each in div.findAll('a'):
						href = "http://www.motociclismo.es" + each.get('href')
						if each.string:
							url_limpias.append(href)
							titulos_limpios.append(each.string)

			for div in soupMotoblogIt.findAll('div', {'class': 'item-list-post'}, limit=10):
				for each in div.findAll('h2'):
					for each in div.findAll('a'):
						href = each.get('href')
						if each.string:
							url_limpias.append(href)
							titulos_limpios.append(each.string)

			for article in soupRepubblicaIt.findAll('article', limit=10):
				for each in article.findAll('h1'):
					for each in article.findAll('a'):
						href = each.get('href')
						if each.string:
							url_limpias.append(href)
							titulos_limpios.append(each.string)

			for div in soupMoto1pro.findAll('div', {'class': 'titulo-01-interiores'}, limit=10):
				for each in div.findAll('h2'):
					for each in div.findAll('a'):
						href = "http://www.moto1pro.com/" + each.get('href')
						if each.string:
							url_limpias.append(href)
							titulos_limpios.append(each.string)


			#print (url_limpias)
			#print (titulos_limpios)

			parejas_limpias = list(zip(titulos_limpios,url_limpias))

			#print(parejas_limpias)
			
			for pl in parejas_limpias:
				try:
					n = Noticia.objects.get(url_noticia=pl[1])
					#print ("Noticia ya esta creada")
				except Exception as e:
					print (str(e))
					n = Noticia()
					n.titulo = pl[0]
					n.url_noticia = pl[1]
					n.save()
					#print ("Guardando noticia %s " % pl[0]) 
					#threading.Timer(1800, tiempo_repetir).start()

		#tiempo_repetir()

			#conn = sqlite3.connect('db.sqlite3')
			#cur = conn.cursor()
			#cur.executemany('insert or replace into noticias_noticia (titulo, url_noticia) values (?,?)',parejas_limpias)
			#conn.commit()
			#conn.close()
