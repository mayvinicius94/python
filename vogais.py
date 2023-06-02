def vogal_ou_consoante(letra):
    letra = letra.lower()
    if letra in ('a', 'e', 'i', 'o', 'u'):
        return True
    elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return False
    else:
        raise ValueError('Não é vogal nem consoante')