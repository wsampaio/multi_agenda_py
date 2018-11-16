#!/usr/bin/env python3.6

import sys
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.tarefas.Historico import Historico
from objetos.tarefas.HistoricoDAO import HistoricoDAO

historico = Historico()
historicoDAO = HistoricoDAO()

print("Content-type: application/json\n")


print(
"""
{
    "historicos": [""")

i = 0
lista = historicoDAO.getLista()

contaLista = len(lista) -1

for forHistorico in lista:

    print(
"""
        {}
            "codHistorico": "{}",
            "codTarefa": "{}",
            "data": "{}",
            "obs": "{}"
        {}""".
        format(
            "{",
            forHistorico.getCodHistorico(),
            forHistorico.getCodTarefa(),
            forHistorico.getData(),
            forHistorico.getObs()
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
