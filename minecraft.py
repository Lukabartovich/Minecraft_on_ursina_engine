from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from file_opener import *
from sheep_file import *

app = Ursina()
window.exit_button.disable()
window.fps_counter.disable()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
wood_texture = load_texture('assets/wood_block.png')
water_texture = load_texture('assets/water_block.png')
fire_texture = load_texture('assets/fire_block.png')
leaves_texture = load_texture('assets/leaves_block.png')
diamond_texture = load_texture('assets/diamond_block.png')
tnt_texture = load_texture('assets/tnt_block.png')
portal_texture = load_texture('assets/portal_block.png')
tree_texture = load_texture('assets/tree_block.png')
slime_texture = load_texture('assets/slime_block.png')
glass_texture = load_texture('assets/glass_block.png')
sand_texture = load_texture('assets/sand_block.png')
diamond_texture_2 = load_texture('assets/diamond_block2.png')
gold_texture_1 = load_texture('assets/gold_block1.png')
gold_texture_2 = load_texture('assets/gold_block2.png')


block_pick = 1
enable_state = True
fly_state = True
fly_hight = 25

voxeles = 15
max_blocks = 18

super_speed = 10
super_jump = 10

sheep_speed = 1
how_many_sheeps = 0

texture_image_path = 'assets/grass.png'

portal_state = 0
portal_ready = False

portal_number = 0
migration = 0

slime_number = 0

index = 0

day_length = 1200
sunset_length = 120

start_time = time.time()
sky_state = 1

glass_col = 0
glass_forever = True

falling_limit = -30

ground_not_normal = True
stone_depth = random.randint(3, 6)
stone_choice = random.randint(1, 2)
r_land = random.randint(1, 2)

def v_minus(voxel):
    pos = (voxel.x, voxel.y - 1, voxel.z)
    destroy(voxel, delay=0.3)
    voxel = Voxel(position=pos, texture=fire_texture)
    destroy(voxel, delay=0.3)

def input(key):
    global fly_state
    global max_blocks
    global block_pick
    global fly_hight

    if key == 'f':
        if fly_state == False:
            fly_state = True
        else:
            fly_state = False

    if fly_state == True:
        if key == 'up arrow' or key == 'up arrow hold':
            fly_hight += 1
            # print('up')
        if key == 'down arrow' or key == 'down arrow hold':
            fly_hight -= 1
            # print('down')


    if key == 'b':
        show = Show()
        block_pick = 1
        show.texture = 'assets/grass.png'

    if key == 'right arrow' or key == 'right arrow hold' or key == 'scroll down':
        if block_pick < max_blocks - 1:
            block_pick += 1
        else:
            block_pick = max_blocks - 1

    if key == 'left arrow' or key == 'left arrow hold' or key == 'scroll up': 
        if block_pick > 1:
            block_pick -= 1

