from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)  # PERMITIR QUE ACESSE INFORMAÇÕES DE OUTRA CLASSE, NO CASO A CLASSE MAE (ItemCardapio)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08) # Aplica um desconto de 8% no preço da bebida