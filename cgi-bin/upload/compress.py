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

import objetos.dbConn.BackupMonitor as bkMonitor

form = cgi.FieldStorage()

#print("Content-type:text/html\r\n\r\n")
print("Content-type:text/text\r\n\r\n")

if "com" in str(form):
	bkMonitor.criaBKP()

if "del" in str(form):
	bkMonitor.removeArquivo(form.getvalue("file"))

if "dec" in str(form):
	bkMonitor.extract(form.getvalue("file"))

if "info" in str(form):
	bkMonitor.fileInfo(form.getvalue("file"))


