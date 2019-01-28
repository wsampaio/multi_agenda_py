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

from objetos.patrimonio.Vendedor import Vendedor
from objetos.patrimonio.VendedorDAO import VendedorDAO


obj = Vendedor()
dao = VendedorDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")


saida ="""
{
	"vendedorCmb": ["""

i = 0
lista = dao.getVendedorCmb()

contaLista = len(lista) -1

for obj in lista:

	stringLbl = obj.getVendedor()[:15]
	stringLbl += " - " + obj.getEndereco()[:15]
	

	saida += """
		{}
			"codVendedor": {},
			"lbl": "{}"
		{}""".format(
			"{",
			obj.getCodVendedor(),
			stringLbl,
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
