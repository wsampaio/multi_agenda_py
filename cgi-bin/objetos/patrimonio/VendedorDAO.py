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


import objetos.patrimonio.Vendedor as Vendedor
import objetos.dbConn.CRUD as CRUD

class VendedorDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "patrimonio"
		tabela = "vendedores"
		pk = "codVendedor"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, vendedor):
		self.setStatement(vendedor, self.__sqlInsert)

	def select(self, pk):

		obj = Vendedor.Vendedor()
		super().setSelect(pk, obj)

		return obj

	def update(self, vendedor):
		self.setStatement(vendedor, self.__sqlUpdate)

# ==================================== CRUD ====================================
# ==============================================================================

	def getLista(self):
		sql = \
			"""
			SELECT
					*
				FROM
					vendedores
				ORDER BY
					codVendedor
			;
		"""
		return super().getList(sql)

	def getVendedorCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					vendedores
				ORDER BY
					LOWER(vendedor)
			;
		"""
		return super().getList(sql)

