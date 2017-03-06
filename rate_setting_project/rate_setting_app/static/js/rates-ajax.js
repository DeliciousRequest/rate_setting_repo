$(document).ready(function() {

$('#btn_go').click(function(){
	var string = document.getElementById('file_input_1').value;
	document.getElementById('ta_results').value = "File 1's name is: " + string;
		});

$('#btn_clear').click(function(){
	document.getElementById("file_input_1").value = "";
	document.getElementById("file_input_2").value = "";
	document.getElementById("file_input_3").value = "";
	document.getElementById('ta_results').value = ""
		});

});