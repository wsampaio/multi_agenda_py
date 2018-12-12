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

from objetos.dbConn.FormatData import FormatData

from objetos.passmots.Registro import Registro
from objetos.passmots.RegistroDAO import RegistroDAO


codRegistro = 0

form = cgi.FieldStorage()

registro = Registro()
registroDAO = RegistroDAO()


print("Content-type: text/html\n")


if str(form) != "FieldStorage(None, None, '')":
	codRegistro = int(form.getvalue("codRegistro"))


	if form.getvalue("codRegistro"):
		registro.setCodRegistro(int(form.getvalue("codRegistro")))

	if form.getvalue("codOrigemRegistro"):
		registro.setCodOrigemRegistro(int(form.getvalue("codOrigemRegistro")))

	if form.getvalue("codTipoCampo"):
		registro.setCodTipoCampo(int(form.getvalue("codTipoCampo")))

	if form.getvalue("ordem"):
		registro.setOrdem(int(form.getvalue("ordem")))

	if form.getvalue("registro"):
		registro.setRegistro(str(form.getvalue("registro")))

	if form.getvalue("dtAtualizacao"):
		registro.setDtAtualizacao(
			FormatData.de_JDate(form.getvalue("dtAtualizacao"))
		)




	if codRegistro > 0:
		if form.getvalue("delete"):
			registroDAO.delete(registro.getCodRegistro())
		else:
			registroDAO.update(registro)
	else:
		registroDAO.insert(registro)

else:
	#tentando enviar status de erro
	#header("HTTP/1.0 404 Not Found");
	#print "Status: 404 Not Found\r\n"
	#print "Content-Type: text/html\r\n\r\n"
	
	#print "Status: 400 Bad Request\r\n"
	pass



#print("form = " + str(form))
#print("codRegistro = " + str(registro.getCodRegistro()))

#print("dtAtualizacao = " + str(registro.getDtAtualizacao()))
#print("dtAtualizacao = " + str(type(registro.getDtAtualizacao())))








#if form.getvalue("delete"):
#	print("DELETE")
#else:
#	print("não delete")

print("""

Dados Salvos


""")




