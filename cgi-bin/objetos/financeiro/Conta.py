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
CREATE TABLE contas (
	codConta INTEGER, 
	codTipoConta INTEGER, 
	descricao TEXT, 
	mesReferencia TEXT, 
	dtVencimento TEXT, 
	codBarras TEXT, 
	valor REAL,
	codContaPagadora INTEGER, 
	codReceitaPagadora INTEGER, 
	codPagador INTEGER, 
	contaPaga BOOLEAN, 
	valorPago REAL, 
	dtPagamento TEXT
);
"""

class Conta:

	__codConta = 0
	__codTipoConta = 0
	__descricao = ""
	__mesReferencia = FormatData.de_JDate("0001-01-01T00:00")
	__dtVencimento = FormatData.de_JDate("0001-01-01T00:00")
	__codBarras = ""
	__valor = 0.0
	__codContaPagadora = 0
	__codReceitaPagadora = 0
	__codPagador = 0
	__contaPaga = False
	__valorPago = 0.0 
	__dtPagamento = FormatData.de_JDate("0001-01-01T00:00")

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodConta(array[0])
		self.setCodTipoConta(array[1])
		self.setDescricao(array[2])
		self.setMesReferencia(FormatData.de_JDate(array[3]))
		self.setDtVencimento(FormatData.de_JDate(array[4]))
		self.setCodBarras(array[5])
		self.setValor(array[6])
		self.setCodContaPagadora(array[7])
		self.setCodReceitaPagadora(array[8])
		self.setCodPagador(array[9])
		self.setContaPaga(True) if array[10] == "true" else ""
		self.setValorPago(array[11])
		self.setDtPagamento(FormatData.de_JDate(array[12]))

		return self


	def getCodConta(self):
		return int(self.__codConta)

	def setCodConta(self, codConta):
		try:
			self.__codConta = int(codConta)
		except ValueError:
			self.__codConta = self.getCodConta()

	def getCodTipoConta(self):
		return int(self.__codTipoConta)

	def setCodTipoConta(self, codTipoConta):
		try:
			self.__codTipoConta = int(codTipoConta)
		except ValueError:
			self.__codTipoConta = self.getCodTipoConta()

	def getDescricao(self):
		return str(self.__descricao)

	def setDescricao(self, descricao):
		try:
			self.__descricao = str(descricao)
		except ValueError:
			self.__descricao = self.getDescricao()

	def getMesReferencia(self):
		return self.__mesReferencia
		#return datetime.datetime.strptime(self.__mesReferencia, "%Y-%m-%dT%H:%M")

	def setMesReferencia(self, mesReferencia):
		if type(mesReferencia) == datetime.datetime:
			self.__mesReferencia = mesReferencia
		else:
			self.__mesReferencia = self.getMesReferencia()

	def getDtVencimento(self):
		return self.__dtVencimento

	def setDtVencimento(self, dtVencimento):
		if type(dtVencimento) == datetime.datetime:
			self.__dtVencimento = dtVencimento
		else:
			self.__dtPagamento = self.getDtVencimento()

	def getCodBarras(self):
		return self.__codBarras

	def setCodBarras(self, codBarras):
		try:
			self.__codBarras = str(codBarras)
		except ValueError:
			self.__codBarras = self.getCodBarras()

	def getValor(self):
		return self.__valor

	def setValor(self, valor):
		try:
			self.__valor = float(valor)
		except ValueError:
			self.__valor = self.getValor()

	def getCodContaPagadora(self):
		return self.__codContaPagadora

	def setCodContaPagadora(self, codContaPagadora):
		try:
			self.__codContaPagadora = int(codContaPagadora)
		except ValueError:
			self.__codContaPagadora = self.getCodContaPagadora()

	def getCodReceitaPagadora(self):
		return self.__codReceitaPagadora

	def setCodReceitaPagadora(self, codReceitaPagadora):
		try:
			self.__codReceitaPagadora = int(codReceitaPagadora)
		except ValueError:
			self.__codReceitaPagadora = self.getCodReceitaPagadora()

	def getCodPagador(self):
		return self.__codPagador

	def setCodPagador(self, codPagador):
		try:
			self.__codPagador = int(codPagador)
		except ValueError:
			self.__codPagador = self.getCodPagador()

	def getContaPaga(self):
		return bool(self.__contaPaga)

	def setContaPaga(self, contaPaga):
		try:
			self.__contaPaga = bool(contaPaga)
		except ValueError:
			self.__contaPaga = self.getContaPaga()

	def getValorPago(self):
		return self.__valorPago

	def setValorPago(self, valorPago):
		try:
			self.__valorPago = float(valorPago)
		except ValueError:
			self.__valorPago = self.getValorPago()

	def getDtPagamento(self):
		return self.__dtPagamento

	def setDtPagamento(self, dtPagamento):
		if type(dtPagamento) == datetime.datetime:
			self.__dtPagamento = dtPagamento
		else:
			self.__dtPagamento = self.getDtPagamento()



