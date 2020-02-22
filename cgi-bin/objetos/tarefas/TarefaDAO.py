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
		pk = "cod_tarefa"

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
					cod_tarefa
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
					terminado = 'false' AND
					cod_tarefa_pai < 1
				ORDER BY
					cod_prioridade,
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
					cod_tarefa_pai = """ + str(codTarefa) + """
				ORDER BY
					terminado,
					inicio,
					fim,
					ordem
			;
			"""

		return super().getList(sql)

	def subTarefasParaCopiar(self, codTarefa):
		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				WHERE
					cod_tarefa_pai = """ + str(codTarefa) + """
				ORDER BY
					ordem
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
					cod_tarefa_pai < 1
				ORDER BY
					cod_tarefa DESC
			;
			"""

		return super().getList(sql)

	def buscaTarefa(self, qryArray):

		strBusca = ""

		for x in qryArray:
			strBusca += \
				" AND lower(tarefa || ' ' || " + \
				"strftime('%d/%m/%Y', inicio) || ' ' || " + \
				"strftime('%d/%m/%Y', fim)) " + \
				"LIKE lower('%" + x + "%')"

		sql = \
			"""
			SELECT
					*
				FROM
					tarefas
				WHERE
					cod_tarefa_pai < 1 AND
					({})
				ORDER BY
					inicio DESC
			;
			""".format(strBusca[5:])

		return super().getList(sql)

	def ttlSubTarefas(self, codTarefaPai):
		sql = \
			"""
	SELECT
			count(cod_tarefa) as ttl
		FROM
			tarefas
		WHERE
			cod_tarefa_pai = {}
;
 
		""".format(codTarefaPai)
		
		return super().getValue(sql, 0)

	def subTarefasTerminadas(self, codTarefaPai):
		sql = \
			"""
	SELECT
			count(cod_tarefa) as ttl
		FROM
			tarefas
		WHERE
			cod_tarefa_pai = {}
		AND terminado = 'true'
;
 
		""".format(codTarefaPai)
		
		return super().getValue(sql, 0)

	def getProximaSubTarefa(self, codTarefaPai):
		sql = \
			"""
SELECT
		cod_tarefa
	FROM (
		SELECT
			*,
				CASE
					WHEN inicio = '0001-01-01T00:00' THEN
						1
					ELSE
						0
				END
			as foo
			FROM
				tarefas
			WHERE
				cod_tarefa_pai = {} AND
				terminado = 'false'
			ORDER BY
				foo,
				inicio,
				fim,
				ordem
			LIMIT 1
	)
;

		""".format(codTarefaPai)

		#return super().getList(sql)
		return super().getValue(sql, 0)





