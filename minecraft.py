from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from database_class import Database

from file_opener import *
# from sheep_file import *

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
door_texture_1 = load_texture('assets/door_block_1.png')
door_texture_2 = load_texture('assets/door_block_2.png')
web_texture = load_texture('assets/web_block.png')

block_pick = 1
enable_state = True
fly_state = True
fly_hight = 25

voxeles = 15
max_blocks = 20

super_speed = 10
super_jump = 10

texture_image_path = 'assets/grass.png'

portal_state = 0
portal_ready = False

portal_number = 0
migration = 0

slime_number = 0

index = 0

day_length = 60
sunset_length = 25

sky_state = 1

super_fly_hight = 1

glass_col = 0
glass_forever = True

falling_limit = -30

ground_not_normal = False
stone_depth = random.randint(3, 6)
stone_choice = random.randint(1, 2)
r_land = random.randint(1, 2)

sheep_wait = 2
sheep_lives = 2
sheep_speed = 1
state = ''
start_time = time.time()
red_start_time = time.time()
sheep_leaves = 0
sheep_spawn_leaves = 0
new_sheep_time_start = time.time()
sheep_spawn = False
how_many_sheeps = 0

axe_state = False
sword_state = False
green_sword_state = False

cursor_color = color.black

texture_col = 0

posx = 0.0
posy = -0.0

inventory_open = False
inventory_o = False
inv_col = 0

third_state = False
t_s = False

textures = [grass_texture, stone_texture, brick_texture,
            dirt_texture, wood_texture, water_texture,
            fire_texture, leaves_texture, diamond_texture,
            tnt_texture, portal_texture, slime_texture, 
            glass_texture, sand_texture, diamond_texture_2,
            gold_texture_1, gold_texture_2, door_texture_1,
            web_texture]

sword_textures = [load_texture('assets/wood_sword_texture.png'),
                    load_texture('assets/diamond_sword_texture.png'),
                    load_texture('assets/green_sword_texture.png')]

sword_num = 0

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
    global super_fly_hight
    global axe_state
    global sword_state
    global inventory_o
    global inventory_open
    global inv_col
    global enable_state
    global textures
    global sheep_spawn
    global third_state
    global green_sword_state
    global sword_textures
    global sword_num

    # if key == 't':
        # if third_state == False:
        #     third_state = True
        # else:
        #     third_state = False
    
    if key == '.' or key == '. hold':
        if sword_state == True:
            if sword_num < len(sword_textures) - 1:
                sword_num += 1
                sword.texture = sword_textures[sword_num]
    if key == ',' or key == ', hold':
        if sword_state == True:
            if sword_num > 0:
                sword_num -= 1
                sword.texture = sword_textures[sword_num]

    if key == 'f':
        if fly_state == False:
            fly_state = True
        else:
            fly_state = False

    if fly_state == True:
        if key == 'up arrow' or key == 'up arrow hold':
            fly_hight += super_fly_hight
            # print('up')
        if key == 'down arrow' or key == 'down arrow hold':
            fly_hight -= super_fly_hight
            # print('down')

    if key == 'i':
        if inv_col == 0:
            inv_col = 1
        else:
            inventory_open = True
        if inventory_o == False:
            inventory_o = True
        else:
            inventory_o = False

    if inventory_o == False:
        bg.disable()
        inventary.disable()
        enable_state = True
    else:
        bg.enable()
        inventary.enable()
        enable_state = False

    if key == 'o':
        if sword_state == False:
            sword_state = True
            axe_state = False
        else:
            sword_state = False
    if key == 'p':
        if axe_state == False:
            axe_state = True
            sword_state = False
        else:
            axe_state = False

    if axe_state == True:
        axe.enable()
        sword.disable()
    else:
        axe.disable()

    if sword_state == True:
        sword.enable()
        axe.disable()
    else:
        sword.disable()

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

    if key == '1':
        db = Database(glass_texture)
        block_pick = db.get_is_num(1)
    if key == '2':
        db = Database(glass_texture)
        block_pick = db.get_is_num(2)
    if key == '3':
        db = Database(glass_texture)
        block_pick = db.get_is_num(3)
    if key == '4':
        db = Database(glass_texture)
        block_pick = db.get_is_num(4)
    if key == '5':
        db = Database(glass_texture)
        block_pick = db.get_is_num(5)

