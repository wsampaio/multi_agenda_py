# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
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

