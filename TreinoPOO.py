from pc import Computador

computador1 = Computador("Dell ", " i5 ", " 8GB ", " Nvidia ", " 1 ")
computador2 = Computador(" HP ", " i7 ", " 16GB ", " Amd ", " 2 ")
computador3 = Computador(" Lenovo ", " i3 ", " 8GB ", " Nvidia ", " 3 ")

print("Qual computador deseja iniciar? [1] [2] [3] ")
escolha = input()
if escolha == '1':
    computador1.iniciar()
    print("Configurações: " +
          computador1.marca +
          computador1.processador +
          computador1.memoria_ram +
          computador1.placa_de_video)
    exit()
elif escolha == '2':
    computador2.iniciar()
    print("Configurações: " +
          computador2.marca +
          computador2.processador +
          computador2.memoria_ram +
          computador2.placa_de_video)
    exit()
elif escolha == '3':
    computador3.iniciar()
    print("Configurações: " +
          computador3.marca +
          computador3.processador +
          computador3.memoria_ram +
          computador3.placa_de_video)
    exit()