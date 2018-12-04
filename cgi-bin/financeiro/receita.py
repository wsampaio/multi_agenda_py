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


codReceita = 0

form = cgi.FieldStorage()



if form:
	codReceita = int(form.getvalue("cod"))


receita = Receita()
receitaDAO = ReceitaDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")

print(
"""
{
	"receita": [""")

receita = receitaDAO.select(codReceita)

print(
"""
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
		{}""".
		format(
			"{",
			receita.getCodReceita(),
			receita.getCodPagador(),
			receita.getCodFavorecido(),
			receita.getDescricao()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			receita.getPadrao(),
			receita.getAcrescimos(),
			receita.getValor(),
			FormatData.mesRefSerial(receita.getMesReferencia()),
			FormatData.para_Data_Serial(receita.getDtCredito()),
			receita.getObs()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
			"}"
		)
	)

print(
"""
	]
}
""")
