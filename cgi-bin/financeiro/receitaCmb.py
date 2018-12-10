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

from objetos.financeiro.Receita import Receita
from objetos.financeiro.ReceitaDAO import ReceitaDAO

from objetos.financeiro.Pagador import Pagador
from objetos.financeiro.PagadorDAO import PagadorDAO

receita = Receita()
receitaDAO = ReceitaDAO()

pagador = Pagador()
pagadorDAO = PagadorDAO()


print("Content-type: application/json\n")

print(
"""
{
	"receitas": [""")

i = 0
lista = receitaDAO.listaCmb()

contaLista = len(lista) -1

for forReceita in lista:
	pagador = pagadorDAO.select(forReceita.getCodPagador())

	print(
"""
		{}
			"codReceita": "{}",
			"lbl": "{}"
		{}""".
		format(
			"{",
			forReceita.getCodReceita(),
			FormatData.mesRef(forReceita.getMesReferencia()) + " em: " +
			FormatData.dataSimples(forReceita.getDtCredito()) + " - " +
			pagador.getPagador(),
			"}"
		)
	)

	if i < contaLista:
		print(",")
		i += 1
	else:
		break

print(
"""
	]
}
""")
