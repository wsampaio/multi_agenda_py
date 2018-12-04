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

import datetime

"""
CREATE TABLE tiposContasModelos (
	codModelo INTEGER, 
	descricao TEXT, 
	codTipoGasto INTEGER, 
	codCategoria INTEGER
);

"""

class TipoContaModelo:

	__codModelo = 0
	__descricao = ""
	__codTipoGasto = 0
	__codCategoria = 0


	def __init__(self):
		pass

	def povoarObj(self, array):

		self.setCodModelo(array[0])
		self.setDescricao(array[1])
		self.setCodTipoGasto(array[2])
		self.setCodCategoria(array[3])
		
		return self


	def getCodModelo(self):
		return int(self.__codModelo)

	def setCodModelo(self, codModelo):
		try:
			self.__codModelo = int(codModelo)
		except ValueError:
			self.__codModelo = self.getCodModelo()


	def getDescricao(self):
		return str(self.__descricao)

	def setDescricao(self, descricao):
		try:
			self.__descricao = str(descricao)
		except ValueError:
			self.__descricao = self.getDescricao()


	def getCodTipoGasto(self):
		return int(self.__codTipoGasto)

	def setCodTipoGasto(self, codTipoGasto):
		try:
			self.__codTipoGasto = int(codTipoGasto)
		except ValueError:
			self.__codTipoGasto = self.getCodTipoGasto()


	def getCodCategoria(self):
		return int(self.__codCategoria)

	def setCodCategoria(self, codCategoria):
		try:
			self.__codCategoria = int(codCategoria)
		except ValueError:
			self.__codCategoria = self.getCodCategoria()

