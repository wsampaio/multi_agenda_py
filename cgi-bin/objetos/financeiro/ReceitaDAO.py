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


import objetos.financeiro.Receita as Receita
import objetos.dbConn.CRUD as CRUD

class ReceitaDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "financeiro"
		tabela = "receita"
		pk = "codReceita"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, receita):
		self.setStatement(receita, self.__sqlInsert)

	def select(self, pk):
		obj = Receita.Receita()
		super().setSelect(pk, obj)

		return obj

	def update(self, receita):
		self.setStatement(receita, self.__sqlUpdate)

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
					receita
				ORDER BY
					codReceita
			;
		"""
		return super().getList(sql)




	def listaCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					receita
				ORDER BY
					dtCredito DESC
			;
		"""
		return super().getList(sql)



	def listaPorMesReferencia(self, dtRef):
		sql = \
			"""
SELECT
		*
	FROM 
		receita
	WHERE
		strftime('%Y-%m', mesReferencia)  = '{}'
	ORDER BY
		dtCredito
;
		""".format(dtRef)

		return super().getList(sql)


	def mediaTresUltimas(self, codPagador, dtRef):
		sql = \
			"""

SELECT AVG(valor) FROM (
	SELECT 
			valor
		FROM 
			receita 
		WHERE 
			codPagador = {} AND
			dtCredito < '{}' 
		ORDER BY 
			dtCredito DESC 
		LIMIT 3 
); 
		""".format(codPagador, dtRef + "-01T00:00")
		
		return "{0:.2f}".format(super().getValue(sql, 0.0))




