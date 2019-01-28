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

from objetos.patrimonio.Marca import Marca
from objetos.patrimonio.MarcaDAO import MarcaDAO


codMarca = 0

form = cgi.FieldStorage()



if form:
	codMarca = int(form.getvalue("cod"))


obj = Marca()
dao = MarcaDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")


saida ="""
{
	"marca": ["""

obj = dao.select(codMarca)

saida += """
		{}
			"codMarca": "{}",
			"marca": "{}"
		{}""".format(
			"{",
			obj.getCodMarca(),
			obj.getMarca(),
			"}"
		)

saida += """
	]
}
"""

print(
saida
	.replace("\n", "")
	.replace("\t", "")
)
