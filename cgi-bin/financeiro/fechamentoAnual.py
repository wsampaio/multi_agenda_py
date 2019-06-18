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


from objetos.financeiro.Receita import Receita
from objetos.financeiro.ReceitaDAO import ReceitaDAO

from objetos.financeiro.Conta import Conta
from objetos.financeiro.ContaDAO import ContaDAO

receita = Receita()
receitaDAO = ReceitaDAO()

conta = Conta()
contaDAO = ContaDAO()

form = cgi.FieldStorage()


ano = "2019"
dtRef = ""

if form:
#	dtRef = form.getvalue("dtRef")
	ano = form.getvalue("anoFechamento")


print("Content-type: application/json\n")

saida = \
"""{
	"fechamentoAnual": ["""

for i in range(1, 13):
	dtRef = ano + "-" + ("0" + str(i))[-2:]
	ttlReceita = receitaDAO.somaMesPelaDataPagamento(dtRef)
	ttlReceitaPrev = receitaDAO.mediaTresUltimosMesesPelaDataCredito(dtRef)
	ttlDespesa = contaDAO.somaPagasNoMesPelaDataCreditoDaReceita(dtRef)
	ttlDespesaPrev = contaDAO.somaPrevisaoDoMesPelaDataCreditoDaReceita(dtRef)

	ttlTotal = "{0:.2f}".format(float(ttlReceita) - float(ttlDespesa))
	ttlTotalPrev = "{0:.2f}".format(
		float(ttlReceitaPrev) - float(ttlDespesaPrev)
	)

	saida += """
		{}
			"dtRef": "{}", 
			"ttlReceita": {}, 
			"ttlReceitaPrev": {}, 
			"ttlDespesa": {}, 
			"ttlDespesaPrev": {}, 
			"ttlTotal": {}, 
			"ttlTotalPrev": {}
		{}""".format(
			"{",
			dtRef,
			ttlReceita,
			ttlReceitaPrev,
			ttlDespesa,
			ttlDespesaPrev,
			ttlTotal,
			ttlTotalPrev,
			"}"
		)

	if i < 12:
		saida += ", "

saida += """
	]
}
"""


print(
saida
	.replace("\n", "")
	.replace("\t", "")
)

