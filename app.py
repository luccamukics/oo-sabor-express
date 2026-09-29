from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante("Restaurante da Praça", "Gourmet")
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == "__main__":
    main()