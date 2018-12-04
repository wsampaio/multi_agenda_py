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

from objetos.dbConn.FormatData import FormatData
import datetime

"""
CREATE TABLE receita (
	codReceita INTEGER, 
	codPagador INTEGER, 
	codFavorecido INTEGER, 
	descricao TEXT, 
	padrao REAL, 
	acrescimos REAL, 
	valor REAL, 
	mesReferencia TEXT, 
	dtCredito TEXT, 
	obs TEXT
);

"""

class Receita:

	__codReceita = 0
	__codPagador = 0
	__codFavorecido = 0
	__descricao = ""
	__padrao = 0.0
	__acrescimos = 0.0
	__valor = 0.0
	__mesReferencia = FormatData.de_JDate("0001-01-01T00:00")
	__dtCredito = FormatData.de_JDate("0001-01-01T00:00")
	__obs = ""

	
	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodReceita(array[0])
		self.setCodPagador(array[1])
		self.setCodFavorecido(array[2])
		self.setDescricao(array[3])
		self.setPadrao(array[4])
		self.setAcrescimos(array[5])
		self.setValor(array[6])
		self.setMesReferencia(FormatData.de_JDate(array[7]))
		self.setDtCredito(FormatData.de_JDate(array[8]))
		self.setObs(array[9])

		return self

	def getCodReceita(self):
		return int(self.__codReceita)

	def setCodReceita(self, codReceita):
		try:
			self.__codReceita = int(codReceita)
		except ValueError:
			self.__codReceita = self.getCodReceita()


	def getCodPagador(self):
		return int(self.__codPagador)

	def setCodPagador(self, codPagador):
		try:
			self.__codPagador = int(codPagador)
		except ValueError:
			self.__codPagador = self.getCodPagador()


	def getCodFavorecido(self):
		return int(self.__codFavorecido)
	
	def setCodFavorecido(self, codFavorecido):
		try:
			self.__codFavorecido = int(codFavorecido)
		except ValueError:
			self.__codPagador = self.getCodFavorecido()

	def getDescricao(self):
		return str(self.__descricao)

	def setDescricao(self, descricao):
		try:
			self.__descricao = str(descricao)
		except ValueError:
			self.__descricao = self.getDescricao()
		

	def getPadrao(self):
		return float(self.__padrao)

	def setPadrao(self, padrao):
		try:
			self.__padrao = str(padrao)
		except ValueError:
			self.__padrao = self.getPadrao()


	def getAcrescimos(self):
		return float(self.__acrescimos)

	def setAcrescimos(self, acrescimos):
		try:
			self.__acrescimos = str(acrescimos)
		except ValueError:
			self.__acrescimos = self.getAcrescimos()


	def getValor(self):
		return float(self.__valor)

	def setValor(self, valor):
		try:
			self.__valor = str(valor)
		except ValueError:
			self.__valor = self.getValor()


	def getMesReferencia(self):
		return self.__mesReferencia

	def setMesReferencia(self, mesReferencia):
		if type(mesReferencia) == datetime.datetime:
			self.__mesReferencia = mesReferencia
		else:
			self.__mesReferencia = self.getMesReferencia()


	def getDtCredito(self):
		return self.__dtCredito

	def setDtCredito(self, dtCredito):
		if type(dtCredito) == datetime.datetime:
			self.__dtCredito = dtCredito
		else:
			self.__dtCredito = self.getDtCredito()


	def getObs(self):
		return str(self.__obs)


	def setObs(self, obs):
		try:
			self.__obs = str(obs)
		except ValueError:
			self.__obs = self.getObs()

