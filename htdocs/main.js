var v1 = [];
var el_lista;

function adicionarPessoa(){
	var text = document.getElementById("adc-pessoa-txt").value
	if(text == "")
		return;
	//v1.push(text);
	var li = document.createElement("li");
	var textNode = document.createTextNode(text);
	li.appendChild(textNode);
	el_lista = document.getElementById("adc-pessoa-lista");
	el_lista.appendChild(li);
}