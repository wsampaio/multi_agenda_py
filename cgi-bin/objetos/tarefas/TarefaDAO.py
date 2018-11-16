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
					terminado = 'false' AND
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
					cod_tarefa_pai = """ + str(codTarefa) + """
				ORDER BY
					terminado,
					inicio,
					fim
			;
			"""
		return self.__getList(sql)













""" DAO EM JAVA
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.multiagenda.tarefas;

import br.com.multiagenda.jdbc.CRUD;
import br.com.multiagenda.jdbc.ConnSQLite;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

/**
 *
 * @author root
 */
public class TarefaDao extends CRUD {
	
	public TarefaDao() throws Exception{
		init("tarefas", "tarefas", "codTarefa");
	}
	
	public void insert (Tarefa tarefa) throws Exception {
		this.setStatement(tarefa, strINSERT());
	}
	
	public Tarefa select(Integer pk) throws Exception{
		Tarefa o = new Tarefa();
		setSelect(pk, (Tarefa) o);
		return o;
	}
	
	public void update(Tarefa tarefa) throws Exception{
		this.setStatement(tarefa, strUPDATE(tarefa.getCodTarefa()));
	}
	
//==============================================================================

	public List<Tarefa> listaTodos(){
		String sql = "SELECT * FROM tarefas";
		
		return (List<Tarefa>)(List<?>) getList(sql, Tarefa.class);
	}
	
	
	public List<Tarefa> listaPrincipaisEmAberto(){
		String sql = 
			"SELECT " +
					"* " +
				"FROM " +
					"tarefas " +
				"WHERE " +
						"terminado = 'false' AND " +
					"codTarefaPai < 1 " +
				"ORDER BY " +
					"codPrioridade, " +
					"prazo DESC, " +
					"inicio";
		
		return (List<Tarefa>)(List<?>) getList(sql, Tarefa.class);
	}

	public List<Tarefa> listaPelaTarefaPai(Integer codTarefa){
		String sql = 
			"SELECT " +
					"*, " +
						"CASE " +
							"WHEN prazo = '0001-01-01T00:00' " +
							"THEN 0 " +
							"ELSE 1 " +
						"END " +
					"AS temPrazo, " +
						"CASE " +
							"WHEN inicio = '0001-01-01T00:00' " +
							"THEN 0 " +
							"ELSE 1 " +
						"END " +
					"AS iniciado " +
				"FROM " +
					"tarefas " +
				"WHERE " +
					"codTarefaPai = " + codTarefa + " " +
				"ORDER BY " +
					"terminado, " +
					"temPrazo DESC, " +
					"iniciado, " +
					"ordem, " +
					"inicio, " +
					"prazo DESC, " +
					"codPrioridade ";
		
		return (List<Tarefa>)(List<?>) getList(sql, Tarefa.class);
	}

	
	public List<Tarefa> listaEmAberto(){
		String sql = 
			"SELECT " +
					"* " +
				"FROM " +
					"tarefas " +
				"WHERE " +
					"terminado = 'false' " +
				"ORDER BY " +
					"codPrioridade, " +
					"prazo DESC, " +
					"inicio";
		
		return (List<Tarefa>)(List<?>) getList(sql, Tarefa.class);
	}

	public List<Tarefa> listaTudo(){
		String sql = 
			"SELECT " +
					"* " +
				"FROM " +
					"tarefas " +
				"WHERE " +
					"codTarefaPai = 0 " +
				"ORDER BY " +
					"codPrioridade, " +
					"prazo DESC, " +
					"inicio";
		
		return (List<Tarefa>)(List<?>) getList(sql, Tarefa.class);
	}
	
	public List<Tarefa> listaGeral(){
		String sql = 
			"SELECT " +
					"* " +
				"FROM " +
					"tarefas " +
				"ORDER BY " +
					"codPrioridade, " +
					"prazo DESC, " +
					"inicio";
		
		return (List<Tarefa>)(List<?>) getList(sql, Tarefa.class);
	}
	
