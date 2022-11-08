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
  "name": "Orc Warrior 3 ",
  "hp": 15,
  "mp": 0,
  "ap": 2,
  "wp": 2,
  "init": 2
}

e4 = {
  "name": "Orc Warrior 4 ",
  "hp": 15,
  "mp": 0,
  "ap": 2,
  "wp": 2,
  "init": 2
}
x=0
respo="a"
esco=0
over = 0
dado=0
magia=0
inimigo=0
dano=0

#Início do jogo
print("       Welcome Player")

print("Be ready to defeat your enemies")

time.sleep(5)#Esperar 5 sgundos
os.system('cls')#Limpar o ecrã

print("Your characters:")
print("|",p1["name"], "|", sep='')
print("---------")
print("|Health:",p1["hp"],"\n","|Mana:",p1["mp"],"\n","|Armor:",p1["ap"],"\n","|Damage:",p1["wp"],"\n", sep='')

print("|",p2["name"], "|", sep='')
print("---------")
print("|Health:",p2["hp"],"\n","|Mana:",p2["mp"],"\n","|Armor:",p2["ap"],"\n","|Damage:",p2["wp"],"\n", sep='')
time.sleep(5)#Esperar 5 sgundos
os.system('cls')#Limpar o ecrã


#Começo da batalha

while over < 1:
  x = random.randrange(1,21)
  while x>0:
    if p2["init"] == x:
      if p2["mp"]>0:
        while esco == 0:
          respo=input("Quer usar magia?:")
          if respo.lower() == "s":
            magia=int(input("Dar dano(1) ou Dar vida(2):"))
            if magia == 2:
              dado = random.randrange(1,7)
              p1["hp"]=p1["hp"] + (dado + p2["wp"])
              p2["mp"]=p2["mp"]-3 
              esco=1
            elif magia == 1:
              dado = random.randrange(1,5)
              print("|",e1["name"], "|", sep='')
              print("---------")
              print("|Health:",e1["hp"],"\n","|Mana:",e1["mp"],"\n","|Armor:",e1["ap"],"\n","|Damage:",e1["wp"],"\n", sep='')
              print("|",e2["name"], "|", sep='')
              print("---------")
              print("|Health:",e2["hp"],"\n","|Mana:",e2["mp"],"\n","|Armor:",e2["ap"],"\n","|Damage:",e2["wp"],"\n", sep='')
              print("|",e3["name"], "|", sep='')
              print("---------")
              print("|Health:",e3["hp"],"\n","|Mana:",e3["mp"],"\n","|Armor:",e3["ap"],"\n","|Damage:",e3["wp"],"\n", sep='')
              print("|",e4["name"], "|", sep='')
              print("---------")
              print("|Health:",e4["hp"],"\n","|Mana:",e4["mp"],"\n","|Armor:",e4["ap"],"\n","|Damage:",e4["wp"],"\n", sep='')
              inimigo=int(input("Atacar inimigo 1,2,3 ou 4? :"))
              if inimigo == 1:
                e1["hp"]=e1["hp"] - (dado*2)
              elif inimigo == 2:
                e2["hp"]=e2["hp"] - (dado*2)
              elif inimigo == 3:
                e3["hp"]=e3["hp"] - (dado*2)
              elif inimigo == 4:
                e4["hp"]=e4["hp"] - (dado*2)
              esco=1
            else:
              print("Introduza novamente. ")
              esco=0
            esco=1
          elif respo.lower() == "n":
            inimigo=int(input("Atacar inimigo 1,2,3 ou 4? :"))
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
    x=x-1
    os.system('cls')