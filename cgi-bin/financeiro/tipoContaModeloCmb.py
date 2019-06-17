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

from objetos.financeiro.TipoContaModelo import TipoContaModelo
from objetos.financeiro.TipoContaModeloDAO import TipoContaModeloDAO

from objetos.financeiro.TipoGasto import TipoGasto
from objetos.financeiro.TipoGastoDAO import TipoGastoDAO

from objetos.financeiro.CategoriaConta import CategoriaConta
from objetos.financeiro.CategoriaContaDAO import CategoriaContaDAO


tipoContaModelo = TipoContaModelo()
tipoContaModeloDAO = TipoContaModeloDAO()

tipoGasto = TipoGasto()
tipoGastoDAO = TipoGastoDAO()

categoria = CategoriaConta()
categoriaDAO = CategoriaContaDAO()


print("Content-type: application/json\n")

saida = """
{
	"tiposContasModelos": ["""

i = 0
lista = tipoContaModeloDAO.listaCmb()

contaLista = len(lista) - 1

for forModelo in lista:

	tipoGasto = tipoGastoDAO.select(forModelo.getCodTipoGasto())
	categoria = categoriaDAO.select(forModelo.getCodCategoria())

	strLbl = forModelo.getDescricao()

	if (forModelo.getCodCategoria() > 0):
		strLbl += " - " + categoria.getCategoria()

	if (forModelo.getCodTipoGasto() > 0):
		strLbl += "/" + tipoGasto.getTipoGasto()


	saida += """
		{}
			"codModelo": {},
			"lbl": "{}"
		{}""".format(
			"{",
			forModelo.getCodModelo(),
			strLbl,
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