def update():
    global block_pick
    global enable_state
    global fly_state
    global index
    global migration
    global sheep_spawn
    global sheep_lives
    global new_sheep_time_start
    global sheep_leaves
    global sheep_spawn_leaves
    global super_fly_hight
    global cursor_color
    global third_state
    global t_s

    # if third_state == True:
    #     steve.enable()
    #     steve.origin = (0, -15, -10)
    #     steve.parent = player
    #     # print(player.camera_pivot.z, player.camera_pivot.y)
    #     player.camera_pivot.z = -3.5
    #     player.camera_pivot.y = 3.5
    #     t_s = False
    # else:
    #     steve.disable()
    #     steve.parent = scene
    #     player.camera_pivot.z = 0
    #     player.camera_pivot.y = 2

    hovered_voxel = mouse.hovered_entity
    if hovered_voxel:
        if hovered_voxel.texture == leaves_texture:
            player.cursor.color = color.white
        else:
            player.cursor.color = cursor_color
    else:
            player.cursor.color = cursor_color

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
    if block_pick == 18:
        show.texture = 'assets/door1.jpg'
    if block_pick == 19:
        show.texture = 'assets/web.png'

    if player.position.y < falling_limit:
        player.position = (3, 23, 3)
        YouDied()
        enable_state = False

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
        axe.active()
        sword.active()
    else:
        hand.passive()
        axe.passive()
        sword.passive()

    if sheep_spawn == True:
        if how_many_sheeps > 0:
            time_  = time.time() - new_sheep_time_start
            if time_ > random.randint(10, 60):
                sheep = Sheep(position = (random.randint(0, voxeles - 1), 13, random.randint(0, voxeles - 1)))
                sheep_spawn = False
                new_sheep_time_start = time.time()
                sheep_lives = 2
    if sheep_spawn_leaves == True:
        sheep = Sheep(position=(random.randint(0, voxeles - 1), 13, random.randint(0, voxeles - 1)))
        sheep_spawn_leaves = False

    if held_keys['left control']:
        player.speed = super_speed
        player.jump_height = super_jump
        super_fly_hight = 5
    else:
        player.speed = 5
        player.jump_height = 2
        super_fly_hight = 1
        
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
            scale = 0.5,
            )
        
    door_state = True
    door_where = ''
    pos_door = ()

    def input(self, key):
        global texture_image_path
        global portal_state
        global portal_ready
        global slime_number
        global glass_col
        global glass_forever
        global block_pick
        global axe_state
        global sword_state
        global sword_num
        global sword_textures

        if self.hovered:
            if key == 'left mouse down':
                if self.texture == door_texture_1:
                    door_sigment_2 = self.intersects().entity
                    door_sigment_1 = self.intersects().entities
                    for vox in door_sigment_1:
                        if vox.texture == door_texture_2:
                            door_sigment_2 = vox
                    x = mouse.normal.x
                    z = mouse.normal.z
                    # print(x, z)
                    if self.door_state == True:
                        if self.door_where == '':
                            self.pos_door = self.position
                            if x == 0 and z == -1:
                                if self.door_where == '':
                                    self.door_where = '1'
                                self.z -= 1
                                self.x -= 1
                                door_sigment_2.z -= 1
                                door_sigment_2.x -= 1
                                self.door_state = False
                            if x == -1 and z == 0:
                                if self.door_where == '':
                                    self.door_where = '2'
                                self.z += 1
                                self.x -= 1
                                door_sigment_2.z += 1
                                door_sigment_2.x -= 1
                                self.door_state = False
                            if x == 0 and z == 1:
                                if self.door_where == '':
                                    self.door_where = '3'
                                self.z += 1
                                self.x += 1
                                door_sigment_2.z += 1
                                door_sigment_2.x += 1
                                self.door_state = False
                            if x == 1 and z == 0:
                                if self.door_where == '':
                                    self.door_where = '4'
                                self.z -= 1
                                self.x += 1
                                door_sigment_2.z -= 1
                                door_sigment_2.x += 1
                                self.door_state = False
                        else:
                            if self.door_where == '1':
                                # print(1)
                                self.z -= 1
                                self.x -= 1
                                door_sigment_2.z -= 1
                                door_sigment_2.x -= 1
                                self.door_state = False
                            if self.door_where == '2':
                                # print(2)
                                self.z += 1
                                self.x -= 1
                                door_sigment_2.z += 1
                                door_sigment_2.x -= 1
                                self.door_state = False
                            if self.door_where == '3':
                                # print(3)
                                self.z += 1
                                self.x += 1
                                door_sigment_2.z += 1
                                door_sigment_2.x += 1
                                self.door_state = False
                            if self.door_where == '4':
                                # print(4)
                                self.z -= 1
                                self.x += 1
                                door_sigment_2.z -= 1
                                door_sigment_2.x += 1
                                self.door_state = False

                    elif self.door_state == False:
                        self.position = self.pos_door
                        pos = (self.x, self.y-1, self.z)
                        door_sigment_2.position = pos
                        self.door_state = True

                else:
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
                    if block_pick == 18:
                        
                        # print(int(player.cursor.get_position()))
                        voxel1 = Voxel(position=self.position + mouse.normal, texture=door_texture_2)
                        pos = (voxel1.x, voxel1.y + 1, voxel1.z)
                        voxel2 = Voxel(position=pos, texture=door_texture_1)
                    if block_pick == 19:
                        voxel = Voxel(position=self.position + mouse.normal, texture=web_texture)

            if key == 'right mouse down':
                if axe_state or str(sword_textures[sword_num]) == 'green_sword_texture.png':
                    texture = grass_texture
                    i_ = self.intersects().entities
                    for i in i_:
                        if i.position == self.position - mouse.normal:
                            # print(i.texture)
                            vox = i
                            texture = i.texture
                            destroy(vox, delay=0.15)
                    if texture == grass_texture:
                        texture = self.texture
                    if texture == grass_texture:
                        destroy(self)
                        block_pick = 1
                        # print('lol')
                    elif texture == dirt_texture:
                        destroy(self)
                        block_pick = 4
                    elif texture == glass_texture:
                        destroy(self)
                        block_pick = 11
                    elif texture == stone_texture:
                        destroy(self)
                        block_pick = 2
                    elif texture == brick_texture:
                        destroy(self)
                        block_pick = 3
                    elif texture == wood_texture:
                        destroy(self)
                        block_pick = 5
                    elif texture == water_texture:
                        destroy(self)
                        block_pick = 6
                    elif texture == fire_texture:
                        destroy(self)
                        block_pick = 7
                    elif texture == leaves_texture:
                        destroy(self)
                        block_pick = 8
                    elif texture == diamond_texture:
                        destroy(self)
                        block_pick = 9
                    elif texture == diamond_texture_2:
                        destroy(self)
                        block_pick = 13
                    elif texture == tnt_texture:
                        destroy(self)
                        block_pick = 17
                    elif texture == slime_texture:
                        destroy(self)
                        block_pick = 10
                    elif texture == sand_texture:
                        destroy(self)
                        block_pick = 12
                    elif texture == gold_texture_1:
                        destroy(self)
                        block_pick = 14
                    elif texture == gold_texture_2:
                        destroy(self)
                        block_pick = 15
                    elif texture == door_texture_1:
                        door_sigment_1 = self.intersects().entities
                        for vox in door_sigment_1:
                            if vox.texture == door_texture_2:
                                if vox.y == self.y - 1:
                                    v = vox
                        try:
                            destroy(v)
                            destroy(self)
                            block_pick = 18
                            door_state = True
                        except:
                            destroy(self)
                    elif self.texture == web_texture:
                        destroy(self)
                        block_pick = 19
                    else:
                        destroy(self)
                else:
                    if self.texture == portal_texture:
                        block_pick = 16
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
                    elif self.texture == grass_texture:
                        destroy(self)
                        block_pick = 1
                        # print('lol')
                    elif self.texture == dirt_texture:
                        destroy(self)
                        block_pick = 4
                    elif self.texture == glass_texture:
                        destroy(self)
                        block_pick = 11
                    elif self.texture == stone_texture:
                        if str(sword_textures[sword_num]) == 'wood_sword_texture.png' and sword_state == True:
                            sword_state = False
                        else:
                            destroy(self)
                            block_pick = 2
                    elif self.texture == brick_texture:
                        if str(sword_textures[sword_num]) == 'wood_sword_texture.png' and sword_state == True:
                            sword_state = False
                        else:
                            destroy(self)
                            block_pick = 3
                    elif self.texture == wood_texture:
                        destroy(self)
                        block_pick = 5
                    elif self.texture == water_texture:
                        destroy(self)
                        block_pick = 6
                    elif self.texture == fire_texture:
                        destroy(self)
                        block_pick = 7
                    elif self.texture == leaves_texture:
                        destroy(self)
                        block_pick = 8
                    elif self.texture == diamond_texture:
                        if str(sword_textures[sword_num]) == 'wood_sword_texture.png' and sword_state == True:
                            sword_state = False
                        else:
                            destroy(self)
                            block_pick = 9
                    elif self.texture == diamond_texture_2:
                        if str(sword_textures[sword_num]) == 'wood_sword_texture.png' and sword_state == True:
                            sword_state = False
                        else:
                            destroy(self)
                            block_pick = 13
                    elif self.texture == tnt_texture:
                        destroy(self)
                        block_pick = 17
                    elif self.texture == slime_texture:
                        destroy(self)
                        block_pick = 10
                    elif self.texture == sand_texture:
                        destroy(self)
                        block_pick = 12
                    elif self.texture == gold_texture_1:
                        if str(sword_textures[sword_num]) == 'wood_sword_texture.png' and sword_state == True:
                            sword_state = False
                        else:
                            destroy(self)
                            block_pick = 14
                    elif self.texture == gold_texture_2:
                        destroy(self)
                        block_pick = 15
                    elif self.texture == door_texture_1:
                        door_sigment_1 = self.intersects().entities
                        for vox in door_sigment_1:
                            if vox.texture == door_texture_2:
                                if vox.y == self.y - 1:
                                    v = vox
                        try:
                            destroy(v)
                            destroy(self)
                            block_pick = 18
                            door_state = True
                        except:
                            destroy(self)
                    elif self.texture == web_texture:
                        destroy(self)
                        block_pick = 19
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
        global cursor_color

        time_ = time.time() - start_time
        # print(time_)
        if int(time_) > day_length - sunset_length:
            self.texture = load_texture('assets/sunset_skybox.jpg')

        if int(time_) > day_length:
            if sky_state == 1:
                sky_state = 2
                start_time = time.time()
                self.texture = load_texture('assets/night_skybox.jpg')
                cursor_color = color.white
                player.cursor.color = cursor_color
            elif sky_state == 2:
                sky_state = 1
                start_time = time.time()
                self.texture = load_texture('assets/skybox.png')
                cursor_color = color.black
                player.cursor.color = cursor_color

