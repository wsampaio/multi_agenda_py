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



if form:
	codTipoConta = int(form.getvalue("cod"))


tipoConta = TipoConta()
tipoContaDAO = TipoContaDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")


saida ="""
{
	"tipoConta": ["""

tipoConta = tipoContaDAO.select(codTipoConta)

saida += """
		{}
			"codTipoConta": "{}",
			"tipoConta": "{}",
			"codModelo": "{}",
			"contaDeCredito": "{}",
			"tipoContaAtivo": "{}",
			"codPagador": "{}",
			"dtInicio": "{}",
			"dtFinal": "{}"
		{}""".format(
			"{",
			tipoConta.getCodTipoConta(),
			tipoConta.getTipoConta(),
			tipoConta.getCodModelo(),
			tipoConta.getContaDeCredito(),
			tipoConta.getTipoContaAtivo(),
			tipoConta.getCodPagador(),
			FormatData.para_Data_Serial(tipoConta.getDtInicio()),
			FormatData.para_Data_Serial(tipoConta.getDtFinal()),
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
