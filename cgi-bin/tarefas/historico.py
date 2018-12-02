#!/usr/bin/env python3.6

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
