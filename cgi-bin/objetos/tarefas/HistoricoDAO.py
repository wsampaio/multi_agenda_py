# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import objetos.tarefas.Historico as Historico
import objetos.dbConn.CRUD as CRUD

class HistoricoDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "tarefas"
		tabela = "historicos"
		pk = "codHistorico"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, historico):
		self.setStatement(historico, self.__sqlInsert)

	def select(self, pk):

		obj = Historico.Historico()
		super().setSelect(pk, obj)

		return obj

	def update(self, historico):
		self.setStatement(historico, self.__sqlUpdate)

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
					historicos
				ORDER BY
					codHistorico
			;
		"""
		return super().getList(sql)

