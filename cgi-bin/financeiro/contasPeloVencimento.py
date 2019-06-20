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

from objetos.financeiro.Conta import Conta
from objetos.financeiro.ContaDAO import ContaDAO

from objetos.financeiro.TipoConta import TipoConta
from objetos.financeiro.TipoContaDAO import TipoContaDAO

from objetos.financeiro.Receita import Receita
from objetos.financeiro.ReceitaDAO import ReceitaDAO

from objetos.financeiro.Pagador import Pagador
from objetos.financeiro.PagadorDAO import PagadorDAO

conta = Conta()
contaDAO = ContaDAO()

tipoConta = TipoConta()
tipoContaDAO = TipoContaDAO()

receita = Receita()
receitaDAO = ReceitaDAO()

pagador = Pagador()
pagadorDAO = PagadorDAO()

form = cgi.FieldStorage()

dtRef = "" + \
str(datetime.date.today().year) + "-" + \
("00" + str(datetime.date.today().month))[-2:]

dtInicio = ""
dtFinal = ""


if form:
	if form.getvalue("dtRef") != None:
		dtRef = form.getvalue("dtRef")

	if form.getvalue("dtInicio") != None:
		dtInicio = FormatData.de_JDate(form.getvalue("dtInicio") + "T00:00")
	elif len(dtInicio) == 0 and form.getvalue("dtFinal") != None:
		dtInicio = FormatData.de_JDate(form.getvalue("dtFinal") + "T00:00")

	if form.getvalue("dtFinal") != None:
		dtFinal = FormatData.de_JDate(form.getvalue("dtFinal") + "T00:00")
	elif len(dtFinal) == 0 and form.getvalue("dtInicio") != None:
		dtFinal = dtInicio + datetime.timedelta(days=30)


print("Content-type: application/json\n")

saida = """
{
	"contas": ["""

i = 0


#define qual lista será acessada
if dtInicio != "" or dtFinal != "":
	lista = contaDAO.listaPorPeriodo(dtInicio, dtFinal)
else:
	lista = contaDAO.listaPeloVencimento(dtRef)


contaLista = len(lista) -1

for forConta in lista:

	tipoConta = tipoContaDAO.select(forConta.getCodTipoConta())
	receita = receitaDAO.select(forConta.getCodReceitaPagadora())

	recPagadora = ""
	
	if (receita.getCodReceita() > 0):
		pagador = pagadorDAO.select(receita.getCodPagador())
		
		recPagadora = "" + \
			FormatData.mesRef(receita.getMesReferencia()) + " - " + \
			pagador.getPagador()

	saida += """
		{}
			"codConta": {},
			"tipoConta": "{}",
			"vencimento": "{}",
			"contaPaga": "{}",
			"dtPagamento": "{}",
			"valor": "{}",
			"valorPago": "{}",
			"receitaPagadora": "{}",
			"codContaPagadora": "{}"
		{}""".format(
			"{",
			forConta.getCodConta(),
			tipoConta.getTipoConta(),
			FormatData.dataSimplesMin(forConta.getDtVencimento()),
			forConta.getContaPaga(),
			FormatData.dataSimplesMin(forConta.getDtPagamento()),
			forConta.getValor(),
			forConta.getValorPago(),
			recPagadora,
			forConta.getCodContaPagadora(),
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
.replace("\n", "")
.replace("\t", "")
)
