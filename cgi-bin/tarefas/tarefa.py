#!/usr/bin/env python3

import sys
import cgi
from os.path import dirname, realpath, sep, pardir

sys.path.append((dirname(realpath(__file__)) + sep + pardir))

import cgitb
cgitb.enable()

from objetos.tarefas.Tarefa import Tarefa
from objetos.tarefas.TarefaDAO import TarefaDAO


codTarefa = 0

form = cgi.FieldStorage()



if form:
    codTarefa = int(form.getvalue("cod"))



tarefa = Tarefa()
tarefaDAO = TarefaDAO()

print("Content-type: application/json\n")

print(
"""
{
    "tarefa": [""")

tarefa = tarefaDAO.select(codTarefa)



print(
"""
        {}
            "codTarefa": "{}",
            "codTarefaPai": "{}",
            "tarefa": "{}",
            "inicio": "{}",
            "fim": "{}",
            "prazo": "{}",
            "terminado": "{}",
            "ordem": "{}",
            "codPrioridade": "{}"
        {}""".
        format(
            "{",
            tarefa.getCodTarefa(),
            tarefa.getCodTarefaPai(),
            tarefa.getTarefa()
                .replace("\r", "%r")
                .replace("\n", "%n")
                .replace("\t", "$t")
                .replace("\\", "$b")
                .replace("\"", "\\\""),
            tarefa.getInicio(),
            tarefa.getFim(),
            tarefa.getPrazo(),
            tarefa.getTerminado(),
            tarefa.getOrdem(),
            tarefa.getCodPrioridade(),
            "}"
        )
    )


print(
"""
    ]
}
""")
