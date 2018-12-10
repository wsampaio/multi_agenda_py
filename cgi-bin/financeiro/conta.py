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



if form:
	codConta = int(form.getvalue("cod"))


conta = Conta()
contaDAO = ContaDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")

saida = ""


saida += """
{
	"conta": ["""

conta = contaDAO.select(codConta)

contaPaga = False

if conta.getContaPaga():
	contaPaga = True


saida+= """
		{}
			"codConta": "{}",
			"codTipoConta": "{}",
			"descricao": "{}",
			"mesReferencia": "{}",
			"dtVencimento": "{}",
			"codBarras": "{}",
			"valor": "{}",
			"codReceitaPagadora": "{}",
			"codPagador": "{}",
			"contaPaga": "{}",
			"valorPago": "{}",
			"dtPagamento": "{}"
		{}""".format(
			"{",
			conta.getCodConta(),
			conta.getCodTipoConta(),
			conta.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			FormatData.mesRefSerial(conta.getMesReferencia()),
			FormatData.para_Data_Serial(conta.getDtVencimento()),
			conta.getCodBarras(),
			conta.getValor(),
			conta.getCodReceitaPagadora(),
			conta.getCodPagador(),
			contaPaga,
			conta.getValorPago(),
			FormatData.para_Data_Serial(conta.getDtPagamento()),
			"}"
		)

saida += """
	]
}
"""

print(
	saida
		.replace("\n", "")
		.replace("\t", "")
)
