var nomes = [];
var form = document.getElementById('form');
var msg = document.getElementById('msg');
form.onsubmit = isValidForm;

checkValidType();

function add(self){
	var parent = self.parentNode;
	while(parent.nodeName != "FORM"){
		parent = parent.parentNode;
	}

	var value = parent.add_nome.value
	if(value == ''){
		msg.innerHTML = "Por favor especifique um nome antes de adicionar a pessoa.";
		return;
	}


	var data = document.createElement("input");
	var view = document.createElement("li");
	var btn = document.createElement("button");

	while(nomes.length > 0){
		if(nomes.find(function(v){return v == value})){
			value = parse_duplicate_entry(value);
		} else {
			break;
		}
	}

	data.setAttribute("type", "hidden");
	data.setAttribute("name", "nome");
	data.setAttribute("value", value);
	view.innerHTML = value;
	btn.setAttribute("type", "button");
	btn.innerHTML = "-";
	btn.addEventListener("click", function(){
		remove(view, btn, data);
	});

	parent.appendChild(data);
	parent.children.namedItem("lista").appendChild(view);
	parent.children.namedItem("lista").appendChild(btn);
	nomes.push(value);
	checkValidType();
}

function remove(view, btn, data){
	var index = nomes.indexOf(data.value);
	nomes.splice(index, 1);
	view.remove();
	data.remove();
	btn.remove();
	checkValidType();
}

function parse_duplicate_entry(value){
	let regex = /([(]\d[)])/g
	var end = value.substr(value.length-3,value.length);
	if(end.match(regex) != null){
		var new_end = "(" + (parseInt(end[1])+1) + ")";
		value = value.substr(0, value.length-3) + new_end;
	} else {
		value += " (2)";
	}
	return value;
}

function isValidForm(){
	if(nomes.length <= 0){
		msg.innerHTML = "Adicione ao menos UMA pessoa para continuar.";
		return false;
	}
	return true;
}

function checkValidType(){
	if(nomes.length <= 1){
		form.divisao[0].checked = true;
		form.divisao[1].disabled = true;
		form.divisao[2].disabled = true;
	} else {
		form.divisao[1].disabled = false;
		form.divisao[2].disabled = false;
	}
}