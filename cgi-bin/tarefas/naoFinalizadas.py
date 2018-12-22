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

from objetos.tarefas.Tarefa import Tarefa
from objetos.tarefas.TarefaDAO import TarefaDAO

tarefa = Tarefa()
tarefaDAO = TarefaDAO()

print("Content-type: application/json\n")

saida = """
{
	"naoFinalizadas": ["""

i = 0
#lista = tarefaDAO.listaPrincipaisEmAberto()
lista = tarefaDAO.listaPrincipaisEmAberto()

contaLista = len(lista) -1

for forTarefa in lista:

	saida += """
		{}
			"codTarefa": "{}",
			"codTarefaPai": "{}",
			"tarefa": "{}",
			"inicio": "{}",
			"fim": "{}",
			"prazo": "{}",
			"terminado": "{}",
			"ordem": "{}",
			"codPrioridade": "{}"
		{}""".format(
			"{",
			forTarefa.getCodTarefa(),
			forTarefa.getCodTarefaPai(),
			forTarefa.getTarefa()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			forTarefa.getInicio(),
			forTarefa.getFim(),
			forTarefa.getPrazo(),
			forTarefa.getTerminado(),
			forTarefa.getOrdem(),
			forTarefa.getCodPrioridade(),
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

print(saida
	.replace("\n", "")
	.replace("\t", "")
)
