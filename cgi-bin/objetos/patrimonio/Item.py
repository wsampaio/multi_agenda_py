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
CREATE TABLE itens (

codItem INTEGER PRIMARY KEY NOT NULL, 
item STRING (150) DEFAULT (''), 
codMarca INTEGER DEFAULT (0) 
	REFERENCES marcas (codMarca) ON DELETE SET DEFAULT, 
codModelo INTEGER DEFAULT (0) 
	REFERENCES modelos (codModelo) ON DELETE SET DEFAULT)

"""

class Item:

	__codItem = 0
	__item = ""
	__codMarca = 0
	__codModelo = 0

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodItem(array[0])
		self.setItem(array[1])
		self.setCodMarca(array[2])
		self.setCodModelo(array[3])

		return self

	def getCodItem(self):
		return self.__codItem

	def setCodItem(self, codItem):
		try:
			self.__codItem = int(codItem)
		except ValueError:
			self.__codItem = self.getCodItem()

	def getItem(self):
		return self.__item

	def setItem(self, item):
		self.__item = item

	def getCodMarca(self):
		return self.__codMarca

	def setCodMarca(self, codMarca):
		try:
			self.__codMarca = int(codMarca)
		except ValueError:
			self.__codMarca = self.getCodMarca()

	def getCodModelo(self):
		return self.__codModelo

	def setCodModelo(self, codModelo):
		try:
			self.__codModelo = int(codModelo)
		except ValueError:
			self.__codModelo = self.getCodModelo()



