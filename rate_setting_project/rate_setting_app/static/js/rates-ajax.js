$(document).ready(function() {

$('#btn_go').click(function(){
	$.get('/rate_setting/validate_tables/', function( data ) {
		  $('#ta_results').val(data);
		});
	});

$('#btn_clear').click(function(){
	document.getElementById("file_input_1").value = "";
	document.getElementById("file_input_2").value = "";
	document.getElementById("file_input_3").value = "";
	document.getElementById('ta_results').value = ""
		});

});