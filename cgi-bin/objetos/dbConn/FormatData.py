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

from datetime import datetime

class FormatData:

	def de_JDate(Jdata):
		#retorna um datetime, padrão do python
		#print(Jdata)
		return datetime.strptime(Jdata, '%Y-%m-%dT%H:%M')
		
	def para_JDate(data):
		#retorna uma string com o formato do LocalDateTime (JAVA)
		#Serve para o campo "input datetime-local" do HTML
		
		strData = data.strftime('%m-%dT%H:%M')
		strAno = data.strftime("%Y")

		return \
			("0000" + strAno)[len(strAno):] + \
			"-" + \
			strData

	def para_Data_Serial(data):
		#retorna uma string com o formato data serial
		#Serve para o campo "imput date" do HTML
		strData = str("0000" + data.strftime('%Y'))[-4:]
		strData += "-" + data.strftime('%m')
		strData += "-" + data.strftime('%d')
		return strData

	def mesRef(datetime):
		#retorna uma str no formato desejado
		return datetime.strftime('%m/%Y')

	def mesRefSerial(datetime):
		#retorna uma str no formato desejado
		#serve para o campo "input month" do HTML
		return datetime.strftime('%Y-%m')

	def dataSimples(datetime):
		#retorna uma str no formato desejado
		return datetime.strftime('%d/%m/%Y')

	def horaSimples(data):
		#retorna uma str no formato desejado
		#serve para o campo "input time" do HTML
		return data.strftime('%H:%M')

	def pegaDataHoraSimples(strData):
		#retorna um datetime, padrão do python
		return datetime.strptime(strData, "%d/%m/%Y %H:%M")

	def dataHoraSimples(data):
		#retorna uma string com o formato desejado
		return data.strftime("%d/%m/%Y %H:%M")

