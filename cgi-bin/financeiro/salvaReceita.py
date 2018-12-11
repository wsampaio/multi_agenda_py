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

from objetos.financeiro.Receita import Receita
from objetos.financeiro.ReceitaDAO import ReceitaDAO


codReceita = 0

form = cgi.FieldStorage()

o = Receita()
dao = ReceitaDAO()







print("Content-type: text/html\n")









if str(form) != "FieldStorage(None, None, '')":
	codReceita = int(form.getvalue("codReceita"))


	if form.getvalue("codReceita"):
		o.setCodReceita(
				int(form.getvalue("codReceita"))
		)

	if form.getvalue("codPagador"):
		o.setCodPagador(
				int(form.getvalue("codPagador"))
		)

	if form.getvalue("codFavorecido"):
		o.setCodFavorecido(
				int(form.getvalue("codFavorecido"))
		)

	if form.getvalue("descricao"):
		o.setDescricao(
				str(form.getvalue("descricao"))
		)

	if form.getvalue("padrao"):
		o.setPadrao(
				float(form.getvalue("padrao"))
		)		

	if form.getvalue("acrescimos"):
		o.setAcrescimos(
				float(form.getvalue("acrescimos"))
		)		

	if form.getvalue("valor"):
		o.setValor(
				float(form.getvalue("valor"))
		)		

	if form.getvalue("mesReferencia"):
		o.setMesReferencia(
			FormatData.de_JDate(form.getvalue("mesReferencia") + "-01T00:00")
		)

	if form.getvalue("dtCredito"):
		o.setDtCredito(
			FormatData.de_JDate(form.getvalue("dtCredito") + "T00:00")
		)

	if form.getvalue("obs"):
		o.setObs(
				str(form.getvalue("obs"))
		)



	if codReceita > 0:
		if form.getvalue("delete"):
			dao.delete(o.getCodReceita())
		else:
			dao.update(o)
	else:
		dao.insert(o)

else:
	#tentando enviar status de erro
	#header("HTTP/1.0 404 Not Found");
	#print "Status: 404 Not Found\r\n"
	#print "Content-Type: text/html\r\n\r\n"
	
	#print "Status: 400 Bad Request\r\n"
	pass


#print("Content-type: application/json\n")

print("form = " + str(form))
#print("codConta = " + str(conta.getCodConta()))
print("delete = " + str(form.getvalue("delete")))


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




