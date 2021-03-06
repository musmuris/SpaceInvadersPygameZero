# Added Missile actor
# Handle space key
# Draw Missle
# Move Missile
# When off the top, stop drawing (so can be shot again)

WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

missile = Actor('missile')
missile.fired = False


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
	if missile.fired:
		missile.draw()

