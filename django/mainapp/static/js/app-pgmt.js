form.onsubmit = isValidForm;
var minValues = [];

(function setMinValues(){
	var vals = document.getElementsByName("valor");
	for(v of vals){
		minValues.push(parseFloat(v.placeholder));
	}
})();

(function addInputListeners(){
	var pgmts = document.getElementsByName("pgmt");
	var vals = document.getElementsByName("valor");
	for(v of vals){
		v.addEventListener("focusout", function(){ formatInput(this); });
	}
	for(var i = 0; i < pgmts.length; i++){
		pgmts[i].addEventListener("input", setFunctionArgs(toggleValor, i));
	}
})(); //Invoca a si mesmo!

function setFunctionArgs(fun, arg){
	return function(){fun(arg);}
}

function toggleValor(index){
	var label;
	var obj;
	if(form.valor.constructor == RadioNodeList){
		obj = form.valor[index];
		label = obj.labels[0];
	} else {
		obj = form.valor;
		label = obj.labels[0];
	}
	if(!label.classList.contains("hide")){
		label.classList.add("hide");
		obj.value = obj.placeholder;
	}else{
		label.classList.remove("hide");
	}
}

function isValidForm(){
	var pgmts = form.pgmt;
	var vals = form.valor;
	if(pgmts.constructor != RadioNodeList){
		pgmts = [pgmts];
	}
	if(vals.constructor != RadioNodeList){
		vals = [vals];
	}
	var flag = true;
	for(var i = 0; i < pgmts.length; i++){
		if(pgmts[i].checked){
			vals[i].value = 0;
		} else if(vals[i] < minValues[i]){
			flag = false;
		} else {
			pgmts[i].type = "hidden";
			pgmts[i].value = "off";
		}
	}
	return flag;
}