class Sheep(Button):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = load_texture('assets/sheep_block2.png'),
            color = color.color(0, 0, random.uniform(0.9, 1)),
            scale = 0.5,
            rotation = Vec3(0, 180, 0),
        )
    
    def update(self):
        global sheep_speed
        global start_time
        global sheep_wait
        global sheep_lives
        global new_sheep_time_start
        global sheep_spawn
        global sheep_spawn_leaves
        global sheep_leaves
        global state
        global axe_state

        origin = self.world_position + (self.up)

        hit_info = raycast(origin=origin, direction=self.rotation_directions,
                            ignore=(self,), distance=.5, debug=False)
        
        time_ = time.time() - start_time
        if time_ >= sheep_wait:
            where = random.randint(1, 4)
            state = ''
            if where == 1:
                if self.x < voxeles:
                    if hit_info.hit == False:
                        self.rotation = Vec3(0, 180, 0)
                        self.x += sheep_speed
                        state = 'x+'
                        start_time = time.time()

            if where == 2:
                if self.x > 1:
                    if hit_info.hit == False:
                        self.rotation = Vec3(0, 360, 0)
                        self.x -= sheep_speed
                        state = 'x-'
                        start_time = time.time()
                
            if where == 3:
                if self.z < voxeles:
                    if hit_info.hit == False:
                        self.rotation = Vec3(0, 90, 0)
                        self.z += sheep_speed
                        state = 'z+'
                        start_time = time.time()

            if where == 4:
                if self.z > 1:
                    if hit_info.hit == False:
                        self.rotation = Vec3(0, 270, 0)
                        self.z -= sheep_speed
                        state = 'z-'
                        start_time = time.time()


        if hit_info.hit:
            if str(hit_info.entity.texture) == 'leaves_block.png':
                destroy(hit_info.entity)
                sheep_leaves += 1
                sheep_spawn_leaves = True
            else:
                pos = hit_info.entity.position
                pos_x = pos[0]
                pos_y = 13
                pos_z = pos[2]
                if state == 'x+':
                    self.position = Vec3(pos_x - 1, pos_y, pos_z)
                if state == 'x-':
                    self.position = Vec3(pos_x + 1, pos_y, pos_z)
                if state == 'z+':
                    self.position = Vec3(pos_x, pos_y, pos_z - 1)
                if state == 'z-':
                    self.position = Vec3(pos_x, pos_y, pos_z + 1)
        else:
            sheep_speed = 1

    def input(self, key):
        global sheep_lives
        global red_start_time
        global new_sheep_time_start
        global sheep_spawn
        global sword_textures
        global sword_num

        if key == 'right mouse down':
            if self.hovered:
                if axe_state or str(sword_textures[sword_num]) == 'diamond_sword_texture.png' \
                    or str(sword_textures[sword_num]) == 'green_sword_texture.png':
                    destroy(self)
                    destroy(self)
                    sheep_spawn = True
                    new_sheep_time_start = time.time()
                    sheep_lives = 2
                if sheep_lives == 1:
                    self.texture = load_texture('assets/red_sheep_block3.png')
                    sheep_lives -= 1
                elif sheep_lives == 2:
                    self.texture = load_texture('assets/red_sheep_block1.png')
                    sheep_lives -= 1
                else:
                    destroy(self)
                    sheep_spawn = True
                    new_sheep_time_start = time.time()
                    sheep_lives = 2

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

