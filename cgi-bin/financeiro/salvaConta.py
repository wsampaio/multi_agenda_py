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

from objetos.financeiro.Conta import Conta
from objetos.financeiro.ContaDAO import ContaDAO


codConta = 0

form = cgi.FieldStorage()

obj = Conta()
dao = ContaDAO()


print("Content-type: text/html\n")


if str(form) != "FieldStorage(None, None, '')":
	codConta = int(form.getvalue("codConta"))

	if form.getvalue("codConta"):
		obj.setCodConta(int(form.getvalue("codConta")))

	if form.getvalue("codTipoConta"):
		obj.setCodTipoConta(int(form.getvalue("codTipoConta")))

	if form.getvalue("descricao"):
		obj.setDescricao(str(form.getvalue("descricao")))
	
	if form.getvalue("mesReferencia"):
		obj.setMesReferencia(
			FormatData.de_JDate(form.getvalue("mesReferencia") + "-01T00:00")
		)

	if form.getvalue("dtVencimento"):
		obj.setDtVencimento(
			FormatData.de_JDate(form.getvalue("dtVencimento") + "T00:00")
		)
	
	if form.getvalue("codBarras"):
		obj.setCodBarras(str(form.getvalue("codBarras")))

	if form.getvalue("valor"):
		obj.setValor(float(form.getvalue("valor")))

	if form.getvalue("codContaPagadora"):
		obj.setCodContaPagadora(int(form.getvalue("codContaPagadora")))

	if form.getvalue("codReceitaPagadora"):
		obj.setCodReceitaPagadora(int(form.getvalue("codReceitaPagadora")))

	if form.getvalue("codPagador"):
		obj.setCodPagador(int(form.getvalue("codPagador")))
	
	if form.getvalue("contaPaga"):
		obj.setContaPaga(True)
	else:
		obj.setContaPaga(False)
	
	if form.getvalue("valorPago"):
		obj.setValorPago(float(form.getvalue("valorPago")))
	
	if form.getvalue("dtPagamento"):
		obj.setDtPagamento(
			FormatData.de_JDate(form.getvalue("dtPagamento") + "T00:00")
		)


	if codConta > 0:
		if form.getvalue("delete"):
			dao.delete(obj.getCodConta())
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




