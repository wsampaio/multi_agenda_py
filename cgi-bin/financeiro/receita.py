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
#import objetos.dbConn.FormatData as FormatData

from objetos.financeiro.Receita import Receita
from objetos.financeiro.ReceitaDAO import ReceitaDAO


codPk = 0

form = cgi.FieldStorage()



if form:
	codPk = int(form.getvalue("cod"))


obj = Receita()
dao = ReceitaDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")


saida = """
{
	"receita": ["""

obj = dao.select(codPk)

saida += """
		{}
			"codReceita": "{}",
			"codPagador": "{}",
			"codFavorecido": "{}",
			"descricao": "{}",
			"padrao": "{}",
			"acrescimos": "{}",
			"valor": "{}",
			"mesReferencia": "{}",
			"dtCredito": "{}",
			"obs": "{}"
		{}""".format(
			"{",
			obj.getCodReceita(),
			obj.getCodPagador(),
			obj.getCodFavorecido(),
			obj.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			obj.getPadrao(),
			obj.getAcrescimos(),
			obj.getValor(),
			#FormatData.mesRefSerial(obj.getMesReferencia()),
			#FormatData.para_Data_Serial(obj.getDtCredito()),
			obj.getMesReferencia(),
			obj.getDtCredito(),
			obj.getObs()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
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

