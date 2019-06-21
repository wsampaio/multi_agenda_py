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


import objetos.financeiro.Pagador as Pagador
import objetos.dbConn.CRUD as CRUD

class PagadorDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "financeiro"
		tabela = "pagadores"
		pk = "codPagador"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, pagador):
		self.setStatement(pagador, self.__sqlInsert)

	def select(self, pk):

		obj = Pagador.Pagador()
		super().setSelect(pk, obj)

		return obj

	def update(self, pagador):
		self.setStatement(pagador, self.__sqlUpdate)

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
					pagadores
				ORDER BY
					codPagador
			;
		"""
		return super().getList(sql)

	def getListaCategoria(self):
	
		sql = \
			"""
			SELECT
					*
				FROM
					pagadores
				ORDER BY
					lower(pagador)
			;
		"""
		return super().getList(sql)


	def listaCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					pagadores
				ORDER BY
					pagador
			;
		"""
		return super().getList(sql)

