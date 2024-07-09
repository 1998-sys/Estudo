## Funções Suplementares Estatística Descritiva
import re


## Função para tratamento da coluna Ticket

def limpar_string(s):
    """
    Remove todos os caracteres não numéricos de uma string.

    Parâmetros:
    s (str): A string a ser limpa.

    Retorna:
    str: Uma nova string contendo apenas os caracteres numéricos da string original.
    """
    return re.sub(r'\D', '', s)





