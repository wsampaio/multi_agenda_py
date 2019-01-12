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

from objetos.tarefas.Tarefa import Tarefa
from objetos.tarefas.TarefaDAO import TarefaDAO

codTarefaPai = 0

form = cgi.FieldStorage()

if form:
	codTarefaPai = int(form.getvalue("cod"))


obj = Tarefa()
dao = TarefaDAO()

print("Content-type: application/json\n")

saida = ""

saida += """
{
	"subTarefas": ["""


i = 0
#lista = tarefaDAO.listaPrincipaisEmAberto()
lista = dao.listaSubTarefas(codTarefaPai)
contaLista = len(lista) -1

for obj in lista:

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
			obj.getCodTarefa(),
			obj.getCodTarefaPai(),
			obj.getTarefa()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b")
				.replace("\"", "\\\""),
			FormatData.para_JDate(obj.getInicio()),
			FormatData.para_JDate(obj.getFim()),
			FormatData.para_JDate(obj.getPrazo()),
			obj.getTerminado(),
			obj.getOrdem(),
			obj.getCodPrioridade(),
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

