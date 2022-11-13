import os
import time
import random


#Definição dos personagens
p1 = {
  "name": "Warrior",
  "hp": 32,
  "mp": 5,
  "ap": 1,
  "wp": 5,
  "init": 2
}

p2 = {
  "name": "Priest",
  "hp": 20,
  "mp": 25,
  "ap": 0,
  "wp": 3,
  "init": 6
}

e1 = {
  "name": "Orc Warrior 1 ",
  "hp": 15,
  "mp": 0,
  "ap": 2,
  "wp": 2,
  "init": 2
}

e2 = {
  "name": "Orc Warrior 2 ",
  "hp": 15,
  "mp": 0,
  "ap": 2,
  "wp": 2,
  "init": 2
}
e3 = {
  "name": "Orc Mage 3 ",
  "hp": 12,
  "mp": 50,
  "ap": 0,
  "wp": 5,
  "init": 1
}

e4 = {
  "name": "Goblin 4 ",
  "hp": 10,
  "mp": 0,
  "ap": 0,
  "wp": 3,
  "init": 7
}


# Variáveis
respo="a"  #Foi usado para respostas em str
esco=0  #Foi usado para respostas em int
dado=0  #Foi usado como dado
magia=0  #Foi usado para respostas onde involve o assuntos de magia
inimigo=0  #Foi usado para respostas onde involve o inimigo
dano=0  #Foi usado para medir quanto de dano recebe algum personagem
p1init = 0  #Foi usado para não alterar o Init oficial do Warrior
p2init = 0  #Foi usado para não alterar o Init oficial do Priest
e1init = 0  #Foi usado para não alterar o Init oficial do Orc
e2init = 0  #Foi usado para não alterar o Init oficial do Orc
e3init = 0  #Foi usado para não alterar o Init oficial do Orc Mage
e4init = 0  #Foi usado para não alterar o Init oficial do Goblin
turn = 1  #Foi usado para ir mostrando os turnos


#Funções
def apagar_ecra(): #Código original do meu colega Ricardo 
 
    #O OS do windows é 'nt'
    if os.name == 'nt':
        #O 'cls' é o código para apagar o terminal no Windows
        os.system('cls')
    else:
        #O 'clear' é o código para apagar o terminal no Mac e no linux
        os.system('clear')

def chamar_inimigo():
  if e1["hp"] > 0:  #Vê se o inimigo 1 tem vida o suficiente para o atacar
    print("Inimigo 1:")
    print("|",e1["name"], "|", sep='')  #{Dá print dos stats do inimigo
    print("---------")
    print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
  if e2["hp"] > 0:  #Vê se o inimigo 2 tem vida o suficiente para o atacar
    print("Inimigo 2:")
    print("|",e2["name"], "|", sep='')  #{Dá print dos stats do inimigo
    print("---------")
    print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
  if e3["hp"] > 0:  #Vê se o inimigo 3 tem vida o suficiente para o atacar
    print("Inimigo 3:")
    print("|",e3["name"], "|", sep='')  #{Dá print dos stats do inimigo
    print("---------")
    print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
  if e4["hp"] > 0:  #Vê se o inimigo 4 tem vida o suficiente para o atacar
    print("Inimigo 4:")
    print("|",e4["name"], "|", sep='')  #{Dá print dos stats do inimigo
    print("---------")
    print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')

def chamar_player():
  print("Os teus personagens:")
  if p1["hp"] > 0:  #Vê se o warrior tem vida o suficiente para o atacar
    print("|",p1["name"], "|", sep='')
    print("---------")  #{Dá print dos stats do warrior
    print("|Vida:",p1["hp"],"\n","|Energia:",p1["mp"],"\n","|Armadura:",p1["ap"],"\n","|Ataque:",p1["wp"],"\n", sep='')

  if p2["hp"] > 0:  #Vê se o priest tem vida o suficiente para o atacar
    print("|",p2["name"], "|", sep='')
    print("---------")  #{Dá print dos stats do priest
    print("|Vida:",p2["hp"],"\n","|Energia:",p2["mp"],"\n","|Armadura:",p2["ap"],"\n","|Ataque:",p2["wp"],"\n", sep='')



apagar_ecra()#Limpa o ecrã


#Início do jogo
print("       Bem vindo jogador")

print("Prepara te para derrotares os teus inimigos!")

time.sleep(5)#Esperar 5 sgundos
apagar_ecra()#Limpa o ecrã

chamar_player()
time.sleep(5)#Esperar 5 sgundos
apagar_ecra()#Limpa o ecrã




