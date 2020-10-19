var form = document.getElementById("form");
var msg = document.getElementById('msg');
var isGorjetaEnabled = true;
form.onsubmit = isValidForm;

addInputListeners();


function addInputListeners(){
	var gjta = document.getElementById("gorjeta");
	gjta.addEventListener("input", toggleGorjeta);
	elmts = document.getElementsByName("gasto");
	for(e of elmts){
		e.addEventListener("input", function(){ formatInput(this); });
	}
}

function formatInput(self){
	//self.value = Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(self.value);
}

function toggleGorjeta(){
	if(isGorjetaEnabled){
		form.gorjeta.labels[0].classList.add("hide");
	}else{
		form.gorjeta.labels[0].classList.remove("hide");
	}
	isGorjetaEnabled = !isGorjetaEnabled;
}

function isValidForm(){
	if(isGorjetaEnabled){
		if(form.gorjeta.value == null || form.gorjeta.value <= 0){
			msg.innerHTML = "Insira um valor valido para gorjeta";
			return false;
		}
	}
	return true;
}