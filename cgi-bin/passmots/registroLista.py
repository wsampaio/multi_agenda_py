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

from objetos.passmots.Registro import Registro
from objetos.passmots.RegistroDAO import RegistroDAO

obj = Registro()
dao = RegistroDAO()

print("Content-type: application/json\n")

saida = """
{
	"registros": ["""

i = 0
lista = dao.getLista()

contaLista = len(lista) -1

for forObj in lista:

	saida += """
		{}
			"codRegistro": "{}",
			"codOrigemRegistro": "{}",
			"codTipoCampo": "{}",
			"ordem": "{}",
			"registro": "{}",
			"dtAtualizacao": "{}"
		{}""".format(
			"{",
			forObj.getCodRegistro(),
			forObj.getCodOrigemRegistro(),
			forObj.getCodTipoCampo(),
			forObj.getOrdem(),
			forObj.getRegistro()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			forObj.getDtAtualizacao(),
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
