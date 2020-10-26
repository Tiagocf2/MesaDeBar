form.onsubmit = isValidForm;
var isGorjetaEnabled = true;
var groups = [];

addInputListeners();

function addInputListeners(){
	var gjta = document.getElementById("temGorjeta");
	var elmts = document.getElementsByName("gasto");
	var btnGroup = document.getElementById("add-grupo");
	gjta.addEventListener("input", toggleGorjeta);
	if(elmts != null){
		for(e of elmts){
			e.addEventListener("focusout", function(){ formatInput(this); });
		}
	}
	if(btnGroup){
		btnGroup.addEventListener("click", addGroup);
	}
}

function toggleGorjeta(){
	if(isGorjetaEnabled){
		form.gorjeta.value = form.gorjeta.labels[0].placeholder;
		form.gorjeta.labels[0].classList.add("hide");
	}else{
		form.gorjeta.labels[0].classList.remove("hide");
	}
	isGorjetaEnabled = !isGorjetaEnabled;
}

function addGroup(){
	var parent = document.getElementById("group-section");
	var container		= document.createElement("fieldset");
	var inputName 		= document.createElement("input");
	var labelName 		= document.createElement("label");
	var inputValor 		= document.createElement("input");
	var labelValor 		= document.createElement("label");
	var selectPessoas	= document.createElement("select");
	var labelPessoas	= document.createElement("label");
	var btnAddPessoas 	= document.createElement("button");
	var listPessoas		= document.createElement("ul");
	var btnRemove 		= document.createElement("button");

	inputName.setAttribute("type","text");
	inputName.setAttribute("name","grupo-nome");
	inputName.setAttribute("required","required");
	inputName.setAttribute("autocomplete","off");
	inputName.setAttribute("placeholder","Qual item será dividido?");
	labelName.innerHTML = "Nome:&nbsp;";
	labelName.appendChild(inputName);
	inputValor.setAttribute("type","number");
	inputValor.setAttribute("name","grupo-valor");
	inputValor.setAttribute("min", 0.05);
	inputValor.setAttribute("max", 10000);
	inputValor.setAttribute("step", "any");
	inputValor.setAttribute("required","required");
	inputValor.setAttribute("autocomplete","off");
	inputValor.setAttribute("pattern","([\d]*[,]\d\d)");
	inputValor.setAttribute("title","Insira um valor seguindo o padrão para dinheiro: 00,00");
	inputValor.setAttribute("placeholder","0,05");
	inputValor.addEventListener("focusout", function(){ formatInput(this); });
	labelValor.innerHTML = "Valor:&nbsp;";
	labelValor.appendChild(inputValor);

	selectPessoas.setAttribute("name","select");
	for(p of pessoas){
		var op = document.createElement("option");
		op.setAttribute("value", p["id"]);
		if(selectPessoas.children.length == 0){
			op.setAttribute("selected", "selected");
		}
		op.innerHTML = p["nome"];
		selectPessoas.appendChild(op);
	}

	btnAddPessoas.setAttribute("type","button");
	btnAddPessoas.innerHTML = "+";
	btnAddPessoas.addEventListener("click", function(){addGroupMember(this, container)});
	listPessoas.setAttribute("name","lista");
	labelPessoas.innerHTML = "Quem vai participar?&nbsp;";
	labelPessoas.setAttribute("name","label-lista")
	labelPessoas.appendChild(selectPessoas);
	labelPessoas.appendChild(btnAddPessoas);
	labelPessoas.appendChild(listPessoas);
	btnRemove.setAttribute("type","button");
	btnRemove.innerHTML = "x";
	btnRemove.addEventListener("click", function(){
		removeGroup(container);
	});

	container.appendChild(labelName);
	container.appendChild(labelValor);
	container.appendChild(labelPessoas);
	container.appendChild(btnRemove);
	parent.appendChild(container);
	groups.push({"group":container,"members":[]});
}

function addGroupMember(self, group){
	var parent = self.parentElement;
	var select = parent.children.namedItem("select");
	var option = select.options[select.selectedIndex];
	if(!option){
		return;
	}

	var data = document.createElement("input");
	var view = document.createElement("li");
	var btn = document.createElement("button");

	data.setAttribute("type", "hidden");
	data.setAttribute("value", option.value);
	
	var gIndex = -1;
	var mIndex = -1;
	for(var i = 0; i < groups.length; i++){
		if(groups[i]["group"] == group){
			mIndex = groups[i]["members"].push(data);
			gIndex = i;
		}
	}

	view.innerHTML = option.innerHTML;
	btn.setAttribute("type", "button");
	btn.innerHTML = "-";
	btn.addEventListener("click", function(){
		removeGroupMember(view, btn, option, gIndex, mIndex - 1);
	});

	option.disabled = true;
	option.selected = false;
	parent.appendChild(data);
	parent.children.namedItem("lista").appendChild(view);
	parent.children.namedItem("lista").appendChild(btn);
}

function removeGroupMember(view, btn, option, gIndex, mIndex){
	view.remove();
	btn.remove();
	if(gIndex > -1 || mIndex > -1){
		groups[gIndex]["members"].splice(mIndex, 1);
	} else {
		return false;
	}
	option.disabled = false;
	option.selected = true;
}

function removeGroup(container){
	var index = -1;
	for(var i = 0; i < groups.length; i++){
		if(groups[i]["group"] == container){
			index = i;
		}
	}
	if (index > -1) {
		container.remove();
	 	groups.splice(index, 1);
	}
}

function isValidForm(){
	if(isGorjetaEnabled){
		if(form.gorjeta.value == null || form.gorjeta.value <= 0){
			msg.innerHTML = "Insira um valor valido para gorjeta";
			return false;
		}
	}

	for(g of groups){
		var len = g["group"].children.namedItem("label-lista").children.namedItem("lista").children.length;
		if(len / 2 <= 1){
			msg.innerHTML = "Insira ao menos DOIS integrantes ao grupo";
			return false;
		}
		var value = [];
		for(m of g["members"]){
			value.push(m.value);
		}
		var data = document.createElement("input");
		data.setAttribute("type","hidden");
		data.setAttribute("value", value);
		data.setAttribute("name","grupo-pessoa")
		g["group"].appendChild(data);
	}

	return true;
}