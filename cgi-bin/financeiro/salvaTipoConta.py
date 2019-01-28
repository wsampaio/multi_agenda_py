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

from objetos.financeiro.TipoConta import TipoConta
from objetos.financeiro.TipoContaDAO import TipoContaDAO


codTipoConta = 0

form = cgi.FieldStorage()

obj = TipoConta()
dao = TipoContaDAO()


print("Content-type: text/html\n")


if str(form) != "FieldStorage(None, None, '')":
	codTipoConta = int(form.getvalue("codTipoConta"))

	if form.getvalue("codTipoConta"):
		obj.setCodTipoConta(int(form.getvalue("codTipoConta")))

	if form.getvalue("tipoConta"):
		obj.setTipoConta(str(form.getvalue("tipoConta")))

	if form.getvalue("codModelo"):
		obj.setCodModelo(int(form.getvalue("codModelo")))

	if form.getvalue("contaDeCredito"):
		obj.setContaDeCredito(True)
	else:
		obj.setContaDeCredito(False)

	if form.getvalue("tipoContaAtivo"):
		obj.setTipoContaAtivo(True)
	else:
		obj.setTipoContaAtivo(False)

	if form.getvalue("codPagador"):
		obj.setCodPagador(int(form.getvalue("codPagador")))

	if form.getvalue("dtInicio"):
		obj.setDtInicio(
			FormatData.de_JDate(form.getvalue("dtInicio") + "T00:00")
		)

	if form.getvalue("dtFinal"):
		obj.setDtFinal(
			FormatData.de_JDate(form.getvalue("dtFinal") + "T00:00")
		)



	if codTipoConta > 0:
		if form.getvalue("delete"):
			dao.delete(obj.getCodTipoConta())
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




