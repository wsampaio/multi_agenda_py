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
CREATE TABLE `tiposCampos` (
	`codTipoCampo`	INTEGER,
	`tipoCampo`	TEXT DEFAULT "",
	`campoDeSenha`	BOOLEAN DEFAULT 0,
	PRIMARY KEY(`codTipoCampo`)
);
"""



class TipoCampo:

	__codTipoCampo = 0
	__tipoCampo = ""
	__campoDeSenha = False

	def __init__(self):
		pass

	def povoarObj(self, array):
		self.setCodTipoCampo(array[0])
		self.setTipoCampo(array[1])
		self.setCampoDeSenha(array[2])
		return self

	def getCodTipoCampo(self):
		return self.__codTipoCampo

	def setCodTipoCampo(self, codTipoCampo):
		try:
			self.__codTipoCampo = int(codTipoCampo)
		except ValueError:
			self.__codTipoCampo = self.getCodTipoCampo()

	def getTipoCampo(self):
		return self.__tipoCampo

	def setTipoCampo(self, tipoCampo):
		self.__tipoCampo = str(tipoCampo)

	def getCampoDeSenha(self):
		return bool(self.__campoDeSenha)

	def setCampoDeSenha(self, campoDeSenha):
		try:
			self.__campoDeSenha = bool(campoDeSenha)
		except ValueError:
			self.__campoDeSenha = self.getCampoDeSenha()


