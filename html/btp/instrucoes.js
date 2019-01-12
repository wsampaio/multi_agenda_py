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


function preencheForm(cod, form, urlJSON, idDados) {

	if (cod > 0) {
		urlJSON += "?cod=" + cod;
	}

	$.getJSON(urlJSON, function (data) {
		//console.log(data);
		insereDoJSON(data[idDados][0], form);
	})
	.done(function( json ) {
		carregaCombos();
	});
	
	//
}

function toDateTimeLocal(dateTime){
	var d = new Date(dateTime);
	var str = 
		("0000" + d.getFullYear()).substr(-4) + "-" +
		("0" + (d.getMonth() + 1)).substr(-2) + "-" +
		("0" + (d.getDate())).substr(-2) + "T" +
		("0" + (d.getHours())).substr(-2) + ":" +
		("0" + (d.getMinutes())).substr(-2);

	return str;
}


function formNull(dados, form) {
	insereDoJSON(dados, form);
	carregaCombos();
}

function insereDoJSON(dados, form){

	var obj = dados;

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

				case "text":
					$(this).val(obj[$(this).attr("id")]);
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
}

function setBotoesDeAcao(PK, form, action) {

	$("#" + PK + "Div").css("display", "none");

	$(".copiar").on("click", function(){
		$("#" + PK + "Div").css("display", "block");
		$("#" + PK + "Div").css("background-color", "palegreen");
		$("#" + PK).val(0);
	});

	$(".salvar").on("click", function(){

		var txt = $(this).html();
		var frm = $(form);
		var dados = "";

		if (txt === "Salvar") {
			dados = frm.serialize();
		} else if (txt === "Excluir") {
			var conf = confirm("Deseja mesmo excluir o registro?");

			if (conf){
				dados = frm.serialize() + "&delete=True";
			} else {
				return 0;
			}
		}

		//posta dados SE não for o botao voltar
		if (txt !== "Voltar"){
			$.post(
				action, 
				dados, 
				function(data) {
					//console.log(data);
				}
			)
			.done(function(){
				alert("Dados salvos!");
				fecharJanela();
			});
		} else {
			fecharJanela();
		}

	});
}

function procurarURLParameters(){

	var searchParams = "";

	if ($("#principal").length > 0) {
		//url = new URL($("#principal").attr("url"));
		searchParams = $("#principal").attr("url").split("?")[1];
	} else {
		searchParams = window.location.search;
	}

	return new URLSearchParams(searchParams);

}


function fecharJanela(){
	//fecha janela ou volta a tela antiga
	if ($("#principal").length > 0){
		$("#principal").attr(
			"url", $("#principal").attr("nextUrl")
		);
		$("#principal").attr("nextUrl", "");
		$("#principal").load($("#principal").attr("url"));
	} else {
		self.close();
	}
}



































