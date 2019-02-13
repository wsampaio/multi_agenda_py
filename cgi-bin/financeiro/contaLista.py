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

from objetos.financeiro.Conta import Conta
from objetos.financeiro.ContaDAO import ContaDAO

conta = Conta()
contaDAO = ContaDAO()

print("Content-type: application/json\n")

saida = ""


saida += """
{
	"contas": ["""

i = 0
lista = contaDAO.getLista()

contaLista = len(lista) -1

for forConta in lista:

	saida += """
		{}
			"codConta": {},
			"codTipoConta": {},
			"descricao": "{}",
			"mesReferencia": "{}",
			"dtVencimento": "{}",
			"codBarras": "{}",
			"valor": {},
			"codContaPagadora": {},
			"codReceitaPagadora": {},
			"codPagador": {},
			"contaPaga": "{}",
			"valorPago": {},
			"dtPagamento": "{}"
		{}""".format(
			"{",
			forConta.getCodConta(),
			forConta.getCodTipoConta(),
			forConta.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			forConta.getMesReferencia(),
			forConta.getDtVencimento(),
			forConta.getCodBarras()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			forConta.getValor(),
			forConta.getCodContaPagadora(),
			forConta.getCodReceitaPagadora(),
			forConta.getCodPagador(),
			forConta.getContaPaga(),
			forConta.getValorPago(),
			forConta.getDtPagamento(),
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

