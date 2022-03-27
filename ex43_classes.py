from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
	
	def enter(self):
		print("This scene is not yet configured.")
		print("Subclass it and implement enter().")
		exit(1)
	
	
class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# be sure to print out the last scene
		current_scene.enter()
	
class Death(Scene):
	
	quips = [
		"You died. You kinda suck at this.",
		"This is very unfortunate.",
		"Perhaps another try might be the way to go.",
		"One more time for the ol' college try?"
	]
	
	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)
	
class CentralCorridor(Scene):
	
	def enter(self):
		print(dedent("""
			The Gothons of Planet Percel #25 have invaded your ship and 
			destroyed your entire crew. You are the last surviving
			member and your last mission is to get the neutron destruct
			bomb from the Weapons Armory, put it in the bridge, and
			blow the ship up after getting into an escape pod.
			
			You're running down the central corridor to the Weapons
			Armory when a Gothon jumps out, red scaly skin, dark grimy
			teeth, and evil clown costume flowing around his hate
			filled body. He's blocking the door to the Armory and 
			about to pull a weapon to blast you.
			"""))
		
		action = input("> ")
		
		if action == "shoot!":
			print(dedent("""
				Quick on the draw you yank out your blaster and fire
				it at the Gothon. His clown costume is flowing and 
				movin around his body, which throws you off your aim.
				Your laser hits this costume but misses him entirely.
				This completely ruins his brand new costume his mother
				bought him, which makes him fly into an insane rage
				and blast you repeatedly in the face until you are 
				dead. Then he eats you.
				"""))
			return 'death'
		
		elif action == "dodge!":
			print(dedent("""
				Like a world class boxer you dodge, weave, slip and
				slide right as the Gothon's blaster cranks a laser 
				past your head. In the middle of your artful dodge
				your foot slips and you bang your head on the metal
				wall and pass out. You wake up shortly after only to 
				die as the Gothon stomps on your head and eats you.
				"""))
			return 'death'
		
		elif action == "tell a joke":
			print(dedent("""
				Lucky for you they made you learn Gothon insults in
				the academy. You tell the one Gothon joke you know:
				Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
				fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
				not to laugh, then bursts out laughing and can't move.
				While he's laughing you run up and shoot him square in 
				the head putting him down, then jump through the
				Weapon Armory Door.
				"""))
			return 'laser_weapon_armory'
		
		else:
			print("DOES NOT COMPUTE!")
			return 'central_corridor'
			
	
class LaserWeaponArmory(Scene):
	
	def enter(self):
		print(dedent("""
			You gotta disarm a bomb.
			You get 10 tries.
			the code is 3 digits.
		"""))
		
		code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
		guess = input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 10:
			print("WRONG ENTRY!")
			guesses += 1
			guess = input("[keypad]> ")
			
		if guess == code:
			print("Nice!!")
			
			return 'the_bridge'
		else:
			print("Yeah...you didn't make it...")
			return 'death'
	
class TheBridge(Scene):
	
	def enter(self):
		print(dedent("""
			You get get on the scene.
			There's 5 Gothon's on the bridge.
			They see you've got the bomb.
			Its a stand off...
		"""))
		
		action = input("> ")
		
		if action == "throw the bomb":
			print(dedent("""
				You yeet the bomb and decide to run.
				You're shot in the back.
				As you lay dying, you know at least everyone's going down.
			"""))
			return 'death'
		elif action == "slowly place the bomb":
			print(dedent("""
				You slowly place the bomb down.
				Bolt.
				Destroy the lock on your way out.
				Head to the escape pod
			"""))
			return 'escape_pod'
		else:
			print("DOES NOT COMPUTE!")
			return "the_bridge"
	
class EscapePod(Scene):
	
	def enter(self):
		print(dedent("""
			You make it to the escape pods.
			There's 5 of them.
			Which one do you pick?
		"""))
		
		good_pod = randint(1,5)
		guess = input("[pod #]> ")
		
		if int(guess) != good_pod:
			print(dedent("""
				Turns out that wasn't the right one.
				You crash and burn.
			"""))
			return 'death'
		else:
			print(dedent("""
				You get into pod {guess}
				As you eject out of the ship, you see it explode.
				YOU WIN!!
			"""))
			return 'finished'
		
class Finished(Scene):
	def enter(self):
		print("You won! Good job.")
		return 'finished'

class Map(object):
	
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)
	

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()