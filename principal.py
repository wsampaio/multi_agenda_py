# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import http.server
import socketserver

from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

import cgi
import objetos.tarefas.Tarefa as Tarefa
import objetos.tarefas.TarefaDAO as TarefaDAO

#import sys

#sys.path.append("..")
import sys
import os

current_path = os.getcwd()
#current_path = current_path.replace('/', '.')
current_path += ('/objetos')
current_path = os.path.join(sys.path[0], 'objetos')
#current_path = sys.path[0]
#current_path = "/home/wsampaio/Documentos/NetBeansProjects/multi_agenda_py"

print(current_path)




#print('Python %s on %s' % (sys.version, sys.platform))
#sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
#sys.path.extend(current_path)
#sys.path.append(current_path)
#sys.path.append('objetos/')

#sys.path.append('/usr/bin/python2.7/dist-packages')

print(sys.path)
#print(sys.modules.keys())
#print(globals().items())


def abreServidor ():

    PORT = 8000
    server_address = ('', PORT)

    handler = CGIHTTPRequestHandler
    handler.cgi_directories = ['/cgi-bin']

    try:
        with HTTPServer(server_address,CGIHTTPRequestHandler) as httpd:
            #httpd.shutdown()
            print('Python %s on %s' % (sys.version, sys.platform))
            print("serving at port", PORT)
            httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.shutdown()


def abreServidor3 ():
    print("VAI CORINTHIANS!")
    tarefa = Tarefa.Tarefa()
    tarefaDAO = TarefaDAO.TarefaDAO()

    #tarefa = tarefaDAO.select(381)


    print(tarefa.getCodTarefa())
    print(tarefa.getTarefa())


    tarefa.setTarefa("MUDEI!!!")
    tarefa.setCodTarefa(0)
    #print(tarefaDAO.insert(tarefa))

    print(tarefa.getTarefa())
    print(tarefa.getTerminado())


if __name__ == "__main__":
    print("Hello World")
    abreServidor()



