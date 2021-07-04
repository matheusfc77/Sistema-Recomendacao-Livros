# Sistema de Recomendação de Livros
## Projeto de Engenharia de Software do curso de Ciência da Computação - IFC (2021)

### Distribuições / bibliotecas necessárias
* [Anaconda](https://www.anaconda.com/products/individual)

### Como utilizar a API - V1 (Content-Based Filtering)
* Após a instalação da distribuição Anaconda execute, no diretório raíz da **API**, o comando `python apiV1.py`. Atentesse para a versão da API.
* Em seguida execute em seu navegador o aquivo testAPI.html
* No campo "Enter Book", informe um código ISBN contido no arquivo clean_books.csv. Exemplos de códigos válidos: 0002005018, 1841721522, 0553294385.
* Será retornado um JSON com os códigos ISBN dos 10 livros mais recomendados

### Como utilizar a API - V2 (Collaborative Filtering)
* Após a instalação da distribuição Anaconda execute, no diretório raíz da **API**, o comando `python apiV2.py`. Atentesse para a versão da API.
* Em seguida execute em seu navegador o aquivo testAPI.html
* No campo "Enter User", informe um ID de usuário contido no arquivo filtering_recommendation.csv. Exemplos de códigos válidos: 242, 388, 446, 643.
* Será retornado um JSON com os códigos ISBN dos 10 livros mais recomendados
