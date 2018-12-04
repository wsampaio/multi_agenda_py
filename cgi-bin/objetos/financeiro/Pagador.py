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
CREATE TABLE [pagadores] ( 
[codPagador] INTEGER, 
[pagador] TEXT);
"""



class Pagador:

	__codPagador = 0
	__pagador = ""

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodPagador(array[0])
		self.setPagador(array[1])
		return self


	def getCodPagador(self):
		return self.__codPagador

	def setCodPagador(self, codPagador):
		try:
			self.__codPagador = int(codPagador)
		except ValueError:
			self.__codPagador = self.getCodPagador()

	def getPagador(self):
		return self.__pagador

	def setPagador(self, pagador):
		self.__pagador = str(pagador)

