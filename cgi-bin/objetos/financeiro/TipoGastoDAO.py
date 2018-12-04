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


import objetos.financeiro.TipoGasto as TipoGasto
import objetos.dbConn.CRUD as CRUD

class TipoGastoDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "financeiro"
		tabela = "tiposGastos"
		pk = "codTipoGasto"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, tipoGasto):
		self.setStatement(tipoGasto, self.__sqlInsert)

	def select(self, pk):

		obj = TipoGasto.TipoGasto()
		super().setSelect(pk, obj)

		return obj

	def update(self, tipoGasto):
		self.setStatement(tipoGasto, self.__sqlUpdate)

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
					tiposGastos
				ORDER BY
					codTipoGasto
			;
		"""
		return super().getList(sql)

	def getListaTipoGasto(self):
	
		sql = \
			"""
			SELECT
					*
				FROM
					tiposGastos
				ORDER BY
					lower(tipoGasto)
			;
		"""
		return super().getList(sql)
