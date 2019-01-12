/*
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
*/


function preencheForm(cod, form, urlJSON) {

	if (cod > 0) {
		urlJSON += "?cod=" + cod;
	}

	$.getJSON(urlJSON, function (data) {
		//console.log(data);
		var obj = data.tarefa[0];

		//each pega uma array com todos elementos da
		//classe .form-control e passa por 'cada' elemento
		$.each($(form + " .form-control, " + form + " .form-check-input"), function(index, element) {

			if($(this).prop("tagName") == "TEXTAREA"){
				$(this).val(obj[$(this).attr("id")].replace(/%r%n/g, "\n", -1));
			} else {

				switch ($(this).attr("type")){

					case "number":
						$(this).val(obj[$(this).attr("id")]);
						break;

					case "checkbox":
						if (obj[$(this).attr("id")] == "True"){
							$(this).attr("checked", "checked")
						} else {
							$(this).prop("checked")
						}

						break;

					case "":
						break;

					case "datetime-local":
						$(this).val(toDateTimeLocal(obj[$(this).attr("id")]));
						break;

					default:
						alert($(this).attr("type"));
						$(this).val(obj[$(this).attr("id")]);
				}
			}
		});

	})
	.done(function( json ) {
		carregaCombos();
	});
	
	//
}

function toDateTimeLocal(dateTime){
	var d = new Date(dateTime);
	var str = 
		d.getFullYear() + "-" +
		("0" + (d.getMonth() + 1)).substr(-2) + "-" +
		("0" + (d.getDate())).substr(-2) + "T" +
		("0" + (d.getHours())).substr(-2) + ":" +
		("0" + (d.getMinutes())).substr(-2);

	return str;
}





