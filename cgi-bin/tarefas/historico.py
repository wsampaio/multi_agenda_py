#!/usr/bin/env python3.6

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

from objetos.tarefas.Historico import Historico
from objetos.tarefas.HistoricoDAO import HistoricoDAO


codHistorico = 0

form = cgi.FieldStorage()

if form:
	codHistorico = int(form.getvalue("cod"))



obj = Historico()
dao = HistoricoDAO()

print("Content-type: application/json\n")

saida = ""

saida += """
{
	"historico": ["""

obj = dao.select(codHistorico)


saida += """
		{}
			"codHistorico": "{}",
			"codTarefa": "{}",
			"data": "{}",
			"obs": "{}"
		{}""".format(
			"{",
			obj.getCodHistorico(),
			obj.getCodTarefa(),
			FormatData.para_JDate(obj.getData()),
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