def update():
    global block_pick
    global enable_state
    global fly_state
    global index
    global migration

    show = Show()
    if block_pick == 1:
        show.texture =  'assets/grass.png'
    if block_pick == 2:
        show.texture =  'assets/stone.png'
    if block_pick == 3:
        show.texture =  'assets/brick.png'
    if block_pick == 4:
        show.texture =  'assets/dirt.png'
    if block_pick == 5:
        show.texture =  'assets/wood.png'
    if block_pick == 6:
        show.texture =  'assets/water.jpg'
    if block_pick == 7:
        show.texture =  'assets/fire.jpg'
    if block_pick == 8:
        show.texture =  'assets/leaves.png'
    if block_pick == 9:
        show.texture =  'assets/diamond.jpg'
    if block_pick == 10:
        show.texture =  'assets/slime.png'
    if block_pick == 11:
        show.texture = 'assets/clear.png'
        show.texture = 'assets/glass.png'
    if block_pick == 12:
        show.texture = 'assets/sand.jpg'
    if block_pick == 13:
        show.texture = 'assets/diamond2.jpg'
    if block_pick == 14:
        show.texture = 'assets/gold1.jpg'
    if block_pick == 15:
        show.texture = 'assets/gold2.jpg'
    if block_pick == 16:
        show.texture = 'assets/portal.jpg'
    if block_pick == 17:
        show.texture = 'assets/the_tnt.jpg'

    if player.position.y < falling_limit:
        player.position = (3, 23, 3)
        YouDied()
        enable_state = False

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['left control']:
        player.speed = super_speed
        player.jump_height = super_jump
    else:
        player.speed = 5
        player.jump_height = 2
        
    if enable_state == False:
        player.disable()
    else:
        player.enable()

    if fly_state == True:
        player.gravity = 0
        player.position = (player.x, fly_hight, player.z)
    else:
        player.gravity = 1

    if portal_ready == True and fly_state == True:
        portals_position = [open_file('files/portal1.txt'), open_file('files/portal2.txt')]
        if str(list((int(player.position.x), int(player.position.z)))) in portals_position:
            index = portals_position.index(str(list((int(player.position.x), int(player.position.z))))) + 1
        elif str(list((int(player.position.x+1), int(player.position.z+1)))) in portals_position:
            index = portals_position.index(str(list((int(player.position.x+1), int(player.position.z+1))))) + 1
        elif str(list((int(player.position.x+1), int(player.position.z)))) in portals_position:
            index = portals_position.index(str(list((int(player.position.x+1), int(player.position.z))))) + 1
        elif str(list((int(player.position.x), int(player.position.z+1)))) in portals_position:
            index = portals_position.index(str(list((int(player.position.x), int(player.position.z+1))))) + 1
        elif str(list((int(player.position.x-1), int(player.position.z-1)))) in portals_position:
            index = portals_position.index(str(list((int(player.position.x-1), int(player.position.z-1))))) + 1
        elif str(list((int(player.position.x-1), int(player.position.z)))) in portals_position:
            index = portals_position.index(str(list((int(player.position.x-1), int(player.position.z))))) + 1
        elif str(list((int(player.position.x), int(player.position.z-1)))) in portals_position:
            index = portals_position.index(str(list((int(player.position.x), int(player.position.z-1))))) + 1
        else:
            index = 0
            migration = 0
        
        if migration == 0:
            if index == 1:
                position_x = int(open_file('files/portal2_position_x.txt'))
                position_z = int(open_file('files/portal2_position_z.txt'))
                position_y = int(open_file('files/portal2_position_y.txt')) + 1
                player.y = position_y
                player.x = position_x
                player.z = position_z
                migration = 1
            if index == 2:
                position_x = int(open_file('files/portal1_position_x.txt'))
                position_z = int(open_file('files/portal1_position_z.txt'))
                position_y = int(open_file('files/portal1_position_y.txt')) + 1
                player.y = position_y
                player.x = position_x
                player.z = position_z
                migration = 1

