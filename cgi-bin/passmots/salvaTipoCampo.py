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

from objetos.passmots.TipoCampo import TipoCampo
from objetos.passmots.TipoCampoDAO import TipoCampoDAO


codTipoCampo = 0

form = cgi.FieldStorage()

obj = TipoCampo()
dao = TipoCampoDAO()

print(str(form))

if str(form) != "FieldStorage(None, None, '')":
	codTipoCampo = int(form.getvalue("codTipoCampo"))

	if form.getvalue("codTipoCampo"):
		obj.setCodTipoCampo(int(form.getvalue("codTipoCampo")))

	if form.getvalue("tipoCampo"):
		obj.setTipoCampo(str(form.getvalue("tipoCampo")))

	if form.getvalue("campoDeSenha"):
		obj.setCampoDeSenha(True)
	else:
		obj.setCampoDeSenha(False)


	if codTipoCampo > 0:
		if form.getvalue("delete"):
			dao.delete(obj.getCodTipoCampo())
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




