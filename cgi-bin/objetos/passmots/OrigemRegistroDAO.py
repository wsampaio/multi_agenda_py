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


import objetos.passmots.OrigemRegistro as OrigemRegistro
import objetos.dbConn.CRUD as CRUD

class OrigemRegistroDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "passmots"
		tabela = "origensRegistro"
		pk = "codOrigemRegistro"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, origemRegistro):
		self.setStatement(origemRegistro, self.__sqlInsert)

	def select(self, pk):

		obj = OrigemRegistro.OrigemRegistro()
		super().setSelect(pk, obj)

		return obj

	def update(self, origemRegistro):
		self.setStatement(origemRegistro, self.__sqlUpdate)

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
					origensRegistro
				ORDER BY
					codOrigemRegistro
			;
		"""
		return super().getList(sql)

	def getListaOrigens(self):
	
		sql = \
			"""
			SELECT
					*
				FROM
					origensRegistro
				ORDER BY
					lower(origemRegistro)
			;
		"""
		return super().getList(sql)

	def getListaCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					origensRegistro
				ORDER BY
					lower(origemRegistro)
			;
		"""
		return super().getList(sql)




