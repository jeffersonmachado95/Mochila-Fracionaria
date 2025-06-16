class Item:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

    def valor_por_peso(self):
        return self.valor / self.peso

def mochila_fracionaria(itens, capacidade):
    # Ordena os itens pela razão valor/peso em ordem decrescente
    itens.sort(key=lambda item: item.valor_por_peso(), reverse=True)

    valor_total = 0.0
    for item in itens:
        if capacidade >= item.peso:
            capacidade -= item.peso
            valor_total += item.valor
        else:
            fracao = capacidade / item.peso
            valor_total += item.valor * fracao
            break

    return valor_total

# Exemplo de uso
if __name__ == "__main__":
    itens = [
        Item(valor=60, peso=10),
        Item(valor=100, peso=20),
        Item(valor=120, peso=30),
        Item(valor=70, peso=40)
    ]
    capacidade_mochila = 50
    resultado = mochila_fracionaria(itens, capacidade_mochila)
    print(f"Valor máximo que pode ser carregado: {resultado:.2f}")
