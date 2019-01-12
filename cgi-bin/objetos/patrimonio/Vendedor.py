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
CREATE TABLE vendedores (
codVendedor INTEGER PRIMARY KEY NOT NULL, 
vendedor STRING DEFAULT (''), 
endereco STRING DEFAULT (''), 
contato STRING DEFAULT (''), 
obs STRING DEFAULT ('')
);
"""

class Vendedor:

	__codVendedor = 0
	__vendedor = ""
	__endereco = ""
	__contato = ""
	__obs = ""

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodVendedor(array[0])
		self.setVendedor(array[1])
		self.setEndereco(array[2])
		self.setContato(array[3])
		self.setObs(array[4])

		return self


	def getCodVendedor(self):
		return int(self.__codVendedor)

	def setCodVendedor(self, codVendedor):
		try:
			self.__codVendedor = int(codVendedor)
		except ValueError:
			self.__codVendedor = self.getCodVendedor()

	def getVendedor(self):
		return str(self.__vendedor)

	def setVendedor(self, vendedor):
		try:
			self.__vendedor = str(vendedor)
		except ValueError:
			self.__vendedor = self.getVendedor()

	def getEndereco(self):
		return str(self.__endereco)

	def setEndereco(self, endereco):
		try:
			self.__endereco = str(endereco)
		except ValueError:
			self.__endereco = self.getEndereco()

	def getContato(self):
		return str(self.__contato)

	def setContato(self, contato):
		try:
			self.__contato = str(contato)
		except ValueError:
			self.__contato = self.getContato()

	def getObs(self):
		return str(self.__obs)

	def setObs(self, obs):
		try:
			self.__obs = str(obs)
		except ValueError:
			self.__obs = self.getObs()








