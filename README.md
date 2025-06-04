# 🛒 Sistema de Gerenciamento de Produtos

Este projeto é um sistema simples em Python para gerenciamento de produtos com funcionalidades como cadastro, alteração, remoção, listagem e recomendações de produtos. Os dados são persistidos em um arquivo JSON.

## 📦 Funcionalidades

- 📋 **Recomendar produtos**  
  Sugestões de produtos pré-definidos caso ainda não haja nenhum produto cadastrado.

- ➕ **Cadastrar produto**  
  Permite adicionar novos produtos ao sistema com código, nome, preço e quantidade.

- ✏️ **Alterar produto**  
  Edita informações de um produto existente a partir de seu código.

- ❌ **Remover produto**  
  Remove um produto do sistema pelo seu código.

- 📃 **Listar produtos**  
  Mostra todos os produtos cadastrados e o total de itens em estoque. Avisa caso a lista esteja vazia

- 💾 **Persistência em JSON**  
  Todos os produtos são salvos no arquivo `dadosprodutos.json` e recarregados automaticamente ao iniciar o programa.