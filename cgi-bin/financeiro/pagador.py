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

from objetos.financeiro.Pagador import Pagador
from objetos.financeiro.PagadorDAO import PagadorDAO


codPagador = 0

form = cgi.FieldStorage()



if form:
	codPagador = int(form.getvalue("cod"))


pagador = Pagador()
pagadorDAO = PagadorDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")

print(
"""
{
	"pagador": [""")

pagador = pagadorDAO.select(codPagador)



print(
"""
		{}
			"codPagador": "{}",
			"pagador": "{}"
		{}""".
		format(
			"{",
			pagador.getCodPagador(),
			pagador.getPagador(),
			"}"
		)
	)


print(
"""
	]
}
""")
