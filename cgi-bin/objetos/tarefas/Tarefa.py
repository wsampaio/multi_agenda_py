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

class Tarefa:

	__codTarefa = 0
	__codTarefaPai = 0
	__tarefa = ""
	__inicio = FormatData.de_JDate("0001-01-01T00:00")
	__fim = FormatData.de_JDate("0001-01-01T00:00")
	__prazo = FormatData.de_JDate("0001-01-01T00:00")
	__terminado = False
	__ordem = 0
	__codPrioridade = 0
	__codSprint = 0
	__codLista = 0

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodTarefa(array[0])
		self.setCodTarefaPai(array[1])
		self.setTarefa(array[2])
		self.setInicio(FormatData.de_JDate(array[3]))
		self.setFim(FormatData.de_JDate(array[4]))
		self.setPrazo(FormatData.de_JDate(array[5]))
		self.setTerminado(bool(array[6]))
		self.setOrdem(array[7])
		self.setCodPrioridade(array[8])
		return self

	def getCodTarefa(self):
		return self.__codTarefa

	def setCodTarefa(self, codTarefa):
		try:
			self.__codTarefa = int(codTarefa)
		except ValueError:
			self.__codTarefa = self.getCodTarefa()

	def getCodTarefaPai(self):
		return self.__codTarefaPai

	def setCodTarefaPai(self, codTarefaPai):
		try:
			self.__codTarefaPai = int(codTarefaPai)
		except ValueError:
			self.__codTarefaPai = self.getCodTarefaPai()

	def getTarefa(self):
		return self.__tarefa

	def setTarefa(self, tarefa):
		self.__tarefa = tarefa

	def getInicio(self):
		#return FormatData.de_JDate(self.__inicio)
		return self.__inicio

	def setInicio(self, inicio):
		try:
			#self.__inicio = FormatData.de_JDate(inicio)
			self.__inicio = inicio
		except ValueError:
			self.__inicio = self.getInicio()

	def getFim(self):
		#return FormatData.de_JDate(self.__fim)
		return self.__fim

	def setFim(self, fim):
		try:
			#self.__fim = FormatData.de_JDate(fim)
			self.__fim = fim
		except ValueError:
			self.__fim = self.getFim()

	def getPrazo(self):
		#return FormatData.de_JDate(self.__prazo)
		return self.__prazo

	def setPrazo(self, prazo):
		try:
			#self.__prazo = FormatData.de_JDate(prazo)
			self.__prazo = prazo
		except ValueError:
			self.__prazo = self.getPrazo()

	def getTerminado(self):
		return self.__terminado

	def setTerminado(self, terminado):
		try:
			self.__terminado = bool(terminado)
		except ValueError:
			self.__terminado = self.getTerminado()

	def getOrdem(self):
		return self.__ordem

	def setOrdem(self, ordem):
		try:
			self.__ordem = int(ordem)
		except ValueError:
			self.__ordem = self.getOrdem()

	def getCodPrioridade(self):
		return self.__codPrioridade

	def setCodPrioridade(self, codPrioridade):
		try:
			self.__codPrioridade = int(codPrioridade)
		except ValueError:
			self.__codPrioridade = self.getCodPrioridade()

	def getCodSprint(self):
		return self.__codSprint

	def setCodSprint(self, codSprint):
		try:
			self.__codSprint = int(codSprint)
		except ValueError:
			self.__codSprint = self.getCodSprint()

	def getCodLista(self):
		return self.__codLista

	def setCodLista(self, codLista):
		try:
			self.__codLista = int(codLista)
		except ValueError:
			self.__codLista = self.getCodLista()

















