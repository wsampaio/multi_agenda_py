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

from objetos.tarefas.Prioridade import Prioridade
from objetos.tarefas.PrioridadeDAO import PrioridadeDAO

prioridade = Prioridade()
prioridadeDAO = PrioridadeDAO()

print("Content-type: application/json\n")

saida = """
{
	"prioridades": ["""

i = 0
lista = prioridadeDAO.getLista()

contaLista = len(lista) -1

for forPrioridade in lista:

	saida += """
		{}
			"codPrioridade": "{}",
			"ordem": "{}",
			"prioridade": "{}",
			"descricao": "{}"
		{}""".format(
			"{",
			forPrioridade.getCodPrioridade(),
			forPrioridade.getOrdem(),
			forPrioridade.getPrioridade()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			forPrioridade.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			"}"
		)

	if i < contaLista:
		saida += ","
		i += 1
	else:
		break

saida +="""
	]
}
"""

print(
saida
	.replace("\n", "")
	.replace("\t", "")
)



