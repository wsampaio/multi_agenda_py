#!/usr/bin/env python3

import sys
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.tarefas.Prioridade import Prioridade
from objetos.tarefas.PrioridadeDAO import PrioridadeDAO

prioridade = Prioridade()
prioridadeDAO = PrioridadeDAO()

print("Content-type: application/json\n")

print(
"""
{
    "prioridades": [""")

i = 0
lista = prioridadeDAO.getLista()

contaLista = len(lista) -1

for forPrioridade in lista:

    print(
"""
        {}
            "codPrioridade": "{}",
            "ordem": "{}",
            "prioridade": "{}",
            "descricao": "{}"
        {}""".
        format(
            "{",
            forPrioridade.getCodPrioridade(),
            forPrioridade.getOrdem(),
            forPrioridade.getPrioridade()
                .replace("\r", "%r")
                .replace("\n", "%n")
                .replace("\t", "$t")
                .replace("\\", "$b")
                .replace("\"", "\\\""),
            forPrioridade.getDescricao()
                .replace("\r", "%r")
                .replace("\n", "%n")
                .replace("\t", "$t")
                .replace("\\", "$b")
                .replace("\"", "\\\""),
            "}"
        )
    )

    if i < contaLista:
        print(",")
        i += 1
    else:
        break

print(
"""
    ]
}
""")
