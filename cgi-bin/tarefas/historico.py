#!/usr/bin/env python3.6

import sys
import cgi
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.tarefas.Historico import Historico
from objetos.tarefas.HistoricoDAO import HistoricoDAO


codHistorico = 0

form = cgi.FieldStorage()

if form:
    codHistorico = int(form.getvalue("cod"))



historico = Historico()
historicoDAO = HistoricoDAO()

print("Content-type: application/json\n")

print(
"""
{
    "historico": [""")

historico = historicoDAO.select(codHistorico)



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
            historico.getCodHistorico(),
            historico.getCodTarefa(),
            historico.getData(),
            historico.getObs()
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
