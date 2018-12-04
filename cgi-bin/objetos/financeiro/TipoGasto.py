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
CREATE TABLE tiposGastos (
	codTipoGasto INTEGER PRIMARY KEY, 
	tipoGasto VARCHAR2 (255), 
	descricao TEXT
);

"""



class TipoGasto:

	__codTipoGasto = 0
	__tipoGasto = ""
	__descricao = ""

	def __init__(self):
		pass

	def povoarObj(self, array):

		self.setCodTipoGasto(array[0])
		self.setTipoGasto(array[1])
		self.setDescricao(array[2])
		
		return self


	def getCodTipoGasto(self):
		return int(self.__codTipoGasto)

	def setCodTipoGasto(self, codTipoGasto):
		try:
			self.__codTipoGasto = int(codTipoGasto)
		except ValueError:
			self.__codTipoGasto = self.getCodTipoGasto()


	def getTipoGasto(self):
		return str(self.__tipoGasto)

	def setTipoGasto(self, tipoGasto):
		try:
			self.__tipoGasto = str(tipoGasto)
		except ValueError:
			self.__tipoGasto = self.getCodTipoGasto()


	def getDescricao(self):
		return str(self.__descricao)

	def setDescricao(self, descricao):
		try:
			self.__descricao = str(descricao)
		except ValueError:
			self.__descricao = self.getDescricao()

