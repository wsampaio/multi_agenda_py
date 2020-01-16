
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

# importing required modules
from zipfile import ZipFile
import os
import datetime

# enderecos dos diretorios do BD e pasta tmp,
# que salvara os arquivos zip
diretorioDB = "../DB-multi_agenda"
diretorioTMP = "./tmp"

#diretorioDB = "../../../../DB-multi_agenda"
#diretorioTMP = "../../../tmp"


def allFilesPath(directory):
	# retorna uma array com o nome de todos arquivos do diretorio
	file_paths = []

	lista_arq = os.listdir(directory)

	for file in lista_arq:
		#seleciona o arquivo somente se o nome terminar em .db
		if file.endswith(".db"):
			file_paths.append(file)

		# seleciona se for o controle de versao
		if file == "controleVersao":
			file_paths.append(file)

	return file_paths


def add2Zip(nomeArquivo):

	dt = datetime.datetime.strptime(nomeArquivo[6:], '%Y%m%d%H%M%S.zip')

	#cria um arquivo de controle de versao
	arquivo = open(diretorioDB + '/controleVersao', 'w')

	arquivo.write(nomeArquivo[6:] + "\n")
	arquivo.write(str(dt))
	arquivo.close()

	# funcao que retorna um array com 
	# o nome dos arquivos na pasta do BD
	file_paths = allFilesPath(diretorioDB)

	# printing the list of all files to be zipped
	print('Following files will be zipped:\n')

	# tenta abrir o arquivo zip e, 
	# se não existir, cria o arquivo
	with ZipFile(nomeArquivo,'w') as zip:
		# passa por cada nome de arquivo na pasta
		# escreve cada arquivo da pasta DB no arquivo zip
		for file in file_paths:
			# pega o nome do arquivo passa para o 
			# arquivo zip incluir e, no segundo parametro, escreve 
			# na arvore do arquivo zip como ficara o nome
			zip.write(
				diretorioDB + "/" + file, diretorioDB[-15:] + "/" + file
			)

			#print nome do arquivo
			print(file)

		# sucesso
		print('\nAll files zipped successfully!')


def extract(nomeArquivoZip):

	# cria um backup antes de limpar pasta DB
	criaBKP()

	# verifica se a pasta DB existe
	if "DB-multi_agenda" in os.listdir("../"):
		# corre os arquivos e remove um por um
		for arq in os.listdir(diretorioDB):
			os.remove(diretorioDB + "/" + arq)

		# remove diretorio DB
		os.rmdir(diretorioDB)

	# abre arquivo para descompactar
	with ZipFile(diretorioTMP + "/" + nomeArquivoZip, 'r') as zip:
		# printa o conteudo do arquivo zip
		zip.printdir()

		# extraindo todos arquivos
		print('Extracting all the files now...')
		zip.extractall(diretorioDB[0:-15])
		print('\nDone!')


def removeArquivo(nomeArquivoZip):
	os.remove(diretorioTMP + "/" + nomeArquivoZip)
	print("arquivo excluído!")



def fileInfo(nomeArquivoZip):

	# procura arquivo de controle da versao em uso
	if "DB-multi_agenda" in os.listdir("../"):
		if "controleVersao" in os.listdir("../DB-multi_agenda"):

			dados = []

			# abre arquivo e pega dados de controle de versao
			arquivo = open('../DB-multi_agenda/controleVersao', 'r')
			for linha in arquivo:
				dados.append(linha.replace("\n", ""))

			arquivo.close()

			dt = datetime.datetime.strptime(dados[1], "%Y-%m-%d %H:%M:%S")


			print("Dados do Controle de Versão:\n")

			print(
				"Nome do arquivo de Backup: " + 
				dados[0]
			)

			print(
				"Data de compactação: " + 
				dt.strftime("%d/%m/%Y às %H:%M")
			)

			print("\n\n")

	file_name = "example.zip"
	# abre o arquivo zip em modo READ
	with ZipFile(diretorioTMP + "/" + nomeArquivoZip, 'r') as zip:
		for info in zip.infolist():
			print(info.filename)
			print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
			print(
				'\tSystem:\t\t' + 
				str(info.create_system) + '(0 = Windows, 3 = Unix)'
			)
			print('\tZIP version:\t' + str(info.create_version))
			print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
			print('\tUncompressed:\t' + str(info.file_size) + ' bytes\n')


def verificaPastaTMP():

	pasta_existe = False

	# lista pastas do diretorio
	lista_arq = os.listdir("./")

	# procura a pasta tmp e, se nao encontrar, cria agora
	if "tmp" not in lista_arq:
		os.mkdir("./tmp")
		lista_arq = os.listdir("./")

	# procura de novo e retorna
	# se achou ou nao
	if "tmp" in lista_arq:
		return True
	else:
		return False


def criaBKP():

	# verifica pasta tmp para continuar sem erro
	if verificaPastaTMP():
	
		# cria novo bkp.zip
		dt = datetime.datetime.now() 

		nomeArquivo = "" +\
			(str(dt.year)) +\
			("0" + str(dt.month))[-2:] +\
			("0" + str(dt.day))[-2:] +\
			("0" + str(dt.hour))[-2:] +\
			("0" + str(dt.minute))[-2:] +\
			("0" + str(dt.second))[-2:] +\
			".zip"

		add2Zip(diretorioTMP + "/" + nomeArquivo)
		# fim de bkp.zip
	

