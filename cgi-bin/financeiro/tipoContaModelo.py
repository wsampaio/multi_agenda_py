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
import cgi
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.financeiro.TipoContaModelo import TipoContaModelo
from objetos.financeiro.TipoContaModeloDAO import TipoContaModeloDAO

codModelo = 0

form = cgi.FieldStorage()



if form:
	codModelo = int(form.getvalue("cod"))


tipoContaModelo = TipoContaModelo()
tipoContaModeloDAO = TipoContaModeloDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")

print(
"""
{
	"tipoContaModelo": [""")

tipoContaModelo = tipoContaModeloDAO.select(codModelo)

print(
"""
		{}
			"codModelo": "{}",
			"descricao": "{}",
			"codTipoGasto": "{}",
			"codCategoria": "{}"
		{}""".
		format(
			"{",
			tipoContaModelo.getCodModelo(),
			tipoContaModelo.getDescricao(),
			tipoContaModelo.getCodTipoGasto(),
			tipoContaModelo.getCodCategoria(),
			"}"
		)
	)

print(
"""
	]
}
""")
