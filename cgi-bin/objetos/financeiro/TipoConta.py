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
CREATE TABLE tiposContas (
	codTipoConta INTEGER, 
	tipoConta TEXT, 
	codModelo INTEGER, 
	contaDeCredito BOOLEAN DEFAULT 0, 
	tipoContaAtivo BOOLEAN DEFAULT 0, 
	codPagador INTEGER, 
	dtInicio TEXT, 
	dtFinal TEXT
);

"""

class TipoConta:

	__codTipoConta = 0
	__tipoConta = ""
	__codModelo = 0
	__contaDeCredito = False
	__tipoContaAtivo = False
	__codPagador = 0
	__dtInicio = FormatData.de_JDate("0001-01-01T00:00")
	__dtFinal = FormatData.de_JDate("0001-01-01T00:00")

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodTipoConta(array[0])
		self.setTipoConta(array[1])
		self.setCodModelo(array[2])
		self.setContaDeCredito(array[3])
		self.setTipoContaAtivo(array[4])
		self.setCodPagador(array[5])
		self.setDtInicio(FormatData.de_JDate(array[6]))
		self.setDtFinal(FormatData.de_JDate(array[7]))

		return self

	def getCodTipoConta(self):
		return int(self.__codTipoConta)

	def setCodTipoConta(self, codTipoConta):
		try:
			self.__codTipoConta = int(codTipoConta)
		except ValueError:
			self.__codTipoConta = self.getCodTipoConta()


	def getTipoConta(self):
		return str(self.__tipoConta)

	def setTipoConta(self, tipoConta):
		try:
			self.__tipoConta = str(tipoConta)
		except ValueError:
			self.__tipoConta = self.getTipoConta()


	def getCodModelo(self):
		return int(self.__codModelo)

	def setCodModelo(self, codModelo):
		try:
			self.__codModelo = int(codModelo)
		except ValueError:
			self.__codModelo = self.getCodModelo()


	def getContaDeCredito(self):
		return bool(self.__contaDeCredito)

	def setContaDeCredito(self, contaDeCredito):
		try:
			self.__contaDeCredito = bool(contaDeCredito)
		except ValueError:
			self.__contaDeCredito = self.getContaDeCredito()


	def getTipoContaAtivo(self):
		return bool(self.__tipoContaAtivo)

	def setTipoContaAtivo(self, tipoContaAtivo):
		try:
			self.__tipoContaAtivo = bool(tipoContaAtivo)
		except ValueError:
			self.__tipoContaAtivo = self.getTipoContaAtivo()


	def getCodPagador(self):
		return int(self.__codPagador)

	def setCodPagador(self, codPagador):
		try:
			self.__codPagador = int(codPagador)
		except ValueError:
			self.__codPagador = self.getCodPagador()


	def getDtInicio(self):
		return self.__dtInicio

	def setDtInicio(self, dtInicio):
		if type(dtInicio) == datetime.datetime:
			self.__dtInicio = dtInicio
		else:
			self.__dtInicio = self.getDtInicio()


	def getDtFinal(self):
		return self.__dtFinal

	def setDtFinal(self, dtFinal):
		if type(dtFinal) == datetime.datetime:
			self.__dtFinal = dtFinal
		else:
			self.__dtFinal = self.getDtFinal()

