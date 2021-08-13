from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#equals
block_pick = 1
grass ="assets/img.png"
oke = "assets/img_1.png"
cobble = "assets/s.jpg"
wood_plank = "assets/img_2.png"
hand = "assets/img_8.png"
water = "assets/img_9.png"
hit = Audio("assets/minecraft_click.mp3")
dirt = "assets/dirt.jpg"
#update
def update():
    global block_pick
    if held_keys["left mouse"] or held_keys["right mouse"]:
        hit.play()
        arm.active()
    else:
        arm.passive()
    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4
    if held_keys['5']:
        block_pick = 5
    if held_keys['6']:
        block_pick = 6
#classes
 #blocks
class Arm(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "cube",
            texture = hand,
            scale = (0.2,0.2,1.7),
            rotation = Vec3(150,-15,0),
            position = Vec2(0.4,-0.6),
            color = color.white
        )
    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)
class Dirt(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = dirt,
            color = color.white,
            highlight_color = color.white66)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":


                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 2:
                    voxel = Voxel2(position=self.position + mouse.normal)
                if block_pick == 3:
                    voxel = Voxel22(position=self.position + mouse.normal)
                if block_pick == 4:
                    voxel = Voxel55(position=self.position + mouse.normal)
                if block_pick == 5:

                    voxel = Voxel25(position=self.position + mouse.normal)
                if block_pick == 6:
                    dirty = Dirt(position=self.position + mouse.normal)
                    

            if key == "right mouse down":
                    hit.play()
                    destroy(self)
class Voxel25(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = water,
            color = color.white66,
            highlight_color = color.white66)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":


                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 2:
                    voxel = Voxel2(position=self.position + mouse.normal)
                if block_pick == 3:
                    voxel = Voxel22(position=self.position + mouse.normal)
                if block_pick == 4:
                    voxel = Voxel55(position=self.position + mouse.normal)
                if block_pick == 5:

                    voxel = Voxel25(position=self.position + mouse.normal)
                if block_pick == 6:
                    dirty = Dirt(position=self.position + mouse.normal)
            if key == "right mouse down":
                    hit.play()
                    destroy(self)
class Voxel22(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = wood_plank,
            color = color.white,
            highlight_color = color.white66)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":

                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 2:
                    voxel = Voxel2(position=self.position + mouse.normal)
                if block_pick == 3:
                    voxel = Voxel22(position=self.position + mouse.normal)
                if block_pick == 4:
                    voxel = Voxel55(position=self.position + mouse.normal)
                if block_pick == 5:
                    voxel = Voxel25(position=self.position + mouse.normal)
                if block_pick == 6:
                    dirty = Dirt(position=self.position + mouse.normal)
            if key == "right mouse down":
                    destroy(self)
class Voxel2(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = oke,
            color = color.white,
            highlight_color = color.white66)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":

                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 2:
                    voxel = Voxel2(position=self.position + mouse.normal)
                if block_pick == 3:
                    voxel = Voxel22(position=self.position + mouse.normal)
                if block_pick == 4:
                    voxel = Voxel55(position=self.position + mouse.normal)
                if block_pick == 5:
                    voxel = Voxel25(position=self.position + mouse.normal)
                if block_pick == 6:
                    dirty = Dirt(position=self.position + mouse.normal)

            if key == "right mouse down":
                destroy(self)
class Voxel3(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = grass,
            color = color.white,
            highlight_color = color.white66)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":

                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 2:
                    voxel = Voxel2(position=self.position + mouse.normal)
                if block_pick == 3:
                    voxel = Voxel22(position=self.position + mouse.normal)
                if block_pick == 4:
                    voxel = Voxel55(position=self.position + mouse.normal)
                if block_pick == 5:
                    voxel = Voxel25(position=self.position + mouse.normal)
                if block_pick == 6:
                    dirty = Dirt(position=self.position + mouse.normal)

            if key == "right mouse down":
                destroy(self)
class Voxel55(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = hand,
            color = color.white,
            highlight_color = color.white66)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":

                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 2:
                    voxel = Voxel2(position=self.position + mouse.normal)
                if block_pick == 3:
                    voxel = Voxel22(position=self.position + mouse.normal)
                if block_pick == 4:
                    voxel = Voxel55(position=self.position + mouse.normal)
                if block_pick == 5:
                    voxel = Voxel25(position=self.position + mouse.normal)
                if block_pick == 6:
                    dirty = Dirt(position=self.position + mouse.normal)

            if key == "right mouse down":
                destroy(self)
class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = cobble,
            color = color.white,
            highlight_color = color.white66)

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":

                if block_pick == 1:
                    voxel = Voxel(position=self.position + mouse.normal)
                if block_pick == 2:
                    voxel = Voxel2(position=self.position + mouse.normal)
                if block_pick == 3:
                    voxel = Voxel22(position=self.position + mouse.normal)
                if block_pick == 4:
                    voxel = Voxel55(position=self.position + mouse.normal)
                if block_pick == 5:
                    voxel = Voxel25(position=self.position + mouse.normal)
                if block_pick == 6:
                    dirty = Dirt(position=self.position + mouse.normal)

            if key == "right mouse down":
                destroy(self)
 #background and styles
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = "assets/img_4.png",
			scale = 1000,
			double_sided = True)


#calling the classes
app = Ursina()
sky = Sky()
arm = Arm()
#creating the map
for z in range(27 ):
    for x in range(25):
        voxel = Voxel3(position = (x,0,z))
#setting to the window
player = FirstPersonController()
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = True
window.title = 'OkeCraft'
app.run()
