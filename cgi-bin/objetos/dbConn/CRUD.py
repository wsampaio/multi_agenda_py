
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
		# Preenche os dados no objeto (obj) com os
		# dados devolvidos pela consulta pela PK
	
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

	def getValue(self, sql, val):
		# devolve o o primeiro valor do primeiro 
		# registro da consulta enviada
		# selecione um valor padrao (val) para retorno
		# em caso de um valor None

		value = val

		try:
			self.__cursor.executeList(sql)
			value = self.__cursor.fetchone()
		except ValueError:
			pass

		if value == None:
			return val
		elif value[0] == None:
			return val
		else:
			return value[0]

	def normalizaNome(str):
		str = ""
		tmp = ""

		for i in len(str):
			if str[i] == "_":
				i = i + 1
				tmp += str[i]
			else:
				tmp += str[i]

		return tmp


	def getList(self, sql):
		# Devolve uma array com objetos

		lista = []

		try:
			self.__cursor.executeList(sql)
			for array in self.__cursor.fetchall():
				lista.append(self.select(array[0]))
		except ValueError:
			pass
		return lista

	def getIndex(self, sql):
		# Devolve uma array soh com as PKs

		listaIndex = []

		try:
			self.__cursor.executeList(sql)
			for array in self.__cursor.fetchall():
				listaIndex.append(array[0])
		except ValueError:
			pass
		return listaIndex

	def setStatement(self, obj, sql):
		# vai puxar os dados do objeto para executar
		# um comando SQL para o BD

		# context = valores que serao passados ao sqlite
		# junto com a string SQL
		context = []
		registroNovo = False
	
		# define os metodos GETTER e SETTER da PK
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

		
		# verifica se a PK é igual a zero
		# e puxa a autonumeração
		if int(getPk()) < 1:
			setPk(self.__conn.autoNumeracao())
			registroNovo = True
		

		

		# ratreia os métodos do objeto com a ajuda
		# da lista com nomes dos campos da tabela
		# e adiciona os dados do objeto a array context
		
		i = 0
		for nomeCampo in self.nomeCampos:

			getMethod = getattr(obj,
					"get" +
					nomeCampo[:1].upper() +
					nomeCampo[1:]
			)
			
			
			# Verifica o tipo de campo do modo que esta
			# registrado no SQLite e formata o registro
			
			if self.tipoCampos[i] == "LocalDateTime":
				context.append(
					FormatData.para_JDate(getMethod())
					#getMethod()
				)
			elif self.tipoCampos[i] == "BOOLEAN":
				if getMethod():
					context.append(1)
				else:
					context.append(0)
			else:
				context.append(getMethod())

			i += 1
			
			
			# TESTES
			#print("")
			#print(self.tipoCampos[i])
			#print(nomeCampo)

		
		# precisa incluir mais uma vez o valor da PK
		# em caso de um UPDATE pois a array de campos do BD
		# inclui a condicao WHERE no final da String
		if registroNovo == False:
			context.append(getPk())

			
			
			
		#TESTES
		#print(sql)
		#print(context)

		self.__cursor.execute(sql, context)

