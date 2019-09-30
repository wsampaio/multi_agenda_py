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


import objetos.financeiro.TipoConta as TipoConta
import objetos.dbConn.CRUD as CRUD

class TipoContaDAO(CRUD.CRUD):
	__sqlInsert = ""
	__sqlUpdate = ""

	def __init__(self):

		schema = "financeiro"
		tabela = "tiposContas"
		pk = "codTipoConta"

		super().__init__(schema, tabela, pk)
		self.__sqlInsert = super().strINSERT()
		self.__sqlUpdate = super().strUPDATE()



# ==================================== CRUD ====================================
# ==============================================================================

	def insert(self, tipoConta):
		self.setStatement(tipoConta, self.__sqlInsert)

	def select(self, pk):
		obj = TipoConta.TipoConta()
		super().setSelect(pk, obj)

		return obj

	def update(self, tipoConta):
		self.setStatement(tipoConta, self.__sqlUpdate)

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
					tiposContas
				ORDER BY
					codTipoConta
			;
		"""
		return super().getList(sql)

	def listaPrincipais(self):
		sql = \
			"""
			SELECT
					*
				FROM
					tiposContas
				WHERE
                                        tipoContaAtivo = 1
				ORDER BY
					TipoConta
			;
		"""
		return super().getList(sql)

	def naoListadasNoPeriodo(self, dtRef):
		sql = \
			"""
				SELECT
						*
					FROM
						tiposContas
					WHERE
						codTipoConta NOT IN(
							SELECT 
									codTipoConta 
								FROM 
									contas 
								WHERE 
									strftime('%Y-%m',dtVencimento) = '{}'
						) AND
						tipoContaAtivo = 1
					ORDER BY 
						tipoConta
				;


		""".format(dtRef)
		
		return super().getList(sql)


	def contaOcorrenciasPelaReferencia(self, codTipoConta, dtRef, tipoRef):

		if tipoRef == "pgto":
			tipoRef = "receita.mesReferencia"
		#elif tipoRef = "venc":
		else:
			tipoRef = "contas.dtVencimento"

		sql = \
    		"""
SELECT COUNT(codConta) FROM contas LEFT JOIN receita ON contas.codReceitaPagadora = receita.codReceita 

WHERE strftime("%Y-%m", {}) = '{}' AND codTipoConta = {};





		""".format(tipoRef, dtRef, codTipoConta)

		return "{0:.0f}".format(super().getValue(sql, 0.0))





	def listaCmb(self):
		sql = \
			"""
			SELECT
					*
				FROM
					tiposContas
				ORDER BY
					tipoConta
			;
		"""
		return super().getList(sql)

