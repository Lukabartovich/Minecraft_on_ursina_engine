from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


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

block_pick = 1
enable_state = True
fly_state = True
fly_hight = 25

voxeles = 15
max_blocks = 12

super_speed = 10
super_jump = 10

sheep_speed = 1
how_many_sheeps = 0

texture_image_path = 'assets/grass.png'

portal_state = 0
portal_ready = False

portal_number = 0
migration = 0

index = 0

def open_file(file_path: str):
    with open(str(file_path), 'r+') as file:
        file_text = file.read()
    return file_text

def write_file(file_path: str, text: str):
    with open(str(file_path), 'w+') as file:
        file.truncate(0)
        file.write(text) 

def input(key):
    global fly_state
    global max_blocks
    global block_pick

    if key == 'f':
        if fly_state == False:
            fly_state = True
        else:
            fly_state = False

    if key == 'b':
        show = Show()
        block_pick = 1
        show.texture = 'assets/grass.png'

    if key == 'right arrow up' or key == 'right arrow hold' or key == 'scroll down':
        if block_pick < max_blocks - 1:
            block_pick += 1
        else:
            block_pick = max_blocks - 1

    if key == 'left arrow up' or key == 'left arrow hold' or key == 'scroll up': 
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
        show.texture =  'assets/the_tnt.jpg'
    if block_pick == 11:
        show.texture = 'assets/portal.jpg'

    if player.position.y < 0:
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


    if portal_ready == True:
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
                player.x = position_x
                player.z = position_z
                migration = 1
            if index == 2:
                position_x = int(open_file('files/portal1_position_x.txt'))
                position_z = int(open_file('files/portal1_position_z.txt'))
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
                        destroy(voxel, delay=0.7)
                        destroy(water_collide.entity, delay=0.7)
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
                        destroy(voxel, delay=0.7)
                        destroy(voxel_interes.entity, delay=0.7)
                if block_pick == 8:
                    voxel = Voxel(position=self.position + mouse.normal, texture=leaves_texture)
                if block_pick == 9:
                    voxel = Voxel(position=self.position + mouse.normal, texture=diamond_texture)
                if block_pick == 10:
                    voxel = Voxel(position=self.position + mouse.normal, texture=tnt_texture)
                if block_pick == 11:
                    if portal_state == 0:
                        voxel = Voxel(position=self.position + mouse.normal, texture=portal_texture)
                        portal_state = 1
                        print(1)
                        write_file('files/portal1.txt', str(list((int(self.position.x), int(self.position.z)))))
                        write_file('files/portal1_position_x.txt', f'{int(self.position.x)}')
                        write_file('files/portal1_position_z.txt', f'{int(self.position.z)}')
                    elif portal_state == 1:
                        voxel = Voxel(position=self.position + mouse.normal, texture = portal_texture)
                        portal_state = 2
                        portal_ready = True
                        print(2)
                        write_file('files/portal2.txt', str(list((int(self.position.x), int(self.position.z)))))
                        write_file('files/portal2_position_x.txt', f'{int(self.position.x)}')
                        write_file('files/portal2_position_z.txt', f'{int(self.position.z)}')
                    else:
                        print('no place')

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

class Sheep(Entity):
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

        origin = self.world_position + (self.up)

        hit_info = raycast(origin=origin, direction=self.rotation_directions,
                            ignore=(self,), distance=.5, debug=False)
        


        where = random.randint(1, 4)
        if where == 1:
            if self.x < voxeles:
                if hit_info.hit == False:
                    self.rotation = Vec3(0, 180, 0)
                    self.x += sheep_speed
                    self.state = 'x+'

        if where == 2:
            if self.x > 1:
                if hit_info.hit == False:
                    self.rotation = Vec3(0, 360, 0)
                    self.x -= sheep_speed
                    self.state = 'x-'
            
        if where == 3:
            if self.z < voxeles:
                if hit_info.hit == False:
                    self.rotation = Vec3(0, 90, 0)
                    self.z += sheep_speed
                    self.state = 'z+'

        if where == 4:
            if self.z > 1:
                if hit_info.hit == False:
                    self.rotation = Vec3(0, 270, 0)
                    self.z -= sheep_speed
                    self.state = 'z-'

        if hit_info.hit:
            if str(hit_info.entity.texture) == 'leaves_block.png':
                destroy(hit_info.entity)
            else:
                pos = hit_info.entity.position
                pos_x = pos[0]
                pos_y = 13
                pos_z = pos[2]
                print(pos_x)
                if self.state == 'x+':
                    self.position = Vec3(pos_x - 1, pos_y, pos_z)
                if self.state == 'x-':
                    self.position = Vec3(pos_x + 1, pos_y, pos_z)
                if self.state == 'z+':
                    self.position = Vec3(pos_x, pos_y, pos_z - 1)
                if self.state == 'z-':
                    self.position = Vec3(pos_x, pos_y, pos_z + 1)
        else:
            sheep_speed = 1

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
if how_many_sheeps > 0:
    for i in range(how_many_sheeps):
        r = random.randint(0, voxeles)
        sheep = Sheep(position=(r, 13, r))

app.run()