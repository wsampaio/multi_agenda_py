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


"""
CREATE TABLE [ORIGENS_REGISTRO] ( 
[COD_ORIGEM_REGISTRO] INTEGER, 
[ORIGEM_REGISTRO] TEXT);
"""



class OrigemRegistro:

	__codOrigemRegistro = 0
	__origemRegistro = ""


	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodOrigemRegistro(array[0])
		self.setOrigemRegistro(array[1])
		return self


	def getCodOrigemRegistro(self):
		return self.__codOrigemRegistro

	def setCodOrigemRegistro(self, codOrigemRegistro):
		try:
			self.__codOrigemRegistro = int(codOrigemRegistro)
		except ValueError:
			self.__codOrigemRegistro = self.getCodOrigemRegistro()

	def getOrigemRegistro(self):
		return self.__origemRegistro

	def setOrigemRegistro(self, origemRegistro):
		self.__origemRegistro = str(origemRegistro)

