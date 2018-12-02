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

from objetos.passmots.Registro import Registro
from objetos.passmots.RegistroDAO import RegistroDAO


codRegistro = 0

form = cgi.FieldStorage()

registro = Registro()
registroDAO = RegistroDAO()


if str(form) != "FieldStorage(None, None, '')":
    codRegistro = int(form.getvalue("codRegistro"))

    registro.setCodRegistro(form.getvalue("codRegistro"))
    registro.setCodOrigemRegistro(form.getvalue("codOrigemRegistro"))
    registro.setCodTipoCampo(form.getvalue("codTipoCampo"))
    registro.setOrdem(form.getvalue("ordem"))
    registro.setRegistro(form.getvalue("registro"))
    registro.setDtAtualizacao(form.getvalue("dtAtualizacao"))

    if codRegistro > 0:
        if form.getvalue("delete"):
            registroDAO.delete(registro.getCodRegistro())
        else:
            registroDAO.update(registro)
    else:
        registroDAO.insert(registro)

else:
    #tentando enviar status de erro
    #header("HTTP/1.0 404 Not Found");
    #print "Status: 404 Not Found\r\n"
    #print "Content-Type: text/html\r\n\r\n"
    
    #print "Status: 400 Bad Request\r\n"
    pass


print("Content-type: text/html\n")
#print("Content-type: application/json\n")

#print("form = " + str(form))
#print("codRegistro = " + str(registro.getCodRegistro()))

#print("dtAtualizacao = " + str(registro.getDtAtualizacao()))
#print("dtAtualizacao = " + str(type(registro.getDtAtualizacao())))








#if form.getvalue("delete"):
#    print("DELETE")
#else:
#    print("não delete")

print("""

Dados Salvos


""")




