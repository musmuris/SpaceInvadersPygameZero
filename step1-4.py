## Added left and right end stops to stop player off the end

WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

keysPressed = {
	keys.LEFT : False,
	keys.RIGHT : False,
}

def on_key_down(key):
	keysPressed[key] = True

def on_key_up(key):
	keysPressed[key] = False

def update():
	if keysPressed[keys.LEFT] and ship.left > 0:
		ship.left -= 2
	if keysPressed[keys.RIGHT] and ship.right < WIDTH:
		ship.right += 2
		
	
def draw():
	screen.clear()
	ship.draw()