class Pickaxe(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/Diamond-Pickaxe',
            texture = load_texture('assets/diamond_axe_tex.png'),
            scale = 0.03,
            # rotation = Vec3(150, -10, 0),
            rotation = Vec3(150, 150, -90),
            position = Vec2(0.45, -0.1),
        )

    def active(self):
        self.position = Vec2(0.35, 0)
        self.rotation = Vec3(110, 150, -90)

    def passive(self):
        self.position = Vec2(0.45, -0.1)
        self.rotation = Vec3(150, 150, -90)

class Sword(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets\DiamondSword',
            texture = sword_textures[0],
            scale = 0.023,
            # rotation = Vec3(150, -10, 0),
            rotation = Vec3(70, 150, -90),
            position = Vec2(0.45, -0.05),
        )

    def active(self):
        self.position = Vec2(0.35, 0.05)
        self.rotation = Vec3(30, 150, -90)

    def passive(self):
        self.position = Vec2(0.45, -0.05)
        self.rotation = Vec3(70, 150, -90)

class YouDied(WindowPanel):
    def __init__(self):
        super().__init__(
            title='you died. play again',
            color=color.red,
            content=(
            ),
            popup = True,
        )
    
    def input(self, key):
        global enable_state
        if key == 'left mouse down':
            if self.hovered:
                self.disable()
                enable_state = True
                player.position = (3, 23, 3)
            else:
                enable_state = False
    
    def update(self):
        if self.hovered:
            self.color = color.green
        else:
            self.color = color.red

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

