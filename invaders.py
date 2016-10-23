WIDTH = 500
HEIGHT = 500

ship = Actor('ship')
ship.midbottom = 250,490

missile = Actor('missile')
missile.fired = False

aliens = []
for row in range(5):
	for col in range(8):
		alien = Actor('alien_a_1')
		alien.pos = 55 * col + 50, 40 * row + 100
		alien.image1 = 'alien_a_1'
		alien.image2 = 'alien_a_2'
		alien.frame = 1		
		alien.dead = 0
		aliens.append(alien)

class Game:
	speed = 41
	direction = 10
	flipDirection = False

game = Game()

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
	if alien.dead > 0:
		return

	alien.frame = alien.frame + 1

	if alien.frame >= game.speed:
		alien.frame = 1
		alien.left += game.direction

		if alien.left > 420 or alien.left < 20:
			game.flipDirection = True

		if alien.image == 'alien_dead':
			alien.dead += 1
		elif alien.image == alien.image1:
			alien.image = alien.image2
		else:
			alien.image = alien.image1

	if alien.colliderect(missile) and missile.fired:
		alien.image = 'alien_dead'
		missile.fired = False
		game.speed -= 1


def update():
	updatePlayer()
	updateMissile()
	for alien in aliens:
		updateAlien(alien)	
	if game.flipDirection:
		game.direction = -game.direction
		game.flipDirection = False
	
def draw():
	screen.clear()
	ship.draw()
	for alien in aliens:
		if alien.dead < 1:
			alien.draw()
	if missile.fired:
		missile.draw()


