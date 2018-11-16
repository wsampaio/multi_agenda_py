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


import objetos.tarefas.Prioridade as Prioridade
import objetos.dbConn.CRUD as CRUD

class PrioridadeDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "tarefas"
		tabela = "prioridades"
		pk = "codPrioridade"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, prioridade):
		self.setStatement(prioridade, self.__sqlInsert)

	def select(self, pk):

		obj = Prioridade.Prioridade()
		super().setSelect(pk, obj)

		return obj

	def update(self, prioridade):
		self.setStatement(prioridade, self.__sqlUpdate)

# ==================================== CRUD ====================================
# ==============================================================================


	def getLista(self):
		sql = \
			"""
			SELECT
					*
				FROM
					prioridades
				ORDER BY
					codPrioridade
			;
		"""
		return super().getList(sql)

