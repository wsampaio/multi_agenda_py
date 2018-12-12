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

conta = Conta()
contaDAO = ContaDAO()


print("Content-type: text/html\n")


if str(form) != "FieldStorage(None, None, '')":
	codConta = int(form.getvalue("codConta"))

	if form.getvalue("codConta"):
		conta.setCodConta(int(form.getvalue("codConta")))

	if form.getvalue("codTipoConta"):
		conta.setCodTipoConta(int(form.getvalue("codTipoConta")))

	if form.getvalue("descricao"):
		conta.setDescricao(str(form.getvalue("descricao")))
	
	if form.getvalue("mesReferencia"):
		conta.setMesReferencia(
			FormatData.de_JDate(form.getvalue("mesReferencia") + "-01T00:00")
		)

	if form.getvalue("dtVencimento"):
		conta.setDtVencimento(
			FormatData.de_JDate(form.getvalue("dtVencimento") + "T00:00")
		)
	
	if form.getvalue("codBarras"):
		conta.setCodBarras(str(form.getvalue("codBarras")))

	if form.getvalue("valor"):
		conta.setValor(float(form.getvalue("valor")))

	if form.getvalue("codReceitaPagadora"):
		conta.setCodReceitaPagadora(int(form.getvalue("codReceitaPagadora")))

	if form.getvalue("codPagador"):
		conta.setCodPagador(int(form.getvalue("codPagador")))
	
	if form.getvalue("contaPaga"):
		conta.setContaPaga(True)
	else:
		conta.setContaPaga(False)
	
	if form.getvalue("valorPago"):
		conta.setValorPago(float(form.getvalue("valorPago")))
	
	if form.getvalue("dtPagamento"):
		conta.setDtPagamento(
			FormatData.de_JDate(form.getvalue("dtPagamento") + "T00:00")
		)


	if codConta > 0:
		if form.getvalue("delete"):
			contaDAO.delete(conta.getCodConta())
		else:
			contaDAO.update(conta)
	else:
		contaDAO.insert(conta)

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




