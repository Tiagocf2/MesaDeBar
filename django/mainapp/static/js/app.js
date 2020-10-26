var form = document.getElementById("form");
var msg = document.getElementById('msg');

function formatInput(self){
	//TODO formatar um numero '1' para '1.00'
	var new_value = self.value;
	if(new_value == NaN){
		new_value = 0;
	} else {
		new_value = new_value.replace(/[.]/g, ',');
	}
	new_value = parseFloat(new_value);
	self.value = new_value.toFixed(2);
}