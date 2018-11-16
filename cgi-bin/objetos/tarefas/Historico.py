# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from objetos.dbConn.FormatData import FormatData


"""
CREATE TABLE historicos (
codHistorico INTEGER PRIMARY KEY, 
codTarefa INTEGER, 
data LocalDateTime, 
obs TEXT);
"""



class Historico:

	__codHistorico = 0
	__codTarefa = 0
	__data = FormatData.de_JDate("0001-01-01T00:00")
	__obs = ""



	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodHistorico(array[0])
		self.setCodTarefa(array[1])
		self.setData(FormatData.de_JDate(array[2]))
		self.setObs(array[3])
		return self

	def getCodHistorico(self):
		return self.__codHistorico

	def setCodHistorico(self, codHistorico):
		try:
			self.__codHistorico = int(codHistorico)
		except ValueError:
			self.__codHistorico = self.getCodHistorico()

	def getCodTarefa(self):
		return self.__codTarefa

	def setCodTarefa(self, codTarefa):
		try:
			self.__codTarefa = int(codTarefa)
		except ValueError:
			self.__codTarefa = self.getCodTarefa()

	def getData(self):
		#return FormatData.de_JDate(self.__data)
		return self.__data

	def setData(self, data):
		try:
			#self.__data = FormatData.de_JDate(data)
			self.__data = data
		except ValueError:
			self.__data = self.getIData()

	def getObs(self):
		return self.__obs

	def setObs(self, obs):
		self.__obs = obs + ""


