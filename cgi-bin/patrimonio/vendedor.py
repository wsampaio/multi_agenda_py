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

from objetos.patrimonio.Vendedor import Vendedor
from objetos.patrimonio.VendedorDAO import VendedorDAO


codPK = 0

form = cgi.FieldStorage()



if form:
	codPK = int(form.getvalue("cod"))


obj = Vendedor()
dao = VendedorDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")


saida ="""
{
	"vendedor": ["""

obj = dao.select(codPK)

saida += """
		{}
			"codVendedor": {},
			"vendedor": "{}",
			"endereco": "{}",
			"contato": "{}",
			"obs": "{}"
		{}""".format(
			"{",
			obj.getCodVendedor(),
			obj.getVendedor()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			obj.getEndereco()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			obj.getContato()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			obj.getObs()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
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