class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            scale = 0.5)
        
    def input(self, key):
        global texture_image_path
        global portal_state
        global portal_ready
        global slime_number
        global glass_col
        global glass_forever

        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3:
                    voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4:
                    voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 5:
                    voxel = Voxel(position=self.position + mouse.normal, texture=wood_texture)
                if block_pick == 6:
                    voxel = Voxel(position=self.position + mouse.normal, texture=water_texture)
                    water_collide = voxel.intersects()
                    if str(water_collide.entity.texture) == 'fire_block.png':
                        destroy(voxel, delay=0.5)
                        destroy(water_collide.entity, delay=0.5)
                if block_pick == 7:
                    voxel = Voxel(position=self.position + mouse.normal, texture=fire_texture)
                    voxel_interes = voxel.intersects()
                    collides = str(voxel_interes.entity.texture)
                    if collides == 'tnt_block.png':
                        tnt_position = voxel_interes.entity.position
                        destroy(voxel, delay=0.5)
                        destroy(voxel_interes.entity)
                        voxel1 = Voxel(position=tnt_position + LVector3f(0, 0, -1), texture = fire_texture)
                        voxel1_int = voxel1.intersects()
                        voxel11 = voxel1_int.entity

                        voxel2 = Voxel(position=tnt_position + LVector3f(-1, 0, 0), texture = fire_texture)
                        voxel2_int = voxel2.intersects()
                        voxel21 = voxel2_int.entity

                        voxel3 = Voxel(position=tnt_position + LVector3f(0, 0, 1), texture = fire_texture)
                        voxel3_int = voxel3.intersects()
                        voxel31 = voxel3_int.entity

                        voxel4 = Voxel(position=tnt_position + LVector3f(1, 0, 0), texture = fire_texture)
                        voxel4_int = voxel4.intersects()
                        voxel41 = voxel4_int.entity

                        voxel5 = Voxel(position=tnt_position + LVector3f(0, 0, 0), texture = fire_texture)
                        voxel5_int = voxel5.intersects()
                        voxel51 = voxel5_int.entity

                        voxel6 = Voxel(position=tnt_position + LVector3f(1, 0, 1), texture = fire_texture)
                        voxel6_int = voxel6.intersects()
                        voxel61 = voxel6_int.entity

                        voxel7 = Voxel(position=tnt_position + LVector3f(1, 0, -1), texture = fire_texture)
                        voxel7_int = voxel7.intersects()
                        voxel71 = voxel7_int.entity
                        
                        voxel8 = Voxel(position=tnt_position + LVector3f(-1, 0, 1), texture = fire_texture)
                        voxel8_int = voxel8.intersects()
                        voxel81 = voxel8_int.entity

                        voxel9 = Voxel(position=tnt_position + LVector3f(-1, 0, -1), texture = fire_texture)
                        voxel9_int = voxel9.intersects()
                        voxel91 = voxel9_int.entity

                        destroy(voxel11)
                        destroy(voxel21)
                        destroy(voxel31)
                        destroy(voxel41)
                        destroy(voxel51)
                        destroy(voxel61)
                        destroy(voxel71)
                        destroy(voxel81)
                        destroy(voxel91)


                        destroy(voxel1, delay=0.5)
                        destroy(voxel2, delay=0.5)
                        destroy(voxel3, delay=0.5)
                        destroy(voxel4, delay=0.5)
                        destroy(voxel5, delay=0.5)
                        destroy(voxel6, delay=0.5)
                        destroy(voxel7, delay=0.5)
                        destroy(voxel8, delay=0.5)
                        destroy(voxel9, delay=0.5)
                    if collides == 'water_block.png':
                        destroy(voxel, delay=0.5)
                        destroy(voxel_interes.entity, delay=0.5)
                    if collides == 'wood_block.png' or collides == 'tree_block.png':
                        destroy(voxel_interes.entity, delay=0.3)
                        v_minus(voxel=voxel)
                    if collides == 'sand_block.png':
                        print('make glass')
                        pos = (voxel.x, voxel.y - 1, voxel.z)
                        destroy(voxel, delay=0.3)
                        destroy(voxel_interes.entity, delay=0.3)
                        voxel = Voxel(position=pos, texture=glass_texture)
                if block_pick == 8:
                    voxel = Voxel(position=self.position + mouse.normal, texture=leaves_texture)
                if block_pick == 9:
                    voxel = Voxel(position=self.position + mouse.normal, texture=diamond_texture)
                if block_pick == 10:
                    slime_voxel = Voxel(position=self.position + mouse.normal, texture=slime_texture)
                    slime_number += 1
                if block_pick == 11:
                    if glass_forever:
                        voxel = Voxel(position=self.position + mouse.normal, texture=glass_texture)
                    else:
                        if glass_col > 0:
                            voxel = Voxel(position=self.position + mouse.normal, texture=glass_texture)
                            glass_col -= 1
                if block_pick == 12:
                    voxel = Voxel(position=self.position + mouse.normal, texture=sand_texture)
                if block_pick == 13:
                    voxel = Voxel(position=self.position + mouse.normal, texture=diamond_texture_2)
                if block_pick == 14:
                    voxel = Voxel(position=self.position + mouse.normal, texture=gold_texture_1)
                if block_pick == 15:
                    voxel = Voxel(position=self.position + mouse.normal, texture=gold_texture_2)
                if block_pick == 16:
                    if portal_state == 0:
                        voxel = Voxel(position=self.position + mouse.normal, texture=portal_texture)
                        portal_state = 1
                        print(1)
                        write_file('files/portal1.txt', str(list((int(self.position.x), int(self.position.z)))))
                        write_file('files/portal1_position_x.txt', f'{int(self.position.x)}')
                        write_file('files/portal1_position_z.txt', f'{int(self.position.z)}')
                        write_file('files/portal1_position_y.txt', f'{int(self.position.y)}')
                    elif portal_state == 1:
                        voxel = Voxel(position=self.position + mouse.normal, texture = portal_texture)
                        portal_state = 2
                        portal_ready = True
                        print(2)
                        write_file('files/portal2.txt', str(list((int(self.position.x), int(self.position.z)))))
                        write_file('files/portal2_position_x.txt', f'{int(self.position.x)}')
                        write_file('files/portal2_position_z.txt', f'{int(self.position.z)}')
                        write_file('files/portal2_position_y.txt', f'{int(self.position.y)}')
                    else:
                        print('no place')
                if block_pick == 17:
                    voxel = Voxel(position=self.position + mouse.normal, texture=tnt_texture)


            if key == 'right mouse down':
                if self.texture == portal_texture:
                    if portal_state == 2:
                        destroy(self)
                        portal_state = 1
                        portal_ready = False
                        index = 0
                    elif portal_state == 1:
                        destroy(self)
                        portal_state = 0
                        index = 0
                    else:
                        print('nope')
                elif self.texture == glass_texture:
                    destroy(self)
                    glass_col += 1
                else:
                    destroy(self)
            
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = load_texture('assets/skybox.png'),
            scale = 200,
            double_sided = True
        )
    
    def update(self):
        global start_time
        global sky_state
        global day_length
        global sunset_length

        time_ = time.time() - start_time
        # print(time_)
        if int(time_) > day_length - sunset_length:
            self.texture = load_texture('assets/sunset_skybox.jpg')

        if int(time_) > day_length:
            if sky_state == 1:
                sky_state = 2
                start_time = time.time()
                self.texture = load_texture('assets/night_skybox.jpg')
                player.cursor.color = color.white
            elif sky_state == 2:
                sky_state = 1
                start_time = time.time()
                self.texture = load_texture('assets/skybox.png')
                player.cursor.color = color.black

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = load_texture('assets/arm_texture.png'),
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.7, -0.6),
        )

    def active(self):
        self.position = Vec2(0.6, -0.5)

    def passive(self):
        self.position = Vec2(0.7, -0.6)

