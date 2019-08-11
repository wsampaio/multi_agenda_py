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

from objetos.passmots.OrigemRegistro import OrigemRegistro
from objetos.passmots.OrigemRegistroDAO import OrigemRegistroDAO

from objetos.passmots.Registro import Registro
from objetos.passmots.RegistroDAO import RegistroDAO

from objetos.passmots.TipoCampo import TipoCampo
from objetos.passmots.TipoCampoDAO import TipoCampoDAO

origemRegistro = OrigemRegistro()
origemRegistroDAO = OrigemRegistroDAO()

registro = Registro()
registroDAO = RegistroDAO()

tipoCampo = TipoCampo()
tipoCampoDAO = TipoCampoDAO()

form = cgi.FieldStorage()




codOrigemRegistro = 0


if form:
	codOrigemRegistro = int(form.getvalue("cod"))

if codOrigemRegistro > 0:
	origemRegistro = origemRegistroDAO.select(codOrigemRegistro)






print("Content-type: application/json\n")
#print("Content-type: text/html\n")
saida = ""


saida += """
{
	"codOrigemRegistro": """ + str(origemRegistro.getCodOrigemRegistro()) + """,
	"origemRegistro": \"""" + origemRegistro.getOrigemRegistro() + """\",
	"registros": ["""

tipoCampo = tipoCampoDAO.select(2)


i = 0
lista = registroDAO.getListaPelaOrigem(codOrigemRegistro)

contaLista = len(lista) -1

for forRegistro in lista:
	tipoCampo = tipoCampoDAO.select(forRegistro.getCodTipoCampo())

	saida += """
		{}
			"codTipoCampo": "{}",
			"tipoCampo": "{}",
			"campoDeSenha": "{}",
			"codRegistro": {},
			"registro": "{}",
			"ordem": {}
		{}""".format(
			"{",
			forRegistro.getCodTipoCampo(),
			tipoCampo.getTipoCampo(),
			tipoCampo.getCampoDeSenha(),
			forRegistro.getCodRegistro(),
			forRegistro.getRegistro(),
			forRegistro.getOrdem(),
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

