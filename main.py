print("Bom dia, serei seu auxiliar na utilização do reconhecedor de faces")
print("1 para treinamento")
print("2 para Capturar imagens")
print("3 para reconhecer")
print("0 para sair")

opcao = input('>')

if opcao == "1":
    import treinamento
elif opcao == "2":
    import captura
elif opcao == "3":
    import reconhecedor_LBPH
elif opcao == '0':
    print("Volte sempre")
