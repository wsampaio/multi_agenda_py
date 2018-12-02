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
CREATE TABLE [catehoriasContas] ( 
[codCategoria] INTEGER, 
[categoria] TEXT);
"""



class CategoriaConta:

	__codCategoria = 0
	__categoria = ""

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodCategoria(array[0])
		self.setCategoria(array[1])
		return self


	def getCodCategoria(self):
		return self.__codCategoria

	def setCodCategoria(self, codCategoria):
		try:
			self.__codCategoria = int(codCategoria)
		except ValueError:
			self.__codCategoria = self.getCodCategoria()

	def getCategoria(self):
		return self.__categoria

	def setCategoria(self, categoria):
		self.__categoria = str(categoria)

