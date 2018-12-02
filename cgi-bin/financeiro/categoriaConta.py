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

from objetos.financeiro.CategoriaConta import CategoriaConta
from objetos.financeiro.CategoriaContaDAO import CategoriaContaDAO


codCategoria = 0

form = cgi.FieldStorage()



if form:
    codCategoria = int(form.getvalue("cod"))


categoriaConta = CategoriaConta()
categoriaContaDAO = CategoriaContaDAO()

print("Content-type: application/json\n")
#print("Content-type: text/html\n")

print(
"""
{
    "categoriaConta": [""")

categoriaConta = categoriaContaDAO.select(codCategoria)



print(
"""
        {}
            "codCategoria": "{}",
            "categoria": "{}"
        {}""".
        format(
            "{",
            categoriaConta.getCodCategoria(),
            categoriaConta.getCategoria()
                .replace("\r", "%r")
                .replace("\n", "%n")
                .replace("\t", "$t")
                .replace("\\", "$b")
                .replace("\"", "\\\""),
            "}"
        )
    )


print(
"""
    ]
}
""")
