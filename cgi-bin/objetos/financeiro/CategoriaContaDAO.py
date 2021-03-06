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


import objetos.financeiro.CategoriaConta as CategoriaConta
import objetos.dbConn.CRUD as CRUD

class CategoriaContaDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "financeiro"
		tabela = "categoriasContas"
		pk = "codCategoria"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, categoriaConta):
		self.setStatement(categoriaConta, self.__sqlInsert)

	def select(self, pk):

		obj = CategoriaConta.CategoriaConta()
		super().setSelect(pk, obj)

		return obj

	def update(self, categoriaConta):
		self.setStatement(categoriaConta, self.__sqlUpdate)

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
					categoriasContas
				ORDER BY
					codCategoria
			;
		"""
		return super().getList(sql)

	def getListaCategoria(self):
	
		sql = \
			"""
			SELECT
					*
				FROM
					categoriasContas
				ORDER BY
					lower(categoria)
			;
		"""
		return super().getList(sql)

	def listaCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					categoriasContas
				ORDER BY
					categoria
			;
		"""
		return super().getList(sql)

