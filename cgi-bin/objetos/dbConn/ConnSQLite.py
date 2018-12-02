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

import sqlite3
import subprocess
import os.path

class ConnSQLite:
	__conn = None
	__cursor = None
	__schema = None
	__tabela = None
	__pk = None
	
	
	def __init__(sqlite3):
		pass

	def getConn(self, schema):
		
		#url = "../DB/" + schema + ".db"
		url = "DB-multi_agenda/" + schema + ".db"


		self.__conn = sqlite3.connect(url)
		self.__cursor = self.__conn.cursor()
		return self.__conn.cursor
	
	def getConn(self, schema, tabela, pk):
		
		self.__schema = schema
		self.__tabela = tabela
		self.__pk = pk
				
		#para verificar arquivos no Termux
		fTest = "../storage/downloads/DB-multi_agenda/financeiro.db"

		if os.path.isfile(fTest):
			 url = "../storage/downloads/DB-multi_agenda/" + self.__schema + ".db"
		else:
			 url = "../../DB-multi_agenda/" + self.__schema + ".db"

		self.__conn = sqlite3.connect(url)
		self.__cursor = self.__conn.cursor()
		return self.__conn.cursor

	def autoNumeracao(self):
		sql = """
			SELECT
					""" + self.__pk + """
				FROM 
					""" + self.__tabela + """
				ORDER BY
					""" + self.__pk + """ DESC
				LIMIT 1
			;
		"""

		num = 0		
		
		self.__cursor.execute(sql)
		
		for array in self.__cursor.fetchall():
			num = array[0]
		return num + 1


	
	def connect(self, url):
		return self.__conn.connect(url)

	def cursor(__cursor):
		return __cursor
	
	def execute(self, sql, context):
		self.__cursor.execute(sql, context)
		self.__conn.commit()
		return 0
	
	def executeList(self, sql):
		return self.__cursor.execute(sql)
	
	def fetchall(self):
		return self.__cursor.fetchall()
	
	def fetchone(self):
		return self.__cursor.fetchone()
	
	def closeDB(self):
		print(self.__conn)
		

