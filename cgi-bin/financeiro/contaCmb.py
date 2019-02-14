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
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.dbConn.FormatData import FormatData

from objetos.financeiro.Conta import Conta
from objetos.financeiro.ContaDAO import ContaDAO

from objetos.financeiro.TipoConta import TipoConta
from objetos.financeiro.TipoContaDAO import TipoContaDAO

conta = Conta()
contaDAO = ContaDAO()

tipoConta = TipoConta()
tipoContaDAO = TipoContaDAO()


print("Content-type: application/json\n")

saida = ""

saida += """
{
	"contas": ["""


i = 0
lista = contaDAO.listaContasDeCredito()

contaLista = len(lista) -1

for forConta in lista:
	tipoConta = tipoContaDAO.select(forConta.getCodTipoConta())

	saida += """
		{}
			"codConta": {},
			"lbl": "{}"
		{}""".format(
			"{",
			forConta.getCodConta(),
			FormatData.dataSimplesMin(forConta.getDtVencimento()) + " - " +
			tipoConta.getTipoConta() + " ref: " +
			FormatData.mesRef(forConta.getMesReferencia()),
			"}"
		)

	if i < contaLista:
		saida += ","
		i += 1
	else:
		break

saida += """
	]
}
"""
print(
saida
	.replace("\n", "")
	.replace("\t", "")
)

