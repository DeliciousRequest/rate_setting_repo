$(document).ready(function() {

$('#btn_clear').click(function(){
	$('#file_input_1').val('');
	$('#ta_results').val('');
		});

$('#validationForm').submit(function(){
	$('#ta_results').val('');
	$('#loadingBox').css({
		'display' : 'block'
		})
	$('#ta_results').css({
		'background' : 'darkgray'
		})
	});
});