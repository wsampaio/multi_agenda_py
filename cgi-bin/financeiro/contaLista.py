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

from objetos.financeiro.TipoConta import TipoConta
from objetos.financeiro.TipoContaDAO import TipoContaDAO

#obj = Conta()
dao = ContaDAO()

tipoConta = TipoConta()
tipoContaDAO = TipoContaDAO()

print("Content-type: application/json\n")

saida = ""


saida += """
{
	"contas": ["""

i = 0
lista = dao.getLista()

contaLista = len(lista) -1

for obj in lista:

	tipoConta = tipoContaDAO.select(obj.getCodTipoConta())

	saida += """
		{}
			"codConta": {},
			"tipoConta": {}
				"codTipoConta": {},
				"tipoConta": "{}"
			{},
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
			obj.getCodConta(),
			"{",
			tipoConta.getCodTipoConta(),
			tipoConta.getTipoConta(),
			"}",
			obj.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			obj.getMesReferencia(),
			obj.getDtVencimento(),
			obj.getCodBarras()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			obj.getValor(),
			obj.getCodContaPagadora(),
			obj.getCodReceitaPagadora(),
			obj.getCodPagador(),
			obj.getContaPaga(),
			obj.getValorPago(),
			obj.getDtPagamento(),
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

