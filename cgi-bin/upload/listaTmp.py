#!/usr/bin/python3

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

import os
import cgitb; cgitb.enable()



lista_arq = os.listdir("./tmp")
lista_arq.sort()




#print("Content-type:text/html\r\n\r\n")
print("Content-type: application/json\n")

saida = """{
	"arquivos": ["""

contaLista = len(lista_arq)
i = 1

for fileName in lista_arq:
	saida += """
		{}
			"nomeArquivo": "{}"
		{}""".format(
			"{",
			fileName,
			"}"
		)

	if i < contaLista:
		saida += ","
		i += 1
	else:
		break

saida += """
	]
}
"""

print(
#lista_arq
	saida
		.replace("\n", "")
		.replace("\t", "")
)




