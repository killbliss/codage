# Chaine de caractère permettant d'encoder/décoder :
code_ = "p+çS#2z8GceHw`Ormè M;%@3g€KRa!^iv1sA,Q9qCIb:NYDhy'/u0oF?éXEkB*jP¨àTxd-_£$(5JWtZl.ùLn=6f4U§&V)7"


def encode(texte):
    codage = []
    for index, char in enumerate(texte):
        Y = (index + 3) % len(code_)  
    return ''.join(codage), texte 


def decode(cd):
   return texte 


if __name__ == "__main__":
    text = input("Entrez un texte : ")
    print("Encodage : ")
    print(encode(text))
