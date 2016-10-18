WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

missile = Actor('missile')
missile.fired = False

alien_a = Actor('alien_a_1')
alien_a.pos = 250, 200

def update():
	if keyboard[keys.LEFT] and ship.left > 0:
		ship.left -= 2
	if keyboard[keys.RIGHT] and ship.right < WIDTH:
		ship.right += 2
	if keyboard[keys.SPACE] and not missile.fired:
		missile.fired = True
		missile.pos = ship.midtop

	if missile.fired:
		missile.top -= 5
		if missile.bottom < 0:
			missile.fired = False


def draw():
	screen.clear()
	ship.draw()
	alien_a.draw()
	if missile.fired:
		missile.draw()


