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


import objetos.tarefas.Tarefa as Tarefa
import objetos.dbConn.CRUD as CRUD
from objetos.dbConn.FormatData import FormatData as FormatData

class TarefaDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "tarefas"
		tabela = "tarefas"
		pk = "codTarefa"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, tarefa):
		self.setStatement(tarefa, self.__sqlInsert)

	def select(self, pk):

		obj = Tarefa.Tarefa()
		super().setSelect(pk, obj)

		return obj

	def update(self, tarefa):
		self.setStatement(tarefa, self.__sqlUpdate)

	def setStatement2(self, obj):
		getPk = getattr(obj,
				"get" +
				self.__pk[:1].upper() +
				self.__pk[1:]
		)
		return getPk()

	def setStatement1(self, obj, sql):

		getPk = getattr(obj,
				"get" +
				self.__pk[:1].upper() +
				self.__pk[1:]
		)

		setPk = getattr(obj,
				"set" +
				self.__pk[:1].upper() +
				self.__pk[1:]
		)

		if getPk() == 0:
			setPk(self.__conn.autoNumeracao())

		if tarefa.getTERMINADO() == True:
			TERMINADO = -1
		else:
			TERMINADO = 0



		context = \
			str(tarefa.getCOD_TAREFA_PAI()),\
			str(tarefa.getTAREFA()),\
			FormatData.para_JDate(tarefa.getINICIO()),\
			FormatData.para_JDate(tarefa.getFIM()),\
			FormatData.para_JDate(tarefa.getPRAZO()),\
			TERMINADO,\
			str(tarefa.getCOD_PRIORIDADE()),\
			str(tarefa.getCOD_TAREFA())

		self.__cursor.execute(sql, context)

# ==================================== CRUD ====================================
# ==============================================================================


	def getLista(self):
		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				ORDER BY
					codTarefa
			;
		"""
		return super().getList(sql)


	def listaTudo(self):
		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				ORDER BY
					cod_prioridade,
					prazo DESC,
					inicio
			;
		"""
		return self.__getList(sql)


	def listaPrincipaisEmAberto(self):
		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				WHERE
					terminado = 0 AND
					codTarefaPai < 1
				ORDER BY
					codPrioridade,
					prazo DESC,
					inicio
			;
			"""
		return super().getList(sql)


	def temSubTarefa(self, codTarefa):
		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				WHERE
					cod_tarefa_pai = """ + str(codTarefa) + """
			;
			"""
		lista = self.__getList(sql)

		return True if len(lista) > 0 else False

	def listaSubTarefas(self, codTarefa):
		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				WHERE
					codTarefaPai = """ + str(codTarefa) + """
				ORDER BY
					terminado,
					inicio,
					fim
			;
			"""

		return super().getList(sql)

	def getListaCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				WHERE
					codTarefaPai < 1
				ORDER BY
					codTarefa DESC
			;
			"""
		return super().getList(sql)







