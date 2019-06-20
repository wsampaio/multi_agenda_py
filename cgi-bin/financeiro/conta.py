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

from objetos.financeiro.Conta import Conta
from objetos.financeiro.ContaDAO import ContaDAO

from objetos.financeiro.TipoConta import TipoConta
from objetos.financeiro.TipoContaDAO import TipoContaDAO


codPk = 0

form = cgi.FieldStorage()



if form:
	codPk = int(form.getvalue("cod"))


obj = Conta()
dao = ContaDAO()

tipoConta = TipoConta()
tipoContaDAO = TipoContaDAO()


print("Content-type: application/json\n")
#print("Content-type: text/html\n")

saida = ""


saida += """
{
	"conta": ["""

obj = dao.select(codPk)
tipoConta = tipoContaDAO.select(obj.getCodTipoConta())


contaPaga = False
contaDeCredito = False

if obj.getContaPaga():
	contaPaga = True

if tipoConta.getContaDeCredito():
	contaDeCredito = True


saida+= """
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
			"dtPagamento": "{}",
			"contaDeCredito": "{}"
		{}""".format(
			"{",
			obj.getCodConta(),
			obj.getCodTipoConta(),
			obj.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			#FormatData.mesRefSerial(conta.getMesReferencia()),
			#FormatData.para_Data_Serial(conta.getDtVencimento()),
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
			contaPaga,
			obj.getValorPago(),
			#FormatData.para_Data_Serial(conta.getDtPagamento()),
			obj.getDtPagamento(),
			contaDeCredito,
			"}"
		)

saida += """
	]
}
"""

print(
	saida
		.replace("\n", "")
		.replace("\t", "")
)

