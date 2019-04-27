#!/usr/bin/env python3

#
# Este arquivo é parte do programa multi_agenda
#
# Esta obra está licenciada com uma 
# Licença Creative Commons Atribuição 4.0 Internacional.
# (CC BY 4.0 Internacional)
#  
# Para ver uma cópia da licença, visite
# https://creativecommons.org/licenses/by/4.0/legalcode
# 
# WELLINGTON SAMPAIO - wsampaio@yahoo.com
# https://www.linkedin.com/in/wellsampaio/
#

import sys
import cgi
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.financeiro.Pagador import Pagador
from objetos.financeiro.PagadorDAO import PagadorDAO


codPK = 0

form = cgi.FieldStorage()

obj = Pagador()
dao = PagadorDAO()


if str(form) != "FieldStorage(None, None, '')":
	codPK = int(form.getvalue("codPagador"))


	if form.getvalue("codPagador"):
		obj.setCodPagador(int(form.getvalue("codPagador")))

	if form.getvalue("pagador"):
		obj.setPagador(str(form.getvalue("pagador")))


	if codPK > 0:
		if form.getvalue("delete"):
			dao.delete(codPK)
		else:
			dao.update(obj)
	else:
		dao.insert(obj)

else:
	#tentando enviar status de erro
	#header("HTTP/1.0 404 Not Found");
	#print "Status: 404 Not Found\r\n"
	#print "Content-Type: text/html\r\n\r\n"
	
	#print "Status: 400 Bad Request\r\n"
	pass


#print("Content-type: text/html\n")
#print("Content-type: application/json\n")

#print("form = " + str(form))
#print("codHistorico = " + str(codHistorico))


if form.getvalue("delete"):
	print("DELETE")
else:
	print("não delete")

print("""

Dados Salvos


""")




