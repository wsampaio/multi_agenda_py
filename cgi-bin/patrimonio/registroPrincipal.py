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


from objetos.patrimonio.Item import Item
from objetos.patrimonio.ItemDAO import ItemDAO

from objetos.patrimonio.Modelo import Modelo
from objetos.patrimonio.ModeloDAO import ModeloDAO

from objetos.patrimonio.Marca import Marca
from objetos.patrimonio.MarcaDAO import MarcaDAO





from objetos.patrimonio.Vendedor import Vendedor
from objetos.patrimonio.VendedorDAO import VendedorDAO








#obj = Registro()
dao = RegistroDAO()

modelo = Modelo()
modeloDAO = ModeloDAO()

marca = Marca()
marcaDAO = MarcaDAO()

item = Item()
itemDAO = ItemDAO()



vendedor = Vendedor()
vendedorDAO = VendedorDAO()







print("Content-type: application/json\n")

saida = """
{
	"registroLista": ["""

i = 0
#lista = tarefaDAO.listaPrincipaisEmAberto()
lista = dao.getLista()

contaLista = len(lista) -1

for obj in lista:


	item = itemDAO.select(obj.getCodItem())
	modelo = modeloDAO.select(item.getCodModelo())
	marca = marcaDAO.select(item.getCodMarca())

	vendedor = vendedorDAO.select(obj.getCodVendedor())

	saida += """
		{}
			"codRegistro": {},
			"registro": "{}",
			"dtAquisicao": "{}",
			"dtDesuso": "{}"
		{}""".format(
			"{",
			obj.getCodRegistro(),
			item.getItem() + " " + modelo.getModelo() + " - " + marca.getMarca(),
			obj.getDtAquisicao(),
			obj.getDtDesuso(),
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

