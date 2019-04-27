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

#obj = Receita()
dao = ReceitaDAO()

print("Content-type: application/json\n")

saida = """
{
	"receitas": ["""

i = 0
lista = dao.getLista()

contaLista = len(lista) -1

for obj in lista:

	saida += """
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
		{}""".format(
			"{",
			obj.getCodReceita(),
			obj.getCodPagador(),
			obj.getCodFavorecido(),
			obj.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			obj.getPadrao(),
			obj.getAcrescimos(),
			obj.getValor(),
			obj.getMesReferencia(),
			obj.getDtCredito(),
			obj.getObs()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
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