class YouDied(WindowPanel):
    def __init__(self):
        super().__init__(
            title='you died. play again',
            content=(
            Button(text = 'play', color = color.green, highlight_color = color.blue),
            ),
            popup = True,
        )
    
    def input(self, key):
        global enable_state
        if key == 'left mouse down':
            self.disable()
            enable_state = True
            player.position = (3, 23, 3)

class Show(Sprite):
    def __init__(self):
        super().__init__(
            texture = texture_image_path,
            parent = camera.ui,
            position = (0.8, 0.45),
            scale = 0.07
        )

class Trees():
    def __init__(self, number = 1):
        number_of_trees = number

        for i in range(number_of_trees):
            pos_x = random.randint(1, voxeles - 1)
            pos_z = random.randint(1, voxeles - 1)
            trunk_length = random.randint(3, 6)


            for trunk_part_int in range(0, trunk_length):
                trunk_part = Voxel(position=(pos_x, trunk_part_int + 13, pos_z), texture=tree_texture)
            for leave_int in range(11):
                if leave_int == 1:
                    leave = Voxel(position=(pos_x, trunk_length + 13, pos_z), texture=leaves_texture)
                if leave_int == 2:
                    leave = Voxel(position=(pos_x+1, trunk_length + 13, pos_z), texture=leaves_texture)
                if leave_int == 3:
                    leave = Voxel(position=(pos_x, trunk_length + 13, pos_z+1), texture=leaves_texture)
                if leave_int == 4:
                    leave = Voxel(position=(pos_x+1, trunk_length + 13, pos_z+1), texture=leaves_texture)
                if leave_int == 5:
                    leave = Voxel(position=(pos_x-1, trunk_length + 13, pos_z), texture=leaves_texture)
                if leave_int == 6:
                    leave = Voxel(position=(pos_x, trunk_length + 13, pos_z-1), texture=leaves_texture)
                if leave_int == 7:
                    leave = Voxel(position=(pos_x-1, trunk_length + 13, pos_z-1), texture=leaves_texture)
                if leave_int == 8:
                    leave = Voxel(position=(pos_x + 1, trunk_length + 13, pos_z - 1), texture=leaves_texture)
                if leave_int == 9:
                    leave = Voxel(position=(pos_x - 1, trunk_length + 13, pos_z + 1), texture=leaves_texture)
                if leave_int == 10:
                    leave = Voxel(position=(pos_x, trunk_length + 13 + 1, pos_z), texture=leaves_texture)

if ground_not_normal == True:
    for z in range(voxeles + 1):
        for x in range(voxeles + 1):
            for y in range(13):
                if y < stone_depth + 1:
                    voxel = Voxel(position = (x, y, z), texture=dirt_texture)
                elif y > stone_depth and y < 8:
                    if x > 1 and z > 1 or x < voxeles and z < voxeles:
                        if stone_choice == 1:
                            voxel = Voxel(position = (x, y, z), texture=diamond_texture)
                        else:
                            voxel = Voxel(position = (x, y, z), texture=gold_texture_1)
                    else:
                        voxel = Voxel(position = (x, y, z), texture=dirt_texture)
                elif y > 7 and y < 10:
                    voxel = Voxel(position = (x, y, z), texture=stone_texture)
                elif y > 9 and y < 12:
                    voxel = Voxel(position = (x, y, z), texture=dirt_texture)
                else:
                    if r_land == 1:
                        voxel = Voxel(position = (x, y, z))
                    else:
                        voxel = Voxel(position = (x, y, z), texture=sand_texture)
else:
    for z in range(voxeles + 1):
        for x in range(voxeles + 1):
            for y in range(13):
                if y < 12:
                    voxel = Voxel(position = (x, y, z), texture=dirt_texture)
                else:
                    voxel = Voxel(position = (x, y, z))

player = FirstPersonController()
player.position = (6, 23, 6)
player.cursor.color = color.black

sky = Sky()
hand = Hand()
show = Show()
trees_number = random.randint(2, 7)
trees = Trees(trees_number)


if how_many_sheeps > 0:
    for i in range(how_many_sheeps):
        r = random.randint(0, voxeles)
        sheep = Sheep(position=(r, 13, r))

app.run()