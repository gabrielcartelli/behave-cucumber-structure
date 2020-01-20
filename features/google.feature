# language: pt

Funcionalidade: realizar pesquisa no Google

  # Contexto são ações que serão executadas antes de cada cenário.
  Contexto: acessar página de teste
    Dado que acesso a página do Google

  Cenário: acessar página do Google e realizar pesquisa
    Dado que preencho o campo de pesquisa com Python
    Quando clico no botão de pesquisar
    Então devo visualizar os resultados