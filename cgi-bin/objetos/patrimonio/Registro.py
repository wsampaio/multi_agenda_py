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

CREATE TABLE registros ( 
codRegistro INTEGER NOT NULL, 
codItem INTEGER DEFAULT (0), 
codVendedor INTEGER DEFAULT (0), 
dtAquisicao LocalDateTime DEFAULT ('0001-01-01T00:00'), 
preco DOUBLE DEFAULT (0), 
garantia STRING DEFAULT (''), 
dtDesuso LocalDateTime DEFAULT ('0001-01-01T00:00'), 

PRIMARY KEY(`codRegistro`), 
FOREIGN KEY(`codItem`) 
REFERENCES `itens`(`codItem`) ON DELETE SET DEFAULT, 
FOREIGN KEY(`codVendedor`) 
REFERENCES `vendedores`(`codVendedor`) ON DELETE SET DEFAULT 

);
"""


from objetos.dbConn.FormatData import FormatData

class Registro:

	__codRegistro = 0
	__codItem = 0
	__codVendedor = 0
	__dtAquisicao = FormatData.de_JDate("0001-01-01T00:00")
	__preco = 0.0
	__garantia = ""
	__dtDesuso = FormatData.de_JDate("0001-01-01T00:00")



	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodRegistro(array[0])
		self.setCodItem(array[1])
		self.setCodVendedor(array[2])
		self.setDtAquisicao(array[3])
		self.setPreco(array[4])
		self.setGarantia(array[5])
		self.setDtDesuso(array[6])

		return self


	def getCodRegistro(self):
		return int(self.__codRegistro)

	def setCodRegistro(self, codRegistro):
		try:
			self.__codRegistro = int(codRegistro)
		except ValueError:
			self.__codRegistro = self.getCodRegistro()

	def getCodItem(self):
		return int(self.__codItem)

	def setCodItem(self, codItem):
		try:
			self.__codItem = int(codItem)
		except ValueError:
			self.__codItem = self.getCodItem()

	def getCodVendedor(self):
		return int(self.__codVendedor)

	def setCodVendedor(self, codVendedor):
		try:
			self.__codVendedor = int(codVendedor)
		except ValueError:
			self.__codVendedor = self.getCodVendedor()

	def getDtAquisicao(self):
		return self.__dtAquisicao

	def setDtAquisicao(self, dtAquisicao):
		try:
			self.__dtAquisicao = dtAquisicao
		except ValueError:
			self.__dtAquisicao = self.getDtAquisicao()

	def getPreco(self):
		return float(self.__preco)

	def setPreco(self, preco):
		try:
			self.__preco = int(preco)
		except ValueError:
			self.__preco = self.getPreco()

	def getGarantia(self):
		return str(self.__garantia)

	def setGarantia(self, garantia):
		try:
			self.__garantia = str(garantia)
		except ValueError:
			self.__garantia = self.getGarantia()

	def getDtDesuso(self):
		return self.__dtDesuso

	def setDtDesuso(self, dtDesuso):
		try:
			self.__dtDesuso = dtDesuso
		except ValueError:
			self.__dtDesuso = self.getDtDesuso()

