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

from objetos.patrimonio.Registro import Registro
from objetos.patrimonio.RegistroDAO import RegistroDAO

#obj = Registro()
dao = RegistroDAO()

print("Content-type: application/json\n")

saida = """
{
	"registroLista": ["""

i = 0
#lista = tarefaDAO.listaPrincipaisEmAberto()
lista = dao.getLista()

contaLista = len(lista) -1

for obj in lista:

	saida += """
		{}
			"codRegistro": {},
			"codItem": {},
			"codVendedor": {},
			"dtAquisicao": "{}",
			"preco": {},
			"garantia": "{}",
			"dtDesuso": "{}",
			"observacoes": "{}"
		{}""".format(
			"{",
			obj.getCodRegistro(),
			obj.getCodItem(),
			obj.getCodVendedor(),
			obj.getDtAquisicao(),
			obj.getPreco(),
			obj.getGarantia(),
			obj.getDtDesuso(),
			obj.getObservacoes()
				.replace("\r", "%r")
				.replace("\n", "%n")
				.replace("\t", "$t")
				.replace("\\", "$b"),
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

