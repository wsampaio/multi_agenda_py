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


import objetos.financeiro.TipoConta as TipoConta
import objetos.dbConn.CRUD as CRUD

class TipoContaDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "financeiro"
		tabela = "tiposContas"
		pk = "codTipoConta"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, tipoConta):
		self.setStatement(tipoConta, self.__sqlInsert)

	def select(self, pk):
		obj = TipoConta.TipoConta()
		super().setSelect(pk, obj)

		return obj

	def update(self, tipoConta):
		self.setStatement(tipoConta, self.__sqlUpdate)

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
					tiposContas
				ORDER BY
					codTipoConta
			;
		"""
		return super().getList(sql)


