from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) # PERMITIR QUE ACESSE INFORMAÇÕES DE OUTRA CLASSE, NO CASO A CLASSE MAE (ItemCardapio)
        self.descricao = descricao

    def __str__(self):
            return self._nome