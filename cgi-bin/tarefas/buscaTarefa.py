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
import urllib
from urllib.parse import urlparse
import cgi
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.tarefas.Tarefa import Tarefa
from objetos.tarefas.TarefaDAO import TarefaDAO

obj = Tarefa()
dao = TarefaDAO()

print("Content-type: application/json\n")

form = cgi.FieldStorage()

qry = []

if form:
	uri = urlparse(form.getvalue("qry"))
	qry = uri.path.split(" ")




#print("Content-type: application/json\n")

saida = """
{
	"tarefas": ["""

i = 0
#lista = tarefaDAO.listaPrincipaisEmAberto()
lista = dao.buscaTarefa(qry)

contaLista = len(lista) -1

for forObj in lista:

	saida += """
		{}
			"codTarefa": {},
			"codTarefaPai": {},
			"tarefa": "{}",
			"inicio": "{}",
			"fim": "{}",
			"prazo": "{}",
			"terminado": "{}",
			"ordem": {},
			"codPrioridade": {}
		{}""".format(
			"{",
			forObj.getCodTarefa(),
			forObj.getCodTarefaPai(),
			forObj.getTarefa()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			forObj.getInicio(),
			forObj.getFim(),
			forObj.getPrazo(),
			forObj.getTerminado(),
			forObj.getOrdem(),
			forObj.getCodPrioridade(),
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
