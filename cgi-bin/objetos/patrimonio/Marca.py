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
CREATE TABLE marcas (
codMarca INTEGER PRIMARY KEY NOT NULL, 
marca STRING DEFAULT ('')
);
"""

class Marca:

	__codMarca = 0
	__marca = ""

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodMarca(array[0])
		self.setMarca(array[1])

		return self


	def getCodMarca(self):
		return int(self.__codMarca)

	def setCodMarca(self, codMarca):
		try:
			self.__codMarca = int(codMarca)
		except ValueError:
			self.__codMarca = self.getCodMarca()

	def getMarca(self):
		return str(self.__marca)

	def setMarca(self, marca):
		try:
			self.__marca = str(marca)
		except ValueError:
			self.__marca = self.getMarca()

