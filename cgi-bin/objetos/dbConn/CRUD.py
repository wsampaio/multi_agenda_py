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

        if int(getPk()) == 0:
            setPk(self.__conn.autoNumeracao())
        else:
            context.append(getPk())


        #print(sql)
        #print(context)

        self.__cursor.execute(sql, context)


""" EM JAVA

public class CRUD {    
    
    public Object getMetodo(String metodo, Object obj) throws Exception {
        
        Class c = Class.forName(obj.getClass().getName());
        
        Object returnValue;
        Method m;

        try {
            // parameter type is null
            m = c.getMethod(metodo, null);
            
            //executa o método
            returnValue = m.invoke(obj);
            
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return returnValue;
    }
    
    public void setMetodo(int indexCampo, Object obj, Object valor){

        //Concatena o nome do método
        String strMetodo = 
                "set" +
                nomeCampo.get(indexCampo).substring(0, 1).toUpperCase() +
                nomeCampo.get(indexCampo).substring(1)
        ;

        try {

            //define o tipo de dado
            //que entra em cArg
            Class[] cArg = new Class[1];
            switch (tipoCampo.get(indexCampo)) {
                case "INTEGER":
                    cArg[0] = int.class;
                    break;

                case "LocalDateTime":
                    cArg[0] = LocalDateTime.class;
                    break;

                case "BOOLEAN":
                    cArg[0] = boolean.class;
                    break;
                                
                case "TEXT":
                    cArg[0] = String.class;
                    break;
                    
                /*TODO - preencher com outros tipo de dados*/





                default: 
                    //cArg[0] = int.class;
                    break;
            }


            Method m = obj.getClass().getMethod(strMetodo, cArg);

            //executa o metodo
            m.invoke(obj, valor);
            
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
    
    public void setStatement(Object obj, String sql) throws Exception{
        
        try{
            
            //Acessa a autonumeração
            if ((int) getMetodo(
                    "get" +
                    pk.substring(0, 1).toUpperCase() +
                    pk.substring(1), 
                    obj) == 0){
                
                setMetodo(nomeCampo.size()-1, obj, 
                    new AutoNumeracao().numerar(schema, tabela, pk)
                );
            }
            
            //prepara o Statement e preenche os campos
            stmt = conn.prepareStatement(sql);
            
            for(int i = 0; i < nomeCampo.size(); i++){
                
                //switch que verifica o tipo de campo e
                //preenche o stmt com o tipo correto
                switch (tipoCampo.get(i)) {
                    case "INTEGER":
                        stmt.setInt(
                            i+1, 
                            (int) getMetodo(
                                "get" +
                                nomeCampo.get(i).substring(0, 1).toUpperCase() +
                                nomeCampo.get(i).substring(1), 
                                obj
                            )
                        );
                        break;

                    case "LocalDateTime":
                        //passa para o SQLite como String
                        LocalDateTime D = (LocalDateTime) getMetodo(
                                "get" +
                                nomeCampo.get(i).substring(0, 1).toUpperCase() +
                                nomeCampo.get(i).substring(1), 
                                obj
                            );
                        
                        stmt.setString(i+1, D.toString());
                        break;

                    case "BOOLEAN":
                        stmt.setString(
                            i+1, 
                            //(boolean) getMetodo(
                            getMetodo(
                                "get" +
                                nomeCampo.get(i).substring(0, 1).toUpperCase() +
                                nomeCampo.get(i).substring(1), 
                                obj
                            ).toString()
                        );
                        break;
                    
                    case "TEXT":
                        stmt.setString(
                            i+1, 
                            (String) getMetodo(
                                "get" +
                                nomeCampo.get(i).substring(0, 1).toUpperCase() +
                                nomeCampo.get(i).substring(1), 
                                obj
                            )
                        );
                        break;
                        
                    
                    /*TODO - preencher com outros tipo de dados*/





                    default: 
                        //cArg[0] = int.class;
                        break;
                }
            }
            
            stmt.execute();
            stmt.close();
            
        }catch(Exception e){
            throw new RuntimeException(e);
        }
    }
    
    public List<Object> getList(String sql, Class objClass){
        
        try {
            List<Object> lista = new ArrayList<>();
            stmt = conn.prepareStatement(sql);

            ResultSet rs = stmt.executeQuery();

            while (rs.next()){
                
                Object o = Class.forName(objClass.getName()).newInstance();
                setSelect(rs.getInt(pk), o);
                lista.add(o);
            }
            rs.close();
            stmt.close();

            return lista;
        } catch(Exception e) {
            throw new RuntimeException(e);
        }
    }
    
}

"""
