WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

missile = Actor('missile')
missile.fired = False

alien_a = Actor('alien_a_1')
alien_a.pos = 250, 200
alien_a.image1 = 'alien_a_1'
alien_a.image2 = 'alien_a_2'
alien_a.frame = 1
alien_a.direction = 10
alien_a.dead = 0

speed = 60

def updatePlayer():
	if keyboard[keys.LEFT] and ship.left > 0:
		ship.left -= 2
	if keyboard[keys.RIGHT] and ship.right < WIDTH:
		ship.right += 2
	if keyboard[keys.SPACE] and not missile.fired:
		missile.fired = True
		missile.pos = ship.midtop

def updateMissile():
	if missile.fired:
		missile.top -= 5
		if missile.bottom < 0:
			missile.fired = False

def updateAlien(alien):
	global speed

	alien.frame = alien.frame + 1
	if alien.frame == speed:
		alien.frame = 1
		updateFrame = True
	else:
		updateFrame = False

	if updateFrame:
		alien.left += alien.direction
		if alien.left > 420:
			alien.direction = -10
		elif alien.left < 20:
			alien.direction = 10

		if alien.image == 'alien_dead':
			alien.dead += 1
		elif alien.image == alien.image1:
			alien.image = alien.image2
		else:
			alien.image = alien.image1

	if alien.colliderect(missile):
		alien.image = 'alien_dead'


def update():
	updatePlayer()
	updateMissile()
	updateAlien(alien_a)	
	
	
def draw():
	screen.clear()
	ship.draw()
	if alien_a.dead < 2:
		alien_a.draw()
	if missile.fired:
		missile.draw()


