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

from objetos.financeiro.CategoriaConta import CategoriaConta
from objetos.financeiro.CategoriaContaDAO import CategoriaContaDAO


codPk = 0

form = cgi.FieldStorage()

obj = CategoriaConta()
dao = CategoriaContaDAO()


print("Content-type: text/html\n")


if str(form) != "FieldStorage(None, None, '')":
	codPk = int(form.getvalue("codCategoria"))

	if form.getvalue("codCategoria"):
		obj.setCodCategoria(int(form.getvalue("codCategoria")))

	if form.getvalue("categoria"):
		obj.setCategoria(str(form.getvalue("categoria")))



	if codPk > 0:
		if form.getvalue("delete"):
			dao.delete(codPk)
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


#print("Content-type: application/json\n")

#print("form = " + str(form))
#print("codConta = " + str(conta.getCodConta()))
#print("delete = " + str(form.getvalue("delete")))


#print("dtAtualizacao = " + str(registro.getDtAtualizacao()))
#print("dtAtualizacao = " + str(type(registro.getDtAtualizacao())))
#print("contaPaga: " + str(conta.getContaPaga()))







#if form.getvalue("delete"):
#	print("DELETE")
#else:
#	print("não delete")

print("""

Dados Salvos


""")




