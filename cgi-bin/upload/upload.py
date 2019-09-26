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

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
	# strip leading path from file name to avoid 
	# directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	open('./tmp/' + fn, 'wb').write(fileitem.file.read())

	message = 'The file "' + fn + '" was uploaded successfully'
   
else:
	message = 'No file was uploaded'
   
print ("""\
Content-Type: text/html\n
<html>
<body>
<p>%s</p>
</body>
</html>
""" + message

)# % (message,)






