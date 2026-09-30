from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa    

restaurante_praca = Restaurante("Restaurante da Praça", "Gourmet")
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()  # Aplica o desconto de 5% no preço da bebida
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 8.00, 'Leite Condensado', 'Médio', 'O melhor pudim da cidade')
sobremesa_pudim.aplicar_desconto()  # Aplica o desconto de 8% no preço do prato
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()