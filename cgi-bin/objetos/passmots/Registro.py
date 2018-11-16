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


"""
CREATE TABLE "REGISTROS" ( 
`COD_REGISTRO` INTEGER, 
`COD_ORIGEM_REGISTRO` INTEGER, 
`COD_TIPO_CAMPO` INTEGER, 
`ORDEM` INTEGER, 
`REGISTRO` TEXT, 
`dtAtualizacao` TEXT );
"""



class Registro:

	__codRegistro = 0
	__codOrigemRegistro = 0
	__codTipoCampo = 0
	__ordem = 0
	__registro = ""
	__dtAtualizacao = FormatData.de_JDate("0001-01-01T00:00")



	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodRegistro(array[0])
		self.setCodOrigemRegistro(array[1])
		self.setCodTipoCampo(array[2])
		self.setOrdem(array[3])
		self.setRegistro(array[4])
		self.setDtAtualizacao(FormatData.de_JDate(array[5]))
		return self


	def getCodRegistro(self):
		return self.__codRegistro

	def setCodRegistro(self, codRegistro):
		try:
			self.__codRegistro = int(codRegistro)
		except ValueError:
			self.__codRegistro = self.getCodRegistro()


	def getCodOrigemRegistro(self):
		return self.__codOrigemRegistro

	def setCodOrigemRegistro(self, codOrigemRegistro):
		try:
			self.__codOrigemRegistro = int(codOrigemRegistro)
		except ValueError:
			self.__codOrigemRegistro = self.getCodOrigemRegistro()


	def getCodTipoCampo(self):
		return self.__codTipoCampo

	def setCodTipoCampo(self, codTipoCampo):
		try:
			self.__codTipoCampo = int(codTipoCampo)
		except ValueError:
			self.__codTipoCampo = self.getCodTipoCampo()


	def getOrdem(self):
		return self.__ordem

	def setOrdem(self, ordem):
		try:
			self.__ordem = int(ordem)
		except ValueError:
			self.__ordem = self.getOrdem()


	def getRegistro(self):
		return self.__registro

	def setRegistro(self, registro):
		self.__registro = str(registro)


	def getDtAtualizacao(self):
		#return FormatData.de_JDate(self.__dtAtualizacao)
		return self.__dtAtualizacao

	def setDtAtualizacao(self, dtAtualizacao):
		try:
			#self.__dtAtualizacao = FormatData.de_JDate(dtAtualizacao)
			self.__dtAtualizacao = dtAtualizacao
		except ValueError:
			self.__dtAtualizacao = self.getDtAtualizacao()