class BG(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (0.56, 0.86),
            texture = load_texture('bg_2.png'),
            render_order = 0
        )

class Item(Draggable):
    def __init__(self, contaner, type):
        super().__init__(
            parent = contaner,
            model = 'quad',
            texture = type,
            color = color.white,
            scale = (0.1, 0.1),
            scale_x = 1 / (contaner.texture_scale[0] * 1.2),
            scale_y = 1 / (contaner.texture_scale[1] * 1.2),
            origin = (-0.6, 0.6),
            render_order = 1
        )

    state = False

    def drag(self):
        self.xy_pos = [self.x, self.y]
        self.render_order = 1

    def drop(self):
        self.x = int((self.x + self.scale_x/2) * 5) / 5
        self.y = int((self.y - self.scale_y/2) * 8) / 8

        x_ = float(str(self.x)[0:4])
        y_ = float(str(self.y)[0:4])

        if y_ == -0.8:
            if x_ == 0:
                db = Database(self.texture)
                # print(self.texture)
                db.set_position(x_, y_, True, True, False, False, False, False)
            if x_ == 0.2:
                db = Database(self.texture)
                db.set_position(x_, y_, True, False, True, False, False, False)
            if x_ == 0.4:
                db = Database(self.texture)
                db.set_position(x_, y_, True, False, False, True, False, False)
            if x_ == 0.6:
                db = Database(self.texture)
                db.set_position(x_, y_, True, False, False, False, True, False)
            if x_ == 0.8:
                db = Database(self.texture)
                db.set_position(x_, y_, True, False, False, False, False, True)
        else:
            db = Database(self.texture)
            db.set_position(x_, y_, False, False, False, False, False, False)

        print(self.y)
        self.constrait()

    def constrait(self):
        if self.x < 0 or self.x > 1 or self.y > 0 or self.y < -1:
            self.x = self.xy_pos[0]
            self.y = self.xy_pos[1]

