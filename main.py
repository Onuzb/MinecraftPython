#Bruno Branco dos Santos
from ursina import *
from ursina.prefabs.first_person_controller \
    import FirstPersonController

app = Ursina()
Sky()

#Cria o mundo 16x16
for x in range(16):
    for z in range(16):
        Entity(model='cube', color=color.lime,
               texture='white_cube',
               position=(x, 0, z), collider='box')

jogador = FirstPersonController(position=(8, 1, 2))
cores = {'1': color.gray, '2': color.orange, '3': color.azure, '4': color.yellow, '5': color.red, 
         '6': color.green, '7': color.pink, '8': color.violet, '9': color.white, '0': color.black}
cor = color.gray

def input(key):
    global cor
    if key in cores:
        cor = cores[key]
    alvo = mouse.hovered_entity
    if not alvo:
        return
    if key == 'right mouse down':
        Entity(model='cube', color=cor,
               texture='white_cube',
               position=alvo.position + mouse.normal,
               collider='box')
    if key == 'left mouse down':
        destroy(alvo)
app.run()