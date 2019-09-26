
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

	return file_paths


def add2Zip(nomeArquivo):

	# funcao que retorna um array com 
	# o nome dos arquivos na pasta do BD
	file_paths = allFilesPath(diretorioDB)

	# printing the list of all files to be zipped
	print('Following files will be zipped:\n\n')

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
		print('All files zipped successfully!')

def extract(nomeArquivoZip, diretorio):
	# specifying the zip file name
	file_name = "my_python_files.zip"

	# opening the zip file in READ mode
	with ZipFile(nomeArquivo, 'r') as zip:
		# printing all the contents of the zip file
		zip.printdir()

		# extracting all the files
		print('Extracting all the files now...')
		zip.extractall(diretorioDB[0:-15])
		print('Done!')


def fileInfo(nomeArquivo):
	file_name = "example.zip"
	# abre o arquivo zip em modo READ
	with ZipFile(nomeArquivo, 'r') as zip:
		for info in zip.infolist():
			print(info.filename)
			print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
			print(
				'\tSystem:\t\t' + 
				str(info.create_system) + '(0 = Windows, 3 = Unix)'
			)
			print('\tZIP version:\t' + str(info.create_version))
			print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
			print('\tUncompressed:\t' + str(info.file_size) + ' bytes')

def verificaPastaTMP():
	#"""
	# procura a pasta tmp e, se nao encontrar, cria agora
	lista_arq = os.listdir("./")
	print("tmp" not in lista_arq)

	if "tmp" not in lista_arq:
		os.mkdir("./tmp")
		lista_arq = os.listdir("./")

	print("tmp" not in lista_arq)

	# fim de procura pasta tmp
	#"""








def criaBKP():

	verificaPastaTMP()
	
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
	

def main():
	#

        print(allFilesPath(diretorioDB))
	#print(allFilesPath(diretorioTMP))


	#fileInfo(diretorioTMP + "/" + nomeArquivo)
	#extract(diretorioTMP + "/" + nomeArquivo)

	
	#f = open(diretorioTMP + "/" + nomeArquivo, 'r')
	#print(str(f)[:30])
	
	




def teste():
	return "WELLSampaio";




if __name__ == "__main__":
	main()


