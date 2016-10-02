

WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.pos = 250,470 

keysPressed = {
	keys.LEFT : False,
	keys.RIGHT : False
}

def on_key_down(key):
	keysPressed[key] = True

def on_key_up(key):
	keysPressed[key] = False

def update():
	if keysPressed[keys.LEFT]:
		ship.left -= 2
	if keysPressed[keys.RIGHT]:
		ship.right += 2


def draw():
	screen.clear()
	ship.draw()
