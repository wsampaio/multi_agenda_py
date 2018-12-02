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

class Prioridade:

	__codPrioridade = 0
	__ordem = 0
	__prioridade = ""
	__descricao = ""



	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodPrioridade(array[0])
		self.setOrdem(array[1])
		self.setPrioridade(array[2])
		self.setDescricao(array[3])
		return self

	def getCodPrioridade(self):
		return self.__codPrioridade

	def setCodPrioridade(self, codPrioridade):
		try:
			self.__codPrioridade = int(codPrioridade)
		except ValueError:
			self.__codPrioridade = self.getCodPrioridade()

	def getOrdem(self):
		return self.__ordem

	def setOrdem(self, ordem):
		try:
			self.__ordem = int(ordem)
		except ValueError:
			self.__ordem = self.getOrdem()

	def getPrioridade(self):
		return self.__prioridade

	def setPrioridade(self, prioridade):
		self.__prioridade = prioridade

	def getDescricao(self):
		return self.__descricao

	def setDescricao(self, descricao):
		self.__descricao = descricao


