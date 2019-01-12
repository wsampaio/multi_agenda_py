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


import objetos.patrimonio.Item as Item
import objetos.dbConn.CRUD as CRUD

class ItemDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "patrimonio"
		tabela = "itens"
		pk = "codItem"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, item):
		self.setStatement(item, self.__sqlInsert)

	def select(self, pk):

		obj = Item.Item()
		super().setSelect(pk, obj)

		return obj

	def update(self, item):
		self.setStatement(item, self.__sqlUpdate)

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
					itens
				ORDER BY
					codItem
			;
		"""

		return super().getList(sql)


	def getItemCmb(self):
		sql = \
			"""

			SELECT
					itens.*
				FROM
					itens
						LEFT JOIN modelos
							USING(codModelo)
						LEFT JOIN marcas
							USING(codMarca)
				ORDER BY
					LOWER(item),
					LOWER(marca),
					LOWER(modelo)
			;
		"""

		return super().getList(sql)



