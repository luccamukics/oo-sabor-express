from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)  # PERMITIR QUE ACESSE INFORMAÇÕES DE OUTRA CLASSE, NO CASO A CLASSE MAE (ItemCardapio)
        self.tamanho = tamanho
        self.tipo = tipo
        self.descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15) # Aplica um desconto de 15% no preço da sobremesa

    