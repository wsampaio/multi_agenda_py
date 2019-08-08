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

import http.server
import socketserver

from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

import cgi

import sys
import os
import socket

current_path = os.getcwd()
current_path += ('/objetos')
current_path = os.path.join(sys.path[0], 'objetos')

#print(current_path)

def abreServidor ():

	PORT = 8000
	server_address = ('', PORT)

	handler = CGIHTTPRequestHandler
	handler.cgi_directories = ['/cgi-bin']

	try:
		print("\nHostname:") 
		print(socket.gethostname() + "\n")

		print("IP Address:")
		os.system("hostname -I")
		print("\n")

		with HTTPServer(server_address, CGIHTTPRequestHandler) as httpd:
			#httpd.shutdown()
			print('Python %s on %s' % (sys.version, sys.platform))
			print("serving at port", PORT)
			httpd.serve_forever()

	except KeyboardInterrupt:
		httpd.shutdown()


if __name__ == "__main__":
	os.system("clear")
	print("\nmulti_agenda_py.server")
	abreServidor()



