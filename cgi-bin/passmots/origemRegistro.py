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

from objetos.passmots.OrigemRegistro import OrigemRegistro
from objetos.passmots.OrigemRegistroDAO import OrigemRegistroDAO


codOrigemRegistro = 0

form = cgi.FieldStorage()



if form:
	codOrigemRegistro = int(form.getvalue("cod"))


origemRegistro = OrigemRegistro()
origemRegistroDAO = OrigemRegistroDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")

saida = ""


saida += """
"""
{
	"origemRegistro": [""")

origemRegistro = origemRegistroDAO.select(codOrigemRegistro)



saida+= """
		{}
			"codOrigemRegistro": "{}",
			"origemRegistro": "{}"
		{}""".
		format(
			"{",
			origemRegistro.getCodOrigemRegistro(),
			origemRegistro.getOrigemRegistro()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			"}"
		)
	)


saida+= """
	]
}
""")


print(
	saida
		.replace("\n", "")
		.replace("\t", "")
)