from ursina import *

title='macOS X Sonoma 14.43 VM lts'
icon='logos/mac-os-logo.png'

app = Ursina(
	borderless=False,
	title=title,
	icon=icon,
	)

def input(self, key):
	if self.hovered:
		if key == 'left mouse down':
			print("left mouse down")

window.cog_menu.enabled = False
# icon references
#	ranksol graphics - os.png
#	Freepik - mac-os-logo.png
#	Freepik - windows.png
#	Freepik - folder.png
#	Ppangman - arrows.png

class ICON(Button):
	def __init__(self):
		self.icon()

	def icon(self, position=(-7.09,4.54,0)):
		super().__init__(
				parent=scene,
				position=position,
				model='quad',
				color=color.white,
				texture='logos/mac-os-logo.png',
				highlight_color=color.light_gray,
				scale=0.3,
			)

class DOCK_BAR(Button):
	def __init__(self):
		self.dock_bar()

	def dock_bar(self, position=(0,-4.15,0.1)):
		super().__init__(
				parent=scene,
				position=position,
				model='quad',
				color=color.white,
				scale=1,
				scale_x=8,
			)

class WindowMGR(Entity):
	def __init__(self):
		self.window()

	def window(self, position=(0,0,0)):
		super().__init__(
				parent=scene,
				position=position,
				model='quad',
				color=color.white,
				scale=5,
				scale_y=2,
				scale_x=5
			)

class BACKGROUND(Entity):
	def __init__(self):
		self.background()

	def background(self, position=(0,0,0.2)):
		super().__init__(
				parent=scene,
				position=position,
				model='quad',
				texture=load_texture('textures/bgs/default-bg.png'),
				scale=10,
			)

class CONSOLE(Entity):
	def __init__(self):
		self.console()

	def console(self, position=(-3.4,-4.14,0)):
		super().__init__(
				parent=scene,
				position=position,
				model='quad',
				texture=load_texture('textures/icons/console.png'),
				highlight_color=color.light_gray,
			)

class FINDER(Entity):
	def __init__(self, position=(-2.2,-4.14,0)):
		super().__init__(
				parent=scene,
				position=position,
				model='quad',
				texture=load_texture('textures/icons/folder.png'),
				highlight_color=color.light_gray,
			)

class TEXT_EDIT(Entity):
	def text_edit(self, position=(0,-4.14,0)):
			super().__init__(
					parent=scene,
					position=position,
					model='quad',
					texture=load_texture('textures/icons/arrows.png'),
					highlight_color=color.light_gray,
				)


if __name__ == '__main__':
	BACKGROUND()
	TEXT_EDIT()
	FINDER()
	CONSOLE()
	DOCK_BAR()
	ICON()
	app.run()
