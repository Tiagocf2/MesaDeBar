var form = document.getElementById("form");
var msg = document.getElementById('msg');

function formatInput(self){
	//TODO formatar um numero '1' para '1.00'
	var new_value = parseFloat(self.value);
	if(new_value != NaN){
		self.value = new_value.toFixed(2);
	}
}