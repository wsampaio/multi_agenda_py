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

if form:
	if form.getvalue("dtRef") != None:
		dtRef = form.getvalue("dtRef")
	


print("Content-type: application/json\n")

saida = """
{
	"contas": ["""

i = 0
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
			"receitaPagadora": "{}"
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
