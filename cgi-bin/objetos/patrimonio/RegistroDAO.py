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


import objetos.patrimonio.Registro as Registro
import objetos.dbConn.CRUD as CRUD
from objetos.dbConn.FormatData import FormatData as FormatData

class RegistroDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "patrimonio"
		tabela = "registros"
		pk = "codRegistro"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, registro):
		self.setStatement(registro, self.__sqlInsert)

	def select(self, pk):

		obj = Registro.Registro()
		super().setSelect(pk, obj)

		return obj

	def update(self, registro):
		self.setStatement(registro, self.__sqlUpdate)


# ==================================== CRUD ====================================
# ==============================================================================


	def getLista(self):
		sql = \
			"""
			SELECT
					*
				FROM
					registros
				ORDER BY
					codRegistro
			;
		"""
		return super().getList(sql)