	public List<Tarefa> buscarTarefa(String criterio){
		String sql = 
			"SELECT " +
					"* " +
				"FROM " +
					"tarefas " +
				"WHERE " +
					"lower(tarefa) like '%" + criterio.toLowerCase() + "%' " +
					"AND codTarefaPai = 0 " +
				"ORDER BY " +
					"codPrioridade, " +
					"prazo DESC, " +
					"inicio";
		
		return (List<Tarefa>)(List<?>) getList(sql, Tarefa.class);
	}

	
	public void deletaGeral(Integer codTarefa) throws Exception{
		
		String sql =
			"DELETE FROM " +
				"tarefas" + " " +
			"WHERE " +
				"codTarefa" + " = ?";
		
		Connection conn = new ConnSQLite().getConn("tarefas", "");
		PreparedStatement pstmt = conn.prepareStatement(sql);
		
		try{
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, codTarefa);
			pstmt.execute();
			pstmt.close();
		}catch(SQLException e){
			throw new RuntimeException(e);
		}
		
		sql =
			"DELETE FROM " +
				"tarefas" + " " +
			"WHERE " +
				"codTarefaPai = ?";
		
		try{
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, codTarefa);
			pstmt.execute();
			pstmt.close();
		}catch(SQLException e){
			throw new RuntimeException(e);
		}
		
		sql =
			"DELETE FROM " +
				"historicos " +
			"WHERE " +
				"codTarefa = ?";
		
		try{
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, codTarefa);
			pstmt.execute();
			pstmt.close();
		}catch(SQLException e){
			throw new RuntimeException(e);
		}
	}
	
	public Integer porcentagemTerminada(Integer codTarefa)
		throws SQLException, Exception{
		
		Integer porcentagem = 0;
		
		String sql = 
			"SELECT " +
						"terminada * 100 / total " +
					"AS porcentagem " +

				"FROM " +
						"(SELECT COUNT(codTarefa) as terminada " +
							"FROM tarefas WHERE codTarefaPai = " + codTarefa + " AND terminado like 'true' " +
							"GROUP BY codTarefaPai) " +
					"AS terminadas, " +
						"(SELECT COUNT(codTarefa) as total FROM tarefas " +
							"WHERE codTarefaPai = " + codTarefa + " GROUP BY codTarefaPai) " +
					"AS todas";
		
					/*TODO - tá dando erro na porcentágem de alguns registros*/

			Connection conn = new ConnSQLite().getConn("tarefas", "");
			PreparedStatement pstmt = conn.prepareStatement(sql);
			Tarefa o = new Tarefa();
			
		try (ResultSet rs = pstmt.executeQuery()) {
			while (rs.next()){
				porcentagem = rs.getInt("porcentagem");
			}
		} catch(Exception e) {
			throw new RuntimeException(e);
		}
		pstmt.close();
		
		return porcentagem;
	}

	public Boolean possuiSubTarefas(Integer codTarefa)
		throws Exception{
		
		Boolean possui = false;
		
		String sql = 
			"SELECT " +
					"codTarefa " +
				"FROM " +
					"tarefas " +
				"WHERE " +
					"codTarefaPai = " + codTarefa;


			Connection conn = new ConnSQLite().getConn("tarefas", "");
			PreparedStatement pstmt = conn.prepareStatement(sql);
			Tarefa o = new Tarefa();
			
		try (ResultSet rs = pstmt.executeQuery()) {
			while (rs.next()){
				possui = true;
			}
		} catch(Exception e) {
			throw new RuntimeException(e);
		}
		pstmt.close();
		
		return possui;
	}
	
	public int numerarSubTarefa(int codTarefaPai) throws Exception{
		
		int numOrdem = 99;
		
		
		String sql = 
			"SELECT " +
				"max(ordem) as ordem " +
			"FROM " +
				"tarefas" + " " +
			"WHERE " +
				"codTarefaPai = " + codTarefaPai;
		
		Connection conn = new ConnSQLite().getConn("tarefas", "");
		PreparedStatement pstmt = conn.prepareStatement(sql);
			
		try (ResultSet rs = pstmt.executeQuery()) {
			while (rs.next()){
				numOrdem = rs.getInt("ordem");
			}
		} catch(Exception e) {
			throw new RuntimeException(e);
		}
		pstmt.close();
		
		return ++numOrdem;
	}
	
}

"""
