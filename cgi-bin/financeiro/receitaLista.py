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

from objetos.financeiro.Receita import Receita
from objetos.financeiro.ReceitaDAO import ReceitaDAO

receita = Receita()
receitaDAO = ReceitaDAO()

print("Content-type: application/json\n")

print(
"""
{
	"receitas": [""")

i = 0
lista = receitaDAO.getLista()

contaLista = len(lista) -1

for forReceita in lista:

	print(
"""
		{}
			"codReceita": "{}",
			"codPagador": "{}",
			"codFavorecido": "{}",
			"descricao": "{}",
			"padrao": "{}",
			"acrescimos": "{}",
			"valor": "{}",
			"mesReferencia": "{}",
			"dtCredito": "{}",
			"obs": "{}"
		{}""".
		format(
			"{",
			forReceita.getCodReceita(),
			forReceita.getCodPagador(),
			forReceita.getCodFavorecido(),
			forReceita.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			forReceita.getPadrao(),
			forReceita.getAcrescimos(),
			forReceita.getValor(),
			forReceita.getMesReferencia(),
			forReceita.getDtCredito(),
			forReceita.getObs()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
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