class Grid(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = load_texture('item_bg.png'),
            texture_scale = (5, 8),
            scale=(0.5, 0.8),
            origin = (-0.5, 0.5),
            position = (-0.25, 0.4)
        )
        self.import_textures()
        self.add_new_item()

    def add_new_item(self):
        global texture_col
        global posx
        global posy

        if inventory_open:
            for i in range(len(self.textures)):   
                d = Database(self.textures[i])
                xy = d.get_position()
                is_ = d.get_is()
                # print(xy)
                item = Item(self, self.textures[i])
                item.drag()
                item.x = xy[0]
                item.y = xy[1]
                if is_:
                    print('is')
                item.drop()
        else:
            for i in range(len(self.textures)):
                item = Item(self, self.textures[i])
                print(item.texture)
                # print(item.texture)
                if posx == 1:
                    posx = 0.0
                    posy -= 0.1
                if float(str(posy)[0:4]) == -0.3:
                    posy = -0.4
                item.x = posx
                item.y = posy
                item.drag()
                item.drop()
                posx += 0.2
                # print(float(str(posy)[0:4]))

    def import_textures(self):
        grass_texture = load_texture('assets/grass.png')
        stone_texture = load_texture('assets/stone.png')
        brick_texture = load_texture('assets/brick.png')
        dirt_texture = load_texture('assets/dirt.png')
        wood_texture = load_texture('assets/wood.png')
        water_texture = load_texture('assets/water.jpg')
        fire_texture = load_texture('assets/fire.jpg')
        leaves_texture = load_texture('assets/leaves.png')
        diamond_texture = load_texture('assets/diamond.jpg')
        tnt_texture = load_texture('assets/the_tnt.jpg')
        portal_texture = load_texture('assets/portal.jpg')
        slime_texture = load_texture('assets/slime.png')
        glass_texture = load_texture('assets/glass.png')
        sand_texture = load_texture('assets/sand.jpg')
        diamond_texture_2 = load_texture('assets/diamond2.jpg')
        gold_texture_1 = load_texture('assets/gold1.jpg')
        gold_texture_2 = load_texture('assets/gold2.jpg')
        door_texture_1 = load_texture('assets/door1.jpg')
        web_texture = load_texture('assets/web.png')

        self.textures = [grass_texture, stone_texture, brick_texture,
                         dirt_texture, wood_texture, water_texture,
                         fire_texture, leaves_texture, diamond_texture,
                         tnt_texture, portal_texture, slime_texture, 
                         glass_texture, sand_texture, diamond_texture_2,
                         gold_texture_1, gold_texture_2, door_texture_1,
                         web_texture]
      

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
axe = Pickaxe()
axe.disable()

sword = Sword()
sword.disable()

bg = BG()
bg.disable()
inventary = Grid()
inventary.disable()

if how_many_sheeps > 0:
    for i in range(how_many_sheeps):
        r = random.randint(0, voxeles)
        sheep = Sheep(position=(r, 13, r))

app.run()