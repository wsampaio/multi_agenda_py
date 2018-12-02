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

import objetos.dbConn.ConnSQLite as ConnSQLite
from objetos.dbConn.FormatData import FormatData as FormatData


class CRUD():

	__conn = None
	__cursor = None
	__schema = ""
	__tabela = ""
	__pk = ""

	nomeCampos = []
	tipoCampos = []

	def __init__(self, schema, tabela, pk):
		self.__schema = schema
		self.__tabela = tabela
		self.__pk = pk

		self.montaListaCampo(schema, "", tabela)

		self.__conn = ConnSQLite.ConnSQLite()
		self.__conn.getConn(self.__schema, self.__tabela, self.__pk)
		self.__cursor = self.__conn.cursor()

	def montaListaCampo(self, schema, DBFolder, tabela):

		#try
		sqlCampos = "PRAGMA table_info({})".format(self.__tabela)

		self.__conn = ConnSQLite.ConnSQLite()
		self.__conn.getConn(self.__schema, self.__tabela, self.__pk)
		self.__cursor = self.__conn.cursor()

		self.__cursor.execute(sqlCampos, ())

		#add campos que não sejam a chave primaria
		for array in self.__cursor.fetchall():

			if (int(array[5]) == 0):
				self.nomeCampos.append(array[1])
				self.tipoCampos.append(array[2])

		#Pegar a chave primaria e jogar no fim da lista
		for array in self.__cursor.fetchall():
			if (int(array[5]) > 0):
				self.nomeCampos.append(array["name"])
				self.tipoCampos.append(array["type"])

	def strINSERT(self):
		str =  ""
		str2 = ""

		for nomeCampo in self.nomeCampos:
			str += ", " + nomeCampo
			str2 += ", ?"

		str = str[2:]
		str2 = str2[2:]

		str = """
			INSERT INTO
			{}
			({})
			VALUES
			({});""".format(self.__tabela, str, str2)

		return str

	def strUPDATE(self):
		str = ""

		for nomeCampo in self.nomeCampos:
			str += ", " + nomeCampo + " = ?"

		str = str[2:]

		str = """
			UPDATE
			{}
			SET {}
			WHERE
			{} = ?;""".format(self.__tabela, str, self.__pk)

		return str


	def delete(self, pk):
		sql = \
			"""
			DELETE
				FROM
					""" + self.__tabela + """
				WHERE
					""" + self.__pk + """ = ?
			;
		"""
		self.__cursor.execute(sql, (pk, ))

	def setSelect(self, pk, obj):
		sql = \
			"""
			SELECT
					*
				FROM
					""" + self.__tabela + """
				WHERE
					""" + self.__pk + """ = ?
			;
		"""

		try:
			self.__cursor.execute(sql, (pk, ))
			for array in self.__cursor.fetchall():
				obj.povoarObj(array)
		except ValueError:
			pass

	def getList(self, sql):
		lista = []

		try:
			self.__cursor.executeList(sql)
			for array in self.__cursor.fetchall():
				lista.append(self.select(array[0]))
		except ValueError:
			pass
		return lista


	def setStatement(self, obj, sql):

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

		#verifica se a PK é igual a zero
		#e puxa a autonumeração
		if int(getPk()) < 1:
			setPk(self.__conn.autoNumeracao())
		else:
			context.append(getPk())

		context = []

		i = 0

		for nomeCampo in self.nomeCampos:

			getMethod = getattr(obj,
					"get" +
					nomeCampo[:1].upper() +
					nomeCampo[1:]
			)

			#print("")
			#print(self.tipoCampos[i])
			#print(nomeCampo)

			if self.tipoCampos[i] == "LocalDateTime":
				context.append(
					#FormatData.para_JDate(getMethod())
					getMethod()
				)
			elif self.tipoCampos[i] == "BOOLEAN":
				context.append(
					str(getMethod())
				)
			else:
				context.append(getMethod())

			i += 1

		#print(sql)
		print(context)

		self.__cursor.execute(sql, context)

