## Added left and right end stops to stop player off the end

WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

def update():
	if keyboard[keys.LEFT] and ship.left > 0:
		ship.left -= 2
	if keyboard[keys.RIGHT] and ship.right < WIDTH:
		ship.right += 2

	
def draw():
	screen.clear()
	ship.draw()