#Começo da batalha
#While que decide o fim do jogo. Quando todos os inimigos ou todos os personagens do jogador morrerem, o loop acaba
while (p1["hp"] > 0 or p2["hp"] > 0) and (e1["hp"] > 0 or e2["hp"] > 0 or e3["hp"] > 0 or e4["hp"] > 0):
  
  
  #Lançamento do dado para cada jogador para decidir quem começa
  dado = random.randrange(1,21)
  p1init = p1["init"] + dado
  dado = random.randrange(1,21)
  p2init = p2["init"] + dado
  dado = random.randrange(1,21)
  e1init = e1["init"] + dado
  dado = random.randrange(1,21)
  e2init = e2["init"] + dado
  dado = random.randrange(1,21)
  e3init = e3["init"] + dado
  dado = random.randrange(1,21)
  e4init = e4["init"] + dado
  
  #For que faz cada turno, vai de 40 a 0 e quando o Init de um personagem combina com ele, o personagem age
  for i in range(40,-1,-1):
    print(f"{turn}º turno")
    print()


    #Turno do Goblin(inimigo 4)
    #Se o goblin não estiver morto, nem o inimigo, ele age
    if e4["hp"]>0 and e4init == i and (p1["hp"] > 0 or p2["hp"] > 0):
        if p1["hp"] > 0 :
          dano=e4["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
            print("Goblin deu",dano,"de dano ao warrior")
            time.sleep(3)#Esperar 5 sgundos
        elif p2["hp"] > 0 :
          dano=e4["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano 
            print("Goblin deu",dano,"de dano ao priest")
            time.sleep(3)#Esperar 5 sgundos


    #Turno do Priest
    #Se o priest não estiver morto, nem o inimigo, ele age
    if p2["hp"]>0 and p2init == i and (e1["hp"] > 0 or e2["hp"] > 0 or e3["hp"] > 0 or e4["hp"] > 0):  
        print("É o turno do Priest ")
        if p2["mp"]>0:  #Verifica se o priest tem mana
          while esco == 0:
            respo=input("Quer usar magia?:")
            if respo.lower() == "s":
              magia=int(input("Dar dano(1) ou Curar(2):"))
              if magia == 2 and p1["hp"] > 0: #Verifica se o Warrior não está morto
                dado = random.randrange(1,7)
                p1["hp"]=p1["hp"] + (dado + p2["wp"])
                p2["mp"]=p2["mp"]-3 
                esco=1
              elif magia == 1:
                dado = random.randrange(1,5)
                chamar_inimigo()
                while (True):
                  inimigo=int(input("Qual Inimigo quer atacar: "))
                  if inimigo == 1 and e1["hp"] > 0:
                    e1["hp"]=e1["hp"] - (dado*2)
                    break
                  elif inimigo == 2 and e2["hp"] > 0:
                    e2["hp"]=e2["hp"] - (dado*2)
                    break
                  elif inimigo == 3 and e3["hp"] > 0:
                    e3["hp"]=e3["hp"] - (dado*2)
                    break
                  elif inimigo == 4 and e4["hp"] > 0:
                    e4["hp"]=e4["hp"] - (dado*2)
                    break
                p2["mp"]=p2["mp"]-5
                esco=1
              else:
                print("Introduza novamente. ")
                esco=0
              esco=1
            elif respo.lower() == "n":
              chamar_inimigo()
              while (True):
                inimigo=int(input("Qual Inimigo quer atacar: "))
                if inimigo == 1 and e1["hp"] > 0:
                  dano=p2["wp"] - e1["ap"]
                  if dano > 0:
                    e1["hp"]=e1["hp"] - dano
                  break
                elif inimigo == 2 and e2["hp"] > 0:
                  dano=p2["wp"] - e2["ap"]
                  if dano > 0:
                    e2["hp"]=e2["hp"] - dano
                  break
                elif inimigo == 3 and e3["hp"] > 0:
                  dano=p2["wp"] - e3["ap"]
                  if dano > 0:
                    e3["hp"]=e3["hp"] - dano
                  break
                elif inimigo == 4 and e4["hp"]> 0:
                  dano=p2["wp"] - e4["ap"]
                  if dano > 0:
                    e4["hp"]=e4["hp"] - dano
                  break
              esco=1
            else:
              print("Introduza novamente. ")
              esco=0
          esco=0
        else:
          chamar_inimigo()
          while (True):
            inimigo=int(input("Qual Inimigo quer atacar: "))
            if inimigo == 1 and e1["hp"] > 0:
                  dano=p2["wp"] - e1["ap"]
                  if dano > 0:
                    e1["hp"]=e1["hp"] - dano
                  break
            elif inimigo == 2 and e2["hp"] > 0:
                  dano=p2["wp"] - e2["ap"]
                  if dano > 0:
                    e2["hp"]=e2["hp"] - dano
                  break
            elif inimigo == 3 and e3["hp"] > 0:
                  dano=p2["wp"] - e3["ap"]
                  if dano > 0:
                    e3["hp"]=e3["hp"] - dano
                  break
            elif inimigo == 4 and e4["hp"] > 0:
                  dano=p2["wp"] - e4["ap"]
                  if dano > 0:
                    e4["hp"]=e4["hp"] - dano
                  break
          
    

    if p1["hp"]>0 and p1init == i and (e1["hp"] > 0 or e2["hp"] > 0 or e3["hp"] > 0 or e4["hp"] > 0): 
        print("É o turno do Warrior ")
        if p1["mp"]>0:
          while esco == 0:
            respo=input("Quer usar magia?:")
            if respo.lower() == "s":
              esco = 1
              dado = random.randrange(1,5)
              chamar_inimigo()
              while (True):
                inimigo=int(input("Qual Inimigo quer atacar: "))
                if inimigo == 1 and e1["hp"] > 0:
                  e1["hp"]=e1["hp"] - (p1["wp"] + dado)
                  break
                elif inimigo == 2 and e2["hp"] > 0:
                  e2["hp"]=e2["hp"] - (p1["wp"] + dado)
                  break
                elif inimigo == 3 and e3["hp"] > 0:
                  e3["hp"]=e3["hp"] - (p1["wp"] + dado)
                  break
                elif inimigo == 4 and e4["hp"] > 0:
                  e4["hp"]=e4["hp"] - (p1["wp"] + dado)
                  break
              p1["mp"]=p1["mp"]-5
            elif respo.lower() == "n":
              chamar_inimigo()
              while (True):  
                inimigo=int(input("Qual Inimigo quer atacar: "))
                if inimigo == 1 and e1["hp"] > 0:
                  dano=p1["wp"] - e1["ap"]
                  if dano > 0:
                    e1["hp"]=e1["hp"] - dano
                  break
                elif inimigo == 2 and e2["hp"] > 0:
                  dano=p1["wp"] - e2["ap"]
                  if dano > 0:
                    e2["hp"]=e2["hp"] - dano
                  break
                elif inimigo == 3 and e3["hp"] > 0:
                  dano=p1["wp"] - e3["ap"]
                  if dano > 0:
                    e3["hp"]=e3["hp"] - dano
                  break
                elif inimigo == 4 and e4["hp"] > 0:
                  dano=p1["wp"] - e4["ap"]
                  if dano > 0:
                    e4["hp"]=e4["hp"] - dano
                  break
              esco=1
            else:
              print("Introduza novamente. ")
              esco=0
          esco=0
        else:
          while (True):
            chamar_inimigo()
            inimigo=int(input("Qual Inimigo quer atacar: "))
            if inimigo == 1 and e1["hp"] > 0:
                  dano=p1["wp"] - e1["ap"]
                  if dano > 0:
                    e1["hp"]=e1["hp"] - dano
                  break
            elif inimigo == 2 and e2["hp"] > 0:
                  dano=p1["wp"] - e2["ap"]
                  if dano > 0:
                    e2["hp"]=e2["hp"] - dano
                  break
            elif inimigo == 3 and e3["hp"] > 0:
                  dano=p1["wp"] - e3["ap"]
                  if dano > 0:
                    e3["hp"]=e3["hp"] - dano
                  break
            elif inimigo == 4 and e4["hp"] > 0:
                  dano=p1["wp"] - e4["ap"]
                  if dano > 0:
                    e4["hp"]=e4["hp"] - dano
                  break
    

    if e1["hp"]>0 and e1init == i and (p1["hp"] > 0 or p2["hp"] > 0):
        if p1["hp"] > 0 :
          dano=e1["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
            print("Orc deu",dano,"de dano ao warrior")
            time.sleep(3)#Esperar 5 sgundos
        elif p2["hp"] > 0 :
          dano=e1["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano 
            print("Orc deu",dano,"de dano ao priest")
            time.sleep(3)#Esperar 5 sgundos
      

    if e2["hp"]>0 and e2init == i and (p1["hp"] > 0 or p2["hp"] > 0):
        if p1["hp"] > 0 :
          dano=e2["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
            print("Orc deu",dano,"de dano ao warrior")
            time.sleep(3)#Esperar 5 sgundos
        elif p2["hp"] > 0 :
          dano=e2["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano
            print("Orc deu",dano,"de dano ao priest")
            time.sleep(3)#Esperar 5 sgundos
    
    
    if e3["hp"]>0 and e3init == i and (p1["hp"] > 0 or p2["hp"] > 0):
      if e3["mp"] > 0:
        dado = random.randrange(1,5)
        e3["mp"] = e3["mp"] - 5
        if p1["hp"] > 0 :
          p1["hp"]=p1["hp"] - (dado*2)
          print("Orc Mage deu",dado*2,"de dano ao warrior")
          time.sleep(3)#Esperar 5 sgundos
        elif p2["hp"] > 0 :
          p2["hp"]=p2["hp"] - (dado*2)
          print("Orc Mage deu",dado*2,"de dano ao priest")
          time.sleep(3)#Esperar 5 sgundos
      else:
        if p1["hp"] > 0 :
          dano=e3["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
            print("Orc Mage deu",dano,"de dano ao warrior")
            time.sleep(3)#Esperar 5 sgundos
        elif p2["hp"] > 0 :
          dano=e3["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano  
            print("Orc Mage deu",dano,"de dano ao priest")
            time.sleep(3)#Esperar 5 sgundos


    print()
    chamar_player()
    time.sleep(0.9)
    apagar_ecra()#Limpa o ecrã
  turn = turn + 1


#Fim do jogo/vencedor
if e1["hp"] > 0 and e2["hp"] > 0 and e3["hp"] > 0 and e4["hp"] > 0:
  apagar_ecra()#Limpa o ecrã
  print("O jogador perdeu!  :(")
else:
  apagar_ecra()#Limpa o ecrã
  print("O jogador ganhou!  :)")