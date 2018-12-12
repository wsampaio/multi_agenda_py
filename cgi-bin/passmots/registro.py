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


from objetos.dbConn.FormatData import FormatData

from objetos.passmots.Registro import Registro
from objetos.passmots.RegistroDAO import RegistroDAO


codRegistro = 0

form = cgi.FieldStorage()



if form:
	codRegistro = int(form.getvalue("cod"))


registro = Registro()
registroDAO = RegistroDAO()

print("Content-type: application/json\n")


saida = ""


saida += """
{
	"registro": ["""

registro = registroDAO.select(codRegistro)



saida += """
		{}
			"codRegistro": {},
			"codOrigemRegistro": {},
			"codTipoCampo": {},
			"ordem": {},
			"registro": "{}",
			"dtAtualizacao": "{}"
		{}""".format(
			"{",
			registro.getCodRegistro(),
			registro.getCodOrigemRegistro(),
			registro.getCodTipoCampo(),
			registro.getOrdem(),
			registro.getRegistro()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			FormatData.para_JDate(registro.getDtAtualizacao()),
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
