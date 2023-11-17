# Penguin Classifier

Este projeto faz parte da entrega da sprint 4 do curso de pós graduação em **Engenharia de Software - PUC Rio** 

O objetivo da aplicação é trazer, em uma única tela interativa, as classificações de espécies de pinguins com base em características físicas coletas e fornecidas para o modelo. A ideia é prever a qual espécie o pinguin está sendo catalogado
---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5002
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5002 --reload
```

Abra o [http://localhost:5002/#/](http://localhost:5002/#/) no navegador para verificar o status da API em execução.