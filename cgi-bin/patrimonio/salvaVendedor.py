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

from objetos.patrimonio.Vendedor import Vendedor
from objetos.patrimonio.VendedorDAO import VendedorDAO


codPK = 0

form = cgi.FieldStorage()

obj = Vendedor()
dao = VendedorDAO()


if str(form) != "FieldStorage(None, None, '')":
	codPK = int(form.getvalue("codVendedor"))


	if form.getvalue("codVendedor"):
		obj.setCodVendedor(int(form.getvalue("codVendedor")))

	if form.getvalue("vendedor"):
		obj.setVendedor(str(form.getvalue("vendedor")))

	if form.getvalue("endereco"):
		obj.setEndereco(str(form.getvalue("endereco")))

	if form.getvalue("contato"):
		obj.setContato(str(form.getvalue("contato")))

	if form.getvalue("obs"):
		obj.setObs(str(form.getvalue("obs")))





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




