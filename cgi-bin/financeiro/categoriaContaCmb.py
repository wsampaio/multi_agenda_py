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

from objetos.financeiro.CategoriaConta import CategoriaConta
from objetos.financeiro.CategoriaContaDAO import CategoriaContaDAO


#categoria = CategoriaConta()
categoriaDAO = CategoriaContaDAO()


print("Content-type: application/json\n")

saida = """
{
	"categoriasContas": ["""

i = 0
lista = categoriaDAO.listaCmb()

contaLista = len(lista) - 1

for forCategoria in lista:

	saida += """
		{}
			"codCategoria": {},
			"lbl": "{}"
		{}""".format(
			"{",
			forCategoria.getCodCategoria(),
			forCategoria.getCategoria(),
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




