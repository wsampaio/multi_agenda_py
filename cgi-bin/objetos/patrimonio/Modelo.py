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
CREATE TABLE modelos (
codModelo INTEGER PRIMARY KEY NOT NULL, 
codMarca INTEGER DEFAULT (0) REFERENCES marcas (codMarca) ON DELETE SET DEFAULT, 
modelo STRING DEFAULT ('')
);
"""

class Modelo:

	__codModelo = 0
	__codMarca = 0
	__modelo = ""

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodModelo(array[0])
		self.setCodMarca(array[1])
		self.setModelo(array[2])

		return self


	def getCodModelo(self):
		return int(self.__codModelo)

	def setCodModelo(self, codModelo):
		try:
			self.__codModelo = int(codModelo)
		except ValueError:
			self.__codModelo = self.getCodModelo()

	def getCodMarca(self):
		return int(self.__codMarca)

	def setCodMarca(self, codMarca):
		try:
			self.__codMarca = int(codMarca)
		except ValueError:
			self.__codMarca = self.getCodMarca()

	def getModelo(self):
		return str(self.__modelo)

	def setModelo(self, modelo):
		try:
			self.__modelo = str(modelo)
		except ValueError:
			self.__modelo = self.getModelo()





