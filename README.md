# 📦 Problema da Mochila Fracionária (Fractional Knapsack Problem)

Este repositório contém uma implementação do **algoritmo guloso** para resolver o problema da **Mochila Fracionária**, utilizando a linguagem **Python**.

## 💡 Descrição

O Problema da Mochila Fracionária consiste em selecionar itens com peso e valor, de modo a **maximizar o valor total** dentro de uma mochila com capacidade limitada. Diferente da Mochila 0-1, neste problema **é permitido fracionar os itens**, ou seja, é possível adicionar apenas uma parte de um item à mochila.

O algoritmo guloso utilizado escolhe os itens com a **maior razão valor/peso** primeiro, garantindo uma solução ótima.

## 🧠 Estratégia Utilizada

- Ordenar os itens com base na razão valor/peso (`valor / peso`) de forma decrescente.
- Adicionar os itens à mochila enquanto houver capacidade.
- Caso um item não caiba completamente, incluir apenas a fração possível.

## 🛠️ Execução

### Pré-requisitos

- Python 3.x instalado

### Como executar

```bash
python mochila_fracionaria.py
