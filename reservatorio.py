from colorama import Fore, Style

print("Olá! Irei te informar a situação do seu reservatório")
nivel = int(input("Digite o nível do seu reservatório: "))

def definir_cor(nivel):
    if nivel == 1:
        return (Fore.RED, "Nível: Muito baixo (crítico)")
    elif nivel == 2:
        return (Fore.YELLOW, "Nível: Baixo")
    elif nivel == 3:
        return (Fore.GREEN, "Nível: Médio")
    elif nivel == 4:
        return (Fore.CYAN, "Nível: Alto")
    elif nivel == 5:
        return(Fore.BLUE, "Nível: Muito alto (alerta)")
    else:
        return (Fore.RESET, "Nível inválido")

cor, mensagem = definir_cor(nivel)
print(cor + mensagem + Style.RESET_ALL)