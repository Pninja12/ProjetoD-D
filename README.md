# Projeto de Iniciação à Computação
### Relatório

![Imagem com dragões e titlo do jogo D&D](https://s2.glbimg.com/C3GPvh6ECD-33n8Df_v1EecSL9o=/0x0:1600x1000/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2019/m/H/k84eHgTA2l7JhjO3Q6Aw/wallpaper-2560-x-1600-wallpaper.jpg)

## Quem fez e o quê
- Paulo Silva (22206205)
    - Definição das classes
    - Lógica do jogo
    - Embelezamento Final
- Mariana Marques (22207510)
    - Definição de comportamento de cada personagem
    - Definição de início e fim do jogo

---

## Pontuação Extra

[x] Sensibilidade para a usabilidade entre Jogador e Jogo
[ ] Implementação de mais personagens
[X] Implementação de mais variabilidade de inimigos
[X] Implementação de Sistema de Magia para Inimigos
[ ] Implementação de mais Feitiços
[ ] Implementação de mais mecânicas de combate (e.g. Defend, Damage over Time, etc.).

---

## Lógica do código

1. ##### Personagens
    - Cada personagem é um dicionário
    - Eles estão divididos pelos stats que os professores deram
    - O Warrior e o Priest estavam ambos com stats não jogáveis
    - O Warrior tinha a "ap" tão alta que ninguém lhe dava dano, por isso baixamos
    - O Priest tinha o ataque básico tão baixo que não dava dano a ninguém, por isso aumentámos
    - Adicionamos um Orc mago, para fazer um dos pontos extra, para tentar incluir um personagem com magia
    - Adicionamos um Goblin, com 0 de "ap" e 5 de "wp" para deixar o jogo mais desafiante
    - É impossível reviver o Warrior

2. ##### Ciclos
    - O ciclo de 1 turno é um for que começa com um número mais alto que o possível (40) e desce até zero
    - Os inits de cada personagem, quando igualados à variável do for, faz com que ele atuem
    - Se um personagem, ou os inimigos, estiverem mortos, mesmo que o init seja igual ao for, ele não faz nada

3. ##### Funções
    - A função "apagar_ecra" lê em que tipo de computador o utilizador está e apaga todos os conteúdos do terminal
    - A função "chamar_inimigo" dá print de todos os inimigos vivos
    - A função "chamar_player" dá print de todos os personagens do jogador vivos

4. ##### Import's
    - O "import os" é usado para apagar as linhas do terminal
    - O "import time" é usado para fazer o programa esperar algum tempo antes de apagar as linhas do terminal
    - O "import random" é usado para fazer o lançamento do dado tanto para inits como para ataques de magia

5. ##### Informação usada de fora
    - Site [W3Schools](https://www.w3schools.com/python/python_dictionaries.asp)
    - Colegas:
        | Nome | Número | Ajuda |
        | - | - | - |
        | António Rodrigues | 22202884 | Lógica do loop for |
        | Henrique Monteiro | 22202855 | Discussão de lógica sobre o ataque |
        | João Silva | 22004451 | Discussão de lógica sobre o ataque |
        | Ricardo de Almeida | 21807601 | Lógica de apagar o terminal |

