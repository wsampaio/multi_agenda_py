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

from datetime import datetime
from objetos.dbConn.FormatData import FormatData

from objetos.tarefas.Tarefa import Tarefa
from objetos.tarefas.TarefaDAO import TarefaDAO


codTarefa = 0

form = cgi.FieldStorage()

obj = Tarefa()
dao = TarefaDAO()


#a ideia é:
#pega o codTarefa e carrega
#cria um objeto tarefaCopia e copia tudo, menos as datas

#com o codTarefa faz um for em todas subtarefas
#cria o objeto subtarefasCopia e já vai
#colocando o PK da tarefaCopia


#print("Content-type: text/html\n")


if str(form) != "FieldStorage(None, None, '')":
	codTarefa = int(form.getvalue("cod"))

	tarefa = Tarefa()
	novaTarefa = Tarefa()

	tarefa = dao.select(codTarefa)

	novaTarefa.setTarefa("CÓPIA - " + tarefa.getTarefa())
	novaTarefa.setInicio(datetime.now())

	dao.insert(novaTarefa)

	#TESTE
	#print("codTarefaNova = " + str(novaTarefa.getCodTarefa()))
	#print("<br>")

	listaSubTarefas = dao.subTarefasParaCopiar(tarefa.getCodTarefa())

	for forObj in listaSubTarefas:
		subTarefa = Tarefa()

		subTarefa.setCodTarefaPai(novaTarefa.getCodTarefa())
		subTarefa.setTarefa(forObj.getTarefa())
		subTarefa.setOrdem(forObj.getOrdem())

		dao.insert(subTarefa)

		#TESTE
		#print("codSubTarefa = " + str(forObj.getCodTarefa()))
		#print("<br>")
		#print("codSubTarefaNova = " + str(subTarefa.getCodTarefa()))
		#print("<br>")
		#print("<br>")


else:
	#tentando enviar status de erro
	#header("HTTP/1.0 404 Not Found");
	#print "Status: 404 Not Found\r\n"
	#print "Content-Type: text/html\r\n\r\n"
	
	#print "Status: 400 Bad Request\r\n"
	pass


#print("Content-type: text/html\n")
#print("Content-type: application/json\n")

#print("form = " + str(form))
#print("codHistorico = " + str(codHistorico))


if form.getvalue("delete"):
	print("DELETE")
else:
	print("não delete")

print("""

Dados Salvos


""")



