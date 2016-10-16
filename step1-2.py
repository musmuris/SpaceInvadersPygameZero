WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

def draw():
	screen.clear()
	ship.draw()