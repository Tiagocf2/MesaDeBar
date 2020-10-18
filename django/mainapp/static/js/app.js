var nomes = [];

function add(self){
	var parent = self.parentNode;

	while(parent.nodeName != "FORM"){
		parent = parent.parentNode;
	}

	var value = parent.add_nome.value
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
}

function remove(view, btn, data){
		view.remove();
		data.remove();
		btn.remove();
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