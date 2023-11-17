/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5002/pinguins';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.pinguins.forEach(item => insertList(item.name, 
                                                item.lenght, 
                                                item.depth,
                                                item.flipper,
                                                item.mass,
                                                item.outcome
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputPinguin, inputLenght, inputDepth, inputFlipper,
                        inputMass) => {
    
  const formData = new FormData();
  formData.append('name', inputPinguin);
  formData.append('lenght', inputLenght);
  formData.append('depth', inputDepth);
  formData.append('flipper', inputFlipper);
  formData.append('mass', inputMass);

  let url = 'http://127.0.0.1:5002/pinguin';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5002/pinguin?name='+item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo Pinguin com lenght, depth, flipper e mass
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputPinguin = document.getElementById("newInput").value;
  let inputLenght = document.getElementById("newLenght").value;
  let inputDepth = document.getElementById("newDepth").value;
  let inputFlipper = document.getElementById("newFlipper").value;
  let inputMass = document.getElementById("newMass").value;

  // Verifique se o nome do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5002/pinguins?nome=${inputPinguin}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.pinguins && data.pinguins.some(item => item.name === inputPinguin)) {
        alert("O pinguin já está cadastrado.\nCadastre o pinguin com um nome diferente ou atualize o existente.");
      } else if (inputPinguin === '') {
        alert("O nome do pinguin não pode ser vazio!");
      } else if (isNaN(inputLenght) || isNaN(inputDepth) || isNaN(inputFlipper) || isNaN(inputMass)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputPinguin, inputLenght, inputDepth, inputFlipper, inputMass);
        postItem(inputPinguin, inputLenght, inputDepth, inputFlipper, inputMass);
        alert("Item adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (namePinguin, lenght, depth,flipper, mass, outcome) => {
  var item = [namePinguin, lenght, depth,flipper, mass, outcome];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newInput").value = "";
  document.getElementById("newLenght").value = "";
  document.getElementById("newDepth").value = "";
  document.getElementById("newFlipper").value = "";
  document.getElementById("newMass").value = "";

  removeElement();
}