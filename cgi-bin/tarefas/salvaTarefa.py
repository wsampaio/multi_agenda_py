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


codTarefa = 0

form = cgi.FieldStorage()

obj = Tarefa()
dao = TarefaDAO()


if str(form) != "FieldStorage(None, None, '')":
	codTarefa = int(form.getvalue("codTarefa"))


	if form.getvalue("codTarefa"):
		obj.setCodTarefa(int(form.getvalue("codTarefa")))

	if form.getvalue("codTarefaPai"):
		obj.setCodTarefaPai(int(form.getvalue("codTarefaPai")))

	if form.getvalue("tarefa"):
		obj.setTarefa(str(form.getvalue("tarefa")))

	if form.getvalue("codTarefa"):
		obj.setCodTarefa(int(form.getvalue("codTarefa")))

	if form.getvalue("inicio"):
		obj.setInicio(
			FormatData.de_JDate(form.getvalue("inicio"))
		)

	if form.getvalue("fim"):
		obj.setFim(
			FormatData.de_JDate(form.getvalue("fim"))
		)

	if form.getvalue("prazo"):
		obj.setPrazo(
			FormatData.de_JDate(form.getvalue("prazo"))
		)

	if form.getvalue("contaPaga"):
		obj.setTerminado(True)
	else:
		obj.setTerminado(False)

	if form.getvalue("ordem"):
		obj.setOrdem(int(form.getvalue("ordem")))

	if form.getvalue("codPrioridade"):
		obj.setCodPrioridade(int(form.getvalue("codPrioridade")))





	if codTarefa > 0:
		if form.getvalue("delete"):
			dao.delete(obj.getCodTarefa())
		else:
			dao.update(obj)
	else:
		dao.insert(obj)

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




