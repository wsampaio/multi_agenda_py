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

from objetos.tarefas.Prioridade import Prioridade
from objetos.tarefas.PrioridadeDAO import PrioridadeDAO


codPrioridade = 0

form = cgi.FieldStorage()



if form:
	codPrioridade = int(form.getvalue("cod"))



prioridade = Prioridade()
prioridadeDAO = PrioridadeDAO()

print("Content-type: application/json\n")

saida = """
{
	"prioridade": ["""

prioridade = prioridadeDAO.select(codPrioridade)


saida += """
		{}
			"codPrioridade": "{}",
			"ordem": "{}",
			"prioridade": "{}",
			"descricao": "{}"
		{}""".format(
			"{",
			prioridade.getCodPrioridade(),
			prioridade.getOrdem(),
			prioridade.getPrioridade()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			prioridade.getDescricao()
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

