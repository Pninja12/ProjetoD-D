import os
import time
import random


#Definição dos personagens
p1 = {
  "name": "Warrior",
  "hp": 32,
  "mp": 5,
  "ap": 2,
  "wp": 5,
  "init": 2
}

p2 = {
  "name": "Priest",
  "hp": 20,
  "mp": 25,
  "ap": 0,
  "wp": 2,
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
x=0
respo="a"
esco=0
over = 0
dado=0
magia=0
inimigo=0
dano=0
morto=0
p1init = 0
p2init = 0
e1init = 0
e2init = 0
e3init = 0
e4init = 0


def baralho():
  x = random.randrange(1,21)
  p1init = p1["init"] + x
  x = random.randrange(1,21)
  p2init = p2["init"] + x
  x = random.randrange(1,21)
  e1init = e1["init"] + x
  x = random.randrange(1,21)
  e2init = e2["init"] + x
  x = random.randrange(1,21)
  e3init = e3["init"] + x
  x = random.randrange(1,21)
  e4init = e4["init"] + x
  x = random.randrange(1,21)

def apagar_ecra(): #Código original do meu colega Ricardo 
 
    #O OS do windows é 'nt'
    if os.name == 'nt':
        #O 'cls' é o código para apagar o terminal no Windows
        os.system('cls')
    else:
        #O 'clear' é o código para apagar o terminal no Mac e no linux
        os.system('clear')

#Início do jogo
print("       Welcome Player")

print("Be ready to defeat your enemies")

time.sleep(5)#Esperar 5 sgundos
apagar_ecra()#Limpa o ecrã

print("Os teus personagens:")
print("|",p1["name"], "|", sep='')
print("---------")
print("|Vida:",p1["hp"],"\n","|Energia:",p1["mp"],"\n","|Armadura:",p1["ap"],"\n","|Ataque:",p1["wp"],"\n", sep='')

print("|",p2["name"], "|", sep='')
print("---------")
print("|Vida:",p2["hp"],"\n","|Energia+:",p2["mp"],"\n","|Armadura:",p2["ap"],"\n","|Ataque:",p2["wp"],"\n", sep='')
time.sleep(5)#Esperar 5 sgundos
apagar_ecra()#Limpa o ecrã




#Começo da batalha

while (p1["hp"] > 0 or p2["hp"] > 0) and (e1["hp"] > 0 or e2["hp"] > 0 or e3["hp"] > 0 or e4["hp"] > 0):
  baralho()
  for i in range(reversed(40)):
    
    if e4["hp"]>0 and e4init == i and (p1["hp"] > 0 or p2["hp"] > 0):
        if p1["hp"] > 0 :
          dano=e1["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
        elif p2["hp"] > 0 :
          dano=e1["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano 

    
    if p2["hp"]>0 and p2init == i and (e1["hp"] > 0 or e2["hp"] > 0 or e3["hp"] > 0 or e4["hp"] > 0):  
        print("É o turno do Priest ")
        if p2["mp"]>0:
          while esco == 0:
            respo=input("Quer usar magia?:")
            if respo.lower() == "s":
              magia=int(input("Dar dano(1) ou Curar(2):"))
              if magia == 2:
                dado = random.randrange(1,7)
                p1["hp"]=p1["hp"] + (dado + p2["wp"])
                p2["mp"]=p2["mp"]-3 
                esco=1
              elif magia == 1:
                dado = random.randrange(1,5)
                if e1["hp"] > 0:
                  print("Inimigo 1:")
                  print("|",e1["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
                if e2["hp"] > 0:
                  print("Inimigo 2:")
                  print("|",e2["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
                if e3["hp"] > 0:
                  print("Inimigo 3:")
                  print("|",e3["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
                if e4["hp"] > 0:
                  print("Inimigo 4:")
                  print("|",e4["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')
                inimigo=int(input("Qual Inimigo quer atacar: "))
                if inimigo == 1:
                  e1["hp"]=e1["hp"] - (dado*2)
                elif inimigo == 2:
                  e2["hp"]=e2["hp"] - (dado*2)
                elif inimigo == 3:
                  e3["hp"]=e3["hp"] - (dado*2)
                elif inimigo == 4:
                  e4["hp"]=e4["hp"] - (dado*2)
                p2["mp"]=p2["mp"]-5
                esco=1
              else:
                print("Introduza novamente. ")
                esco=0
              esco=1
            elif respo.lower() == "n":
              if e1["hp"] > 0:
                  print("Inimigo 1:")
                  print("|",e1["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
              if e2["hp"] > 0:
                  print("Inimigo 2:")
                  print("|",e2["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
              if e3["hp"] > 0:
                  print("Inimigo 3:")
                  print("|",e3["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
              if e4["hp"] > 0:
                  print("Inimigo 4:")
                  print("|",e4["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')
              inimigo=int(input("Qual Inimigo quer atacar: "))
              if inimigo == 1:
                dano=p2["wp"] - e1["ap"]
                if dano > 0:
                  e1["hp"]=e1["hp"] - dano
              elif inimigo == 2:
                dano=p2["wp"] - e2["ap"]
                if dano > 0:
                  e2["hp"]=e2["hp"] - dano
              elif inimigo == 3:
                dano=p2["wp"] - e3["ap"]
                if dano > 0:
                  e3["hp"]=e3["hp"] - dano
              elif inimigo == 4:
                dano=p2["wp"] - e4["ap"]
                if dano > 0:
                  e4["hp"]=e4["hp"] - dano
              esco=1
            else:
              print("Introduza novamente. ")
              esco=0
          esco=0
        else:
          if e1["hp"] > 0:
                print("Inimigo 1:")
                print("|",e1["name"], "|", sep='')
                print("---------")
                print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
          if e2["hp"] > 0:
                  print("Inimigo 2:")
                  print("|",e2["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
          if e3["hp"] > 0:
                  print("Inimigo 3:")
                  print("|",e3["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
          if e4["hp"] > 0:
                  print("Inimigo 4:")
                  print("|",e4["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')
          inimigo=int(input("Qual Inimigo quer atacar: "))
          if inimigo == 1:
                dano=p2["wp"] - e1["ap"]
                if dano > 0:
                  e1["hp"]=e1["hp"] - dano
          elif inimigo == 2:
                dano=p2["wp"] - e2["ap"]
                if dano > 0:
                  e2["hp"]=e2["hp"] - dano
          elif inimigo == 3:
                dano=p2["wp"] - e3["ap"]
                if dano > 0:
                  e3["hp"]=e3["hp"] - dano
          elif inimigo == 4:
                dano=p2["wp"] - e4["ap"]
                if dano > 0:
                  e4["hp"]=e4["hp"] - dano
          
    

    if p1["hp"]>0 and p1init == i and (e1["hp"] > 0 or e2["hp"] > 0 or e3["hp"] > 0 or e4["hp"] > 0): 
        print("É o turno do Warrior ")
        if p1["mp"]>0:
          while esco == 0:
            respo=input("Quer usar magia?:")
            if respo.lower() == "s":
              esco = 1
              dado = random.randrange(1,5)
              if e1["hp"] > 0:
                  print("Inimigo 1:")
                  print("|",e1["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
              if e2["hp"] > 0:
                  print("Inimigo 2:")
                  print("|",e2["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
              if e3["hp"] > 0:
                  print("Inimigo 3:")
                  print("|",e3["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
              if e4["hp"] > 0:
                  print("Inimigo 4:")
                  print("|",e4["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')
              inimigo=int(input("Qual Inimigo quer atacar: "))
              if inimigo == 1:
                e1["hp"]=e1["hp"] - (p1["wp"] + dado)
              elif inimigo == 2:
                e2["hp"]=e2["hp"] - (p1["wp"] + dado)
              elif inimigo == 3:
                e3["hp"]=e3["hp"] - (p1["wp"] + dado)
              elif inimigo == 4:
                e4["hp"]=e4["hp"] - (p1["wp"] + dado)
              p1["mp"]=p1["mp"]-5
            elif respo.lower() == "n":
              if e1["hp"] > 0:
                  print("Inimigo 1:")
                  print("|",e1["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
              if e2["hp"] > 0:
                  print("Inimigo 2:")
                  print("|",e2["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
              if e3["hp"] > 0:
                  print("Inimigo 3:")
                  print("|",e3["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
              if e4["hp"] > 0:
                  print("Inimigo 4:")
                  print("|",e4["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')
              inimigo=int(input("Qual Inimigo quer atacar: "))
              if inimigo == 1:
                dano=p1["wp"] - e1["ap"]
                if dano > 0:
                  e1["hp"]=e1["hp"] - dano
              elif inimigo == 2:
                dano=p1["wp"] - e2["ap"]
                if dano > 0:
                  e2["hp"]=e2["hp"] - dano
              elif inimigo == 3:
                dano=p1["wp"] - e3["ap"]
                if dano > 0:
                  e3["hp"]=e3["hp"] - dano
              elif inimigo == 4:
                dano=p1["wp"] - e4["ap"]
                if dano > 0:
                  e4["hp"]=e4["hp"] - dano
              esco=1
            else:
              print("Introduza novamente. ")
              esco=0
          esco=0
        else:
          if e1["hp"] > 0:
                print("Inimigo 1:")
                print("|",e1["name"], "|", sep='')
                print("---------")
                print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
          if e2["hp"] > 0:
                  print("Inimigo 2:")
                  print("|",e2["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
          if e3["hp"] > 0:
                  print("Inimigo 3:")
                  print("|",e3["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
          if e4["hp"] > 0:
                  print("Inimigo 4:")
                  print("|",e4["name"], "|", sep='')
                  print("---------")
                  print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')
          inimigo=int(input("Qual Inimigo quer atacar: "))
          if inimigo == 1:
                dano=p2["wp"] - e1["ap"]
                if dano > 0:
                  e1["hp"]=e1["hp"] - dano
          elif inimigo == 2:
                dano=p2["wp"] - e2["ap"]
                if dano > 0:
                  e2["hp"]=e2["hp"] - dano
          elif inimigo == 3:
                dano=p2["wp"] - e3["ap"]
                if dano > 0:
                  e3["hp"]=e3["hp"] - dano
          elif inimigo == 4:
                dano=p2["wp"] - e4["ap"]
                if dano > 0:
                  e4["hp"]=e4["hp"] - dano
    

    if e1["hp"]>0 and e1init == i and (p1["hp"] > 0 or p2["hp"] > 0):
        if p1["hp"] > 0 :
          dano=e1["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
        elif p2["hp"] > 0 :
          dano=e1["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano 
      

    if e2["hp"]>0 and e2init == i and (p1["hp"] > 0 or p2["hp"] > 0):
        if p1["hp"] > 0 :
          dano=e2["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
        elif p2["hp"] > 0 :
          dano=e2["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano
    
    
    if e4["hp"]>0 and e4init == i and (p1["hp"] > 0 or p2["hp"] > 0):
      if e4["mp"] > 0:
        dado = random.randrange(1,7)
        if p1["hp"] > 0 :
          p1["hp"]=p1["hp"] - (dado*2)
        elif p2["hp"] > 0 :
          dano=e2["wp"] - p2["ap"]
      else:
        if p1["hp"] > 0 :
          dano=e2["wp"] - p1["ap"]
          if dano > 0:
            p1["hp"]=p1["hp"] - dano
        elif p2["hp"] > 0 :
          dano=e2["wp"] - p2["ap"]
          if dano > 0:
            p2["hp"]=p2["hp"] - dano  
  
    apagar_ecra()#Limpa o ecrã
    print(x)
    print("Your characters:")
    print("|",p1["name"], "|", sep='')
    print("---------")
    print("|Health:",p1["hp"],"\n","|Mana:",p1["mp"],"\n","|Armor:",p1["ap"],"\n","|Damage:",p1["wp"],"\n", sep='')

    print("|",p2["name"], "|", sep='')
    print("---------")
    print("|Health:",p2["hp"],"\n","|Mana:",p2["mp"],"\n","|Armor:",p2["ap"],"\n","|Damage:",p2["wp"],"\n", sep='')