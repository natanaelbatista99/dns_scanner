import time
inicio = time.time()

import sys
import dns.resolver
import logging
import time
from threading import Thread
import math

global i
global tmpfinal

i = tmpfinal = 0

def test(t, lista):
	global i
	global tmpfinal
	logging.info(lista)
	dominio = 'pudim.com.br'
 
	try:
		arquivo = open(lista)
		linhas = arquivo.read().splitlines()
	except:
		print("Arquivo nao encontrado ou ivalido")
		sys.exit(1)

	for linha in linhas:
		subdominio = linha + '.' + dominio
		try:
			respostas = dns.resolver.query(subdominio, 'a')
			for resultado in respostas:
				print (subdominio, resultado)
		except:
			pass
	i = i + 1
	fim = time.time()
	print ('Time %d: ' % t)
	tmpfinal = max(tmpfinal, (fim-inicio))
	print (round((fim-inicio), 4))

	if(i == 5):
		fim = time.time()
		print ('\nTime Final')
		print (round(tmpfinal, 4))
    	


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

t1 = Thread(target=test, args=(1, 'lt1-100.txt',))
t1.start()

t2 = Thread(target=test, args=(2, 'lt2-100.txt',))
t2.start()

t3 = Thread(target=test, args=(3, 'lt3-100.txt',))
t3.start()

t4 = Thread(target=test, args=(4, 'lt4-100.txt',))
t4.start()

t5 = Thread(target=test, args=(5, 'lt5-100.txt',))
t5.start()
