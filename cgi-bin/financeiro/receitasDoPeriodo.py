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

from objetos.financeiro.Receita import Receita
from objetos.financeiro.ReceitaDAO import ReceitaDAO

from objetos.financeiro.Conta import Conta
from objetos.financeiro.ContaDAO import ContaDAO

from objetos.financeiro.Pagador import Pagador
from objetos.financeiro.PagadorDAO import PagadorDAO

receita = Receita()
receitaDAO = ReceitaDAO()

conta = Conta()
contaDAO = ContaDAO()

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
	"receitasDoPeriodo": ["""

i = 0
lista = receitaDAO.listaPorMesReferencia(dtRef)

contaLista = len(lista) -1

for forReceita in lista:

	#tipoConta = tipoContaDAO.select(forConta.getCodTipoConta())
	#receita = receitaDAO.select(forConta.getCodReceitaPagadora())

	referencia = ""
	
	if (forReceita.getCodReceita() > 0):
		pagador = pagadorDAO.select(forReceita.getCodPagador())
		
		mesRef = \
			FormatData.mesRef(forReceita.getMesReferencia())

		dtCreditoMin = \
			FormatData.dataSimplesMin(forReceita.getDtCredito())

		referencia = "" + \
			FormatData.mesRef(forReceita.getMesReferencia()) + " - " + \
			pagador.getPagador() + \
			"(em: " + FormatData.dataSimplesMin(forReceita.getDtCredito()) + ")"
		
	
	

	saida += """
		{}
			"codReceita": {},
			"mesRef": "{}",
			"dtCreditoMin": "{}",
			"pagador": "{}",
			"valorReceita": {},
			"mediaReceita": {},
			"valorTtlContas": {},
			"valorTtlContasPagas": {}
		{}""".format(
			"{",
			forReceita.getCodReceita(),
			mesRef,
			dtCreditoMin,
			pagador.getPagador(),
			"{0:.2f}".format(forReceita.getValor()),
			receitaDAO.mediaTresUltimas(
				forReceita.getCodPagador(),
				dtRef
			),
			contaDAO.somaPelaReceitaPagadora(forReceita.getCodReceita()),
			contaDAO.somaPagasPelaReceita(forReceita.getCodReceita()),
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
