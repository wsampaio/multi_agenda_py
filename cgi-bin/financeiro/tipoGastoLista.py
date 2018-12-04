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

from objetos.financeiro.TipoGasto import TipoGasto
from objetos.financeiro.TipoGastoDAO import TipoGastoDAO

tipoGasto = TipoGasto()
tipoGastoDAO = TipoGastoDAO()

print("Content-type: application/json\n")

print(
"""
{
	"tiposGastos": [""")

i = 0
lista = tipoGastoDAO.getLista()

contaLista = len(lista) -1

for forTipoGasto in lista:

	print(
"""
		{}
			"codTipoGasto": "{}",
			"tipoGasto": "{}",
			"descricao": "{}"
		{}""".
		format(
			"{",
			forTipoGasto.getCodTipoGasto(),
			forTipoGasto.getTipoGasto(),
			forTipoGasto.getDescricao()
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
