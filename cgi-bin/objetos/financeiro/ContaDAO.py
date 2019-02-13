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


import objetos.financeiro.Conta as Conta
import objetos.dbConn.CRUD as CRUD

class ContaDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "financeiro"
		tabela = "contas"
		pk = "codConta"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, conta):
		self.setStatement(conta, self.__sqlInsert)

	def select(self, pk):

		obj = Conta.Conta()
		super().setSelect(pk, obj)

		return obj

	def update(self, conta):
		self.setStatement(conta, self.__sqlUpdate)

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
					contas
				ORDER BY
					codConta
			;
		"""
		return super().getList(sql)

	def listaPeloVencimento(self, dtRef):
		sql = \
			"""
			SELECT
					*
				FROM
					contas
				WHERE 
					strftime('%Y-%m',dtVencimento) = '{}' 
				ORDER BY
					dtVencimento,
					codConta
			;
		""".format(dtRef)
		
		return super().getList(sql)


	def listaPelaReceita(self, codReceita):
		sql = \
			"""
			SELECT
					*
				FROM
					contas
				WHERE 
					codReceitaPagadora ={} 
				ORDER BY
					dtVencimento,
					codConta
			;
		""".format(codReceita)
		
		return super().getList(sql)


	def somaPelaReceitaPagadora(self, codReceitaPagadora):
		sql = \
			"""
SELECT 
			SUM(CASE WHEN contaPaga = 1 THEN valorPago ELSE valor END) 
		AS vlrTotal 
	FROM 
		contas 
	WHERE 
		codReceitaPagadora = {} 
	GROUP BY 
		codReceitaPagadora
;
		""".format(codReceitaPagadora)
		
		return "{0:.2f}".format(super().getValue(sql, 0.0))
		


	def somaPagasPelaReceita(self, codReceitaPagadora):
		sql = \
			"""
SELECT 
			SUM(CASE WHEN contaPaga = 1 THEN valorPago ELSE valor END) 
		AS vlrTotal 
	FROM 
		contas 
	WHERE 
		codReceitaPagadora = {} AND
		contaPaga = 1
	GROUP BY 
		codReceitaPagadora
;
		""".format(codReceitaPagadora)
		
		return "{0:.2f}".format(super().getValue(sql, 0.0))


	def mediaTresUltimas(self, codTipoConta, dtRef):
		sql = \
			"""

SELECT AVG(valor) FROM (
    SELECT 
 			codConta, 
				CASE
				WHEN contaPaga = 1 THEN
					valorPago
				ELSE
					valor
				END
			AS valor
		FROM 
			contas
		WHERE 
			codTipoConta = {} AND 
			dtVencimento < '{}' 
		ORDER BY 
			dtVencimento DESC 
		LIMIT 3 
); 
		""".format(codTipoConta, dtRef + "-01T00:00")
		
		return "{0:.2f}".format(super().getValue(sql, 0.0))

	def listaContasDeCredito(self):
		sql = \
			"""

			SELECT
					contas.*
				FROM
					contas
						LEFT JOIN tiposContas
							USING (codTipoConta)
				WHERE
					contaDeCredito = 1
				ORDER BY
					dtVencimento DESC
			;
		"""
		
		return super().getList(sql)




