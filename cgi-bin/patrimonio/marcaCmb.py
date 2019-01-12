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

from objetos.patrimonio.Marca import Marca
from objetos.patrimonio.MarcaDAO import MarcaDAO


obj = Marca()
dao = MarcaDAO()


print("Content-type: application/json\n")
#print("Content-type: text/html\n")


saida ="""
{
	"marcaCmb": ["""

i = 0
lista = dao.getMarcaCmb()

contaLista = len(lista) -1

for obj in lista:


	stringLbl = obj.getMarca()

	saida += """
		{}
			"codMarca": {},
			"lbl": "{}"
		{}""".format(
			"{",
			obj.getCodMarca(),
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
