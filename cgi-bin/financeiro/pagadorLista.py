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

from objetos.financeiro.Pagador import Pagador
from objetos.financeiro.PagadorDAO import PagadorDAO

#obj = Pagador()
dao = PagadorDAO()

print("Content-type: application/json\n")

saida = """
{
	"pagadores": ["""

i = 0
lista = dao.getLista()

contaLista = len(lista) -1

for obj in lista:

	saida += """
		{}
			"codPagador": "{}",
			"pagador": "{}"
		{}""".format(
			"{",
			obj.getCodPagador(),
			obj.getPagador(),
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

