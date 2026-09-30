from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) # TODA VEZ QUE CRIAR UM NOVO OBJETO ELE VAI SER ADICIONADO A LISTA DE RESTAURANTES   


    def __str__(self):
        return f"Nome do restaurante: {self._nome} | Categoria do restaurante: {self._categoria}"

    @classmethod # METODO EXCLUSIVO DA CLASSE, ELE PODE SER CHAMADO SEM INSTANCIAR UM OBJETO
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '🚫'

    def alternar_status(self):
        self._ativo = not self._ativo
        status = 'Ativo' if self._ativo else 'Inativo'
        print(f'O restaurante {self._nome} agora está {status}.')

    def receber_avaliacao(self, cliente:str, nota:float):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_avaliacoes = len(self._avaliacao)
        media = soma_das_notas / quantidade_de_avaliacoes
        return f'{media:.1f}'    

    def adicionar_no_cardapio(self, item):
        if isinstance(item, (ItemCardapio)):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, intem in enumerate(self._cardapio, start=1):
            if hasattr(intem, 'descricao'):
                mensagem_prato = f'{i}. Nome: {intem._nome.ljust(20)} | Preço: R$ {intem._preco:.2f} | Descrição: {intem.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {intem._nome.ljust(20)} | Preço: R$ {intem._preco:.2f} | Tamanho: {intem.tamanho}'
                print(mensagem_bebida)