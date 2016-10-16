## Added KeysPressed
## Added key event handlers
## Added update to move the ship

WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

def update():
	if keyboard[keys.LEFT]:
		ship.left -= 2
	if keyboard[keys.RIGHT]:
		ship.right += 2
	
def draw():
	screen.clear()
	ship.draw()
