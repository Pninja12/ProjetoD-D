import os
import time


#Defenição dos personagens
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
  "name": "Orc Warrior",
  "hp": 15,
  "mp": 0,
  "ap": 2,
  "wp": 2,
  "init": 2
}

e2 = {
  "name": "Orc Warrior",
  "hp": 15,
  "mp": 0,
  "ap": 2,
  "wp": 2,
  "init": 2
}


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
over = 0
while over < 1:
  print()