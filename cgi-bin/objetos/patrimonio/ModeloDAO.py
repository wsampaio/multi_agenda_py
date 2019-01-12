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


import objetos.patrimonio.Modelo as Modelo
import objetos.dbConn.CRUD as CRUD

class ModeloDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "patrimonio"
		tabela = "modelos"
		pk = "codModelo"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, modelo):
		self.setStatement(modelo, self.__sqlInsert)

	def select(self, pk):

		obj = Modelo.Modelo()
		super().setSelect(pk, obj)

		return obj

	def update(self, modelo):
		self.setStatement(modelo, self.__sqlUpdate)

	def setStatement2(self, obj):
		getPk = getattr(obj,
				"get" +
				self.__pk[:1].upper() +
				self.__pk[1:]
		)
		return getPk()

# ==================================== CRUD ====================================
# ==============================================================================

	def getLista(self):
		sql = \
			"""
			SELECT
					*
				FROM
					modelos
				ORDER BY
					codModelo
			;
		"""
		return super().getList(sql)

	def getModeloCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					modelos
				ORDER BY
					LOWER(modelo)
			;
		"""
		return super().getList(sql)
