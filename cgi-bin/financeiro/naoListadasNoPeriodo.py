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
import datetime
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.dbConn.FormatData import FormatData

from objetos.financeiro.TipoConta import TipoConta
from objetos.financeiro.TipoContaDAO import TipoContaDAO

tipoConta = TipoConta()
tipoContaDAO = TipoContaDAO()

form = cgi.FieldStorage()

dtRef = "" + \
str(datetime.date.today().year) + "-" + \
("00" + str(datetime.date.today().month))[-2:]

if form:
	if form.getvalue("dtRef") != None:
		dtRef = form.getvalue("dtRef")




print("Content-type: application/json\n")

saida = """
{
	"contas": ["""

i = 0
lista = tipoContaDAO.naoListadasNoPeriodo(dtRef)

contaLista = len(lista) -1

for forTipoConta in lista:

	saida += """
		{}
			"codTipoConta": {},
			"tipoConta": "{}"
		{}""".format(
			"{",
			forTipoConta.getCodTipoConta(),
			forTipoConta.getTipoConta(),
			"}"
		)
	#)

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
#.replace("\n", "")
#.replace("\t", "")
)


