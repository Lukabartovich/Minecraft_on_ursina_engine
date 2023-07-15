import sqlite3
from ursina import *
from StringSort import StringSort

grass_texture = 'grass.png'
stone_texture = 'stone.png'
brick_texture = 'brick.png'
dirt_texture = 'dirt.png'
wood_texture = 'wood.png'
water_texture = 'water.jpg'
fire_texture = 'fire.jpg'
leaves_texture = 'leaves.png'
diamond_texture = 'diamond.jpg'
tnt_texture = 'the_tnt.jpg'
portal_texture = 'portal.jpg'
tree_texture = 'tree.png'
slime_texture = 'slime.png'
glass_texture = 'glass.png'
sand_texture = 'sand.jpg'
diamond_texture_2 = 'diamond2.jpg'
gold_texture_1 = 'gold1.jpg'
gold_texture_2 = 'gold2.jpg'
door_texture_1 = 'door1.jpg'
web_texture = 'web.png'
button_texture = 'button.png'
piston_texture = 'piston.png'

textures = [grass_texture, stone_texture, brick_texture,
            dirt_texture, wood_texture, water_texture,
            fire_texture, leaves_texture, diamond_texture,
            tnt_texture, portal_texture, slime_texture, 
            glass_texture, sand_texture, diamond_texture_2,
            gold_texture_1, gold_texture_2, door_texture_1,
            web_texture, button_texture, piston_texture]

block_pick = 0
block_pick_state = False

class Database:
    def __init__(self, texture):
        self.database = 'Minecraft_on_ursina_engine/files/database.db'
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.string = ''
        if str(texture) == grass_texture:
            self.string = 'grass'
        if str(texture) == stone_texture:
            self.string = 'stone'
        if str(texture) == brick_texture:
            self.string = 'brick'
        if str(texture) == dirt_texture:
            self.string = 'dirt'
        if str(texture) == wood_texture:
            self.string = 'wood'
        if str(texture) == water_texture:
            self.string = 'water'
        if str(texture) == fire_texture:
            self.string = 'fire'
        if str(texture) == leaves_texture:
            self.string = 'leaves'
        if str(texture) == sand_texture:
            self.string = 'sand'
        if str(texture) == glass_texture:
            self.string = 'glass'
        if str(texture) == slime_texture:
            self.string = 'slime'
        if str(texture) == tnt_texture:
            self.string = 'tnt'
        if str(texture) == portal_texture:
            self.string = 'portal'
        if str(texture) == diamond_texture:
            self.string = 'diamond'
        if str(texture) == diamond_texture_2:
            self.string = 'diamond_2'
        if str(texture) == gold_texture_1:
            self.string = 'gold_1'
        if str(texture) == gold_texture_2:
            self.string = 'gold_2'
        if str(texture) == door_texture_1:
            self.string = 'door'
        if str(texture) == web_texture:
            self.string = 'web'
        if str(texture) == button_texture:
            self.string = 'button'
        if str(texture) == piston_texture:
            self.string = 'piston'

    def get_position(self):
        str_x = f'SELECT "pos_x" from "blocks" WHERE "texture" = "{self.string}"'
        self.cursor.execute(str_x)
        x = self.cursor.fetchall()
        sx = StringSort(str(x))
        x = float(sx.delete("[(,)]"))
        str_y = f'SELECT "pos_y" from "blocks" WHERE "texture" = "{self.string}"'
        self.cursor.execute(str_y)
        y = self.cursor.fetchall()
        sy = StringSort(str(y))
        y = float(sy.delete("[(,)]"))
        return [x, y]

    def set_position(self, pos_x, pos_y, is_, one, two, three, four, five):
        string = f'UPDATE "blocks" SET "pos_x" = "{pos_x}" WHERE "texture" = "{self.string}"'
        string2 = f'UPDATE "blocks" SET "pos_y" = "{pos_y}" WHERE "texture" = "{self.string}"'
        string3 = f'UPDATE "blocks" SET "is" = "{is_}" WHERE "texture" = "{self.string}"'
        string4 = f'UPDATE "blocks" SET "1" = "{one}" WHERE "texture" = "{self.string}"'
        string5 = f'UPDATE "blocks" SET "2" = "{two}" WHERE "texture" = "{self.string}"'
        string6 = f'UPDATE "blocks" SET "3" = "{three}" WHERE "texture" = "{self.string}"'
        string7 = f'UPDATE "blocks" SET "4" = "{four}" WHERE "texture" = "{self.string}"'
        string8 = f'UPDATE "blocks" SET "5" = "{five}" WHERE "texture" = "{self.string}"'
        self.connection.execute(string)
        self.connection.execute(string2)
        self.connection.execute(string3)
        self.connection.execute(string4)
        self.connection.execute(string5)
        self.connection.execute(string6)
        self.connection.execute(string7)
        self.connection.execute(string8)
        self.connection.commit()

    def get_is(self):
        str_is = f'SELECT "is" from "blocks" WHERE "texture" = "{self.string}"'
        self.cursor.execute(str_is)
        s_is = self.cursor.fetchall()
        is_s = StringSort(str(s_is))
        is_ = bool(is_s.delete("[(,)]"))
        return is_

    
    def get_is_num(self, number):
        global textures
        global block_pick
        global block_pick_state

        string = f'SELECT "texture" from "blocks" where "{number}" = "True"'
        self.cursor.execute(string)
        is_num = self.cursor.fetchall()
        s = StringSort(str(is_num))
        is_num = s.delete("[(,')]")
        texture = is_num
        if texture == 'grass':
            block_pick = 1
            block_pick_state = True
        elif texture == 'dirt':
            block_pick = 4
            block_pick_state = True
        elif texture == 'glass':
            block_pick = 11
            block_pick_state = True
        elif texture == 'stone':
            block_pick = 2
            block_pick_state = True
        elif texture == 'brick':
            block_pick = 3
            block_pick_state = True
        elif texture == 'wood':
            block_pick = 5
            block_pick_state = True
        elif texture == 'water':
            block_pick = 6
            block_pick_state = True
        elif texture == 'fire':
            block_pick = 7
            block_pick_state = True
        elif texture == 'leaves':
            block_pick = 8
            block_pick_state = True
        elif texture == 'diamond':
            block_pick = 9
            block_pick_state = True
        elif texture == 'diamond_2':
            block_pick = 13
            block_pick_state = True
        elif texture == 'tnt':
            block_pick = 17
            block_pick_state = True
        elif texture == 'slime':
            block_pick = 10
            block_pick_state = True
        elif texture == 'sand':
            block_pick = 12
            block_pick_state = True
        elif texture == 'gold_1':
            block_pick = 14
            block_pick_state = True
        elif texture == 'gold_2':
            block_pick = 15
            block_pick_state = True
        elif texture == 'door':
            block_pick = 18
            block_pick_state = True
        elif texture == 'web':
            block_pick = 19
            block_pick_state = True
        elif texture == 'button':
            block_pick = 20
            block_pick_state = True
        elif texture == 'piston':
            block_pick = 21
            block_pick_state = True

        return block_pick
    
