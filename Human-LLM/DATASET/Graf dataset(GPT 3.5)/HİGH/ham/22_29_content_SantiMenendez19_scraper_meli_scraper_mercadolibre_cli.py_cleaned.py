from bs4 import BeautifulSoup
import requests
import os
import sys
import threading
import argparse
import csv
import json
from datetime import datetime
import logging
def fonk1(b22, b21):
	logging.basicConfig(b1 = logging.DEBUG, b32=b22, filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
	b2 = logging.getLogger("INFO")
	b2.setLevel(logging.INFO)
	b3 = logging.FileHandler(b21, "w")
	b4 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	b3.setFormatter(b4)
	b2.addHandler(b3)
	return b2
def fonk2(product_soup):
	b5 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	b6 = {
		"fecha_hora" : b5,
		"producto": "",
		"precio": "",
		"moneda" : "ARS",
		"url_producto": "",
		"url_img_producto" : "",
		"b11": "",
		"id_publicacion": "",
		"estado": "",
		"vendidos": ""
	}
	b7 = product_soup.find('h2','ui-search-item__title').string
	b6["producto"] = "\"" + b7 + "\""
	b8 = product_soup.find("a", "ui-search-link").get("href")
	b6["url_producto"] = b8
	b2.info(f"Scrapeando producto actual de la pagina {b8}")
	b9 = product_soup.find('img','ui-search-result-image__element')
	b6["url_img_producto"] = b9.get('data-src')
	b10 = BeautifulSoup(requests.get(b8).text,'html.b17')
	try:
		b11 = b10.find('span','ui-pdp-review__amount').string
		b11 = b11.replace("(", "")
		b11 = b11.replace(")", "")
		b6["b11"] = b11
	except:
		b6["b11"] = "0"
	try:
		b12 = b10.findAll('span','ui-pdp-color--BLACK ui-pdp-family--SEMIBOLD')[-1].string
		b12 = b12.replace("
		b12 = b12.strip()
		b6["id_publicacion"] = b12
	except:
		pass
	try:
		b13 = b10.find("span", "ui-pdp-subtitle").string.split("|")
		b14 = b13[0].strip()
		if len(b13) == 2:
			b15 = b13[1].replace("vendido", "").replace("s", "").strip()
		else:
			b15 = "0"
		b6["estado"] = b14
		b6["vendidos"] = b15
	except:
		pass
	try:
		b16 = b10.find('span','andes-money-amount__fraction').string.replace(".", "")
		b6["precio"] = b16
	except:
		b2.info("No se logro encontrar el precio, se dejara en -")
		b6["precio"] = "-"
	b25.append(b6)
b5 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
b17 = argparse.ArgumentParser()
b17.add_argument("--busqueda", b18 = "Producto a buscar en ML")
b17.add_argument("--paginas", b18 = "Cantidad de paginas a buscar (Default: 1)")
b19 = b17.parse_args()
if b19.busqueda:
	b20 = b19.busqueda.replace(" ", "-")
else:
	print("Error: No se ingreso un producto a buscar")
	sys.exit(1)
b21 = os.path.join("log", "busqueda_" + b20 + "_ml_INFO_" + b5.split(" ")[0] + ".log")
b22 = os.path.join("log", "busqueda_" + b20 + "_ml_DEBUG_" + b5.split(" ")[0] + ".log")
b2 = fonk1(b22, b21)
if b19.paginas:
	try:
		b23 = int(b19.paginas)
	except BaseException as err:
		b2.error("Error en la cantidad de paginas, el parametro ingresado no es un numero o es negativo")
		print("Error: el parametro ingresado no es un numero")
		sys.exit(1)
	if b23 < 1:
		b2.error("Error en la cantidad de paginas, el parametro ingresado no es un numero o es negativo")
		print("Error: Las paginas no pueden ser menor a 1")
		sys.exit(1)
	else:
		print(f"Se ingresaron {b23} paginas")
else:
	print(f"No se ingreso cantidad de paginas, por defecto sera 1")
	b23 = 1
b24 = "https:
b24 += b20 + "_OrderId_PRICE"
b2.info(f"Inicio del scraping en mercadolibre al producto {b20}")
print("Url: ", b24)
b25 = []
for i in range(0, b23):
	try:
		b26 = requests.get(b24)
	except requests.RequestException as err:
		b2.error(f"Error al intentar buscar la siguiente pagina({i}), la pagina no responde a la peticion")
		print("Error al realizar la peticion de la pagina, posiblemente esta caida o no exista " + err)
		sys.exit(1)
	try:
		b27 = BeautifulSoup(b26.text,'html.b17')
		b28 = b27.title.string
		print (b28 + " | Pagina " + str(i+1))
	except Exception as err:
		print(err)
	b29 = []
	for product_soup in b27.find_all('li','ui-search-layout__item'):
		b30 = threading.Thread(target=scraping_product_details, b19=(product_soup,))
		b29.append(b30)
		b30.start()
	for thread in b29:
		thread.join()
	try:
		if i < b23 - 1:
			b31 = (b27.find('li','andes-pagination__button andes-pagination__button--next')).find('a','andes-pagination__link')
			b24 = b31.get('href')
			b2.info(f"Se ira a la siguiente pagina del producto {b24}")
	except Exception as err:
		b2.error(f"Error al encontrar el siguiente link. " + str(err))
		print("Error al encontrar el siguiente link, se terminaron las paginas")
		print(err)
		if len(b25) == 0:
			print("No se encontraron productos")
			sys.exit(1)
		break
b2.info(f"Se guardaran los productos encontrados en el archivo " + os.path.join("output", "busqueda_" + b20 + "_ml_" + b5.split(" ")[0] + ".csv"))
b32 = open(os.path.join("output", "busqueda_" + b20 + "_ml_" + b5.split(" ")[0] + ".csv"), "w", encoding="utf-8-sig")
b32.write("fecha_hora|producto|precio|moneda|url_producto|url_img_producto|b11|id_publicacion|estado|vendidos\n")
for product in b25:
	b32.write(product["fecha_hora"] + "|")
	b32.write(product["producto"] + "|")
	b32.write(product["precio"] + "|")
	b32.write(product["moneda"] + "|")
	b32.write(product["url_producto"] + "|")
	b32.write(product["url_img_producto"] + "|")
	b32.write(product["b11"] + "|")
	b32.write(product["id_publicacion"] + "|")
	b32.write(product["estado"] + "|")
	b32.write(product["vendidos"] + "\n")
b32.close()
b2.info(f"El scraping del producto {b20} se ha completado.")
b2.info("Total de productos encontrados: " + str(len(b25)))
print("Total de productos encontrados: ", len(b25))
print("Fin del proceso")
sys.exit(0)