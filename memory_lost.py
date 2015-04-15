# -------------------- Import Statements --------------------
import os
from sys import exit
import random

from general_functions import *
from memory_lost_equipment import *

			
# -----------------------------------------------------------
# -------------- Scene Base Classes/Subclasses --------------
class Scene(object):
	"""What some languages would consider an interface or abstract base class.
	   Not to be used directly, but that it be subclassed by other classes,
	   ensuring that they conform to the scene interface by implementing enter.
	   """
	   
	def enter(self):
		raise NotImplementedError
		exit(1)


# --------------------- Scene Subclasses --------------------
class Forest(Scene):

	def enter(self):
		me.scenes_visited.append('forest')
		print "-------------------------------------------------------------------------------"
		print "\nYour head pounds as you strain yourself trying to remember more about who you"
		print "are. You transition to a crouch with one knee in the dirt and the other bent"
		print "with your foot flat. Slowly, by pushing off your bent knee, you make it to your"
		print "feet. A few yards away you notice a tattered knapsack laying near a large rock."
		print "You cautiously make your way over to it and proceed to undo what's left of the"
		print "heavily worn straps."
		
		print "\nIn one of the pockets of the knapsack you find three pairs of vials with each"
		print "pair containing a different color liquid. On each vial is a label; on the vials"
		print "containing red liquid written on the label is: HEALTH. Written on the label of"
		print "the vials containing a yellow liquid is: ATTACK. Lastly, written on the label"
		print "of the vials containing a blue liquid is: DEFENSE. These strange vials of"
		print "liquid leave you puzzled, worsening the pounding of your head."
		
		print "\nYou take a deep breath and feel a tightness in your chest. You carefully place"
		print "the vials back in the pocket of the knapsack. In doing so you notice another"
		print "pocket containing five identical gold coins. You examine them for a moment and"
		print "then place them back into the pocket of the knapsack. You then proceed to place"
		print "the knapsack on your back as the tightening subsides slightly."
		
		print "\nYou begin to wonder about the parallels of your misfortune with that of a plot"
		print "of a bad video game... The knapsack containing gold coins, vials containing"
		print "strange liquids which are reminiscent of potions, and a dark forest? You decide"
		print "it's time to head out and find your way back home... wherever that may be."
		
		loop = 'start of forest'
		while loop == 'start of forest':
			forest_goblin = Goblin()
			me.enemy = forest_goblin
			
			print "\nYou trudge forward, your eyes darting all around you as you approach a trail"
			print "that's been partially cleared. You begin to follow the trail but quickly start"
			print "questioning your decision. Should I risk running into someone else along this"
			print "trail while still in such bad shape?"
			
			print "\n(Enter only the number for your decision)"
			stay_on_path = "stay on the partially cleared trail."
			stay_off_path = "wander through the forest without following the trail."
			print "-------------------------------------------------------------------------------"
			print "1. %s" % stay_on_path
			print "2. %s" % stay_off_path
			print "-------------------------------------------------------------------------------"		
			forest_path_choice = raw_input("Choice 1 or 2? ")
			me.forest_path_choice = forest_path_choice
			 
			if forest_path_choice == "1":
				print "\nAfter a few seconds you decide to stay on the partially cleared trail. You"
				print "continue along the trails twists, turns, inclines, and declines. You start to"
				print "feel confident in your decision to follow the trail. The denseness of the"
				print "forest seems to be lessening. Just as your nerves are starting to calm you see"
				print "a shadow in your peripheral."
				
				# Temporary boosts given for element of surprise
				forest_goblin.agility += 4
				
				print "What appears to be a goblin lunges towards you! Forcing you to take action.\n"
				
				me.state = 'in combat'
				me.attack()
				
				# End of temporary boosts given for element of surprise
				forest_goblin.agility -= 4
				
				loop = 0
			elif forest_path_choice == "2":
				print "\nAfter a few seconds you decide to wander through the forest without following"
				print "the trail. You wander through the forest with a voice in your head questioning"
				print "your decision. \"You idiot, you should have stayed on the trail. You're getting"
				print "yourself even more lost.\" You try and direct your focus outwards on your"
				print "surroundings hoping that it will silence the annoying voice that's insulting"
				print "you. Just as the voice in your head begins to quiet down you see something"
				print "moving in the distance. You quickly realize it isn't human nor is it an animal;"
				print "the frame and posture seem completely foreign."
				
				print "\nYou crouch down and slowly move forward, keeping cover behind tree trunks and"
				print "foliage. You're close enough to hear it snarling and see that it appears to be"
				print "a goblin. You slowly begin to stand up slightly to start getting your distance"
				print "from it when a twig snaps under your foot. You look up in horror and see the"
				print "goblin looking right at you. The goblin charges towards you!\n"
				
				me.state = 'in combat'
				me.attack()
				
				loop = 0
			else:
				loop = 'start of forest'
				
	
class Meadow(Scene):

	def enter(self):
		me.scene_player_is_in = 'meadow'
		me.scenes_visited.append('meadow')
		if me.scenes_visited.count('troll cave') == 1 and me.enemies_killed.count('Werewolf') == 0:
			print "-------------------------------------------------------------------------------"
			print "\nYou begin heading towards the mountains located adjacent to the side of the"
			print "mountains containing the cave entrance. A familiar shadowy figure comes"
			print "charging towards you... it's the Werewolf! You prepare yourself for battle.\n"
				
			meadow_werewolf = Werewolf()
			me.enemy = meadow_werewolf
			me.state = 'in combat'
			me.attack()
		elif me.scenes_visited.count('swamp') == 0:
			print "-------------------------------------------------------------------------------"
			print "\nYou nervously continue forward through the forest your mind racing faster than"
			print "before. A goblin... a GOBLIN? Repeating that word begins to make you feel even"
			print "crazier. You've played enough video games to know a goblin when you see one but"
			print "those were just video games... what in the hell is going on..."
			
			print "\nYou notice a clearing up ahead; it appears to be a meadow upon closer"
			print "inspection. You continue forward with a pace that's eager of leaving the forest"
			print "behind. The light from the full moon illuminates the meadow. On two sides of"
			print "the meadow are monuments to the power of plate tectonics... mountains. The"
			print "sight sends a chill rushing down your spine as you are reminded of your"
			print "insignificance."
			
			meadow_werewolf = Werewolf()
			me.enemy = meadow_werewolf
				
			if me.intelligence <= 4:
				print "\nYou tilt your head back while closing your eyes... taking a deep breath in the"
				print "process. You immediately regret doing so as you hear the whoosh of something"
				print "moving quickly towards you."
				
				# Temporary boosts given for blindsiding player	
				meadow_werewolf.agility += 9
				meadow_werewolf.attack_rating += 10
					
				print "\nYou are blindsided by whatever was running towards you... a quick glance as you"
				print "ready yourself allows you to see that it's a Werewolf!\n"
					
				me.state = 'in combat'
				me.attack()
				
				# End of temporary boosts given for blindsiding player
				meadow_werewolf.agility -= 9
				meadow_werewolf.attack_rating -= 10
			else:
				print "\nYou look around the open area before you and see something racing in your"
				print "direction. You ready your stance and prepare for battle. As it nears, you see"
				print "that it's a Werewolf!\n"
				
				me.state = 'in combat'
				me.attack()	
		elif me.scenes_visited.count('swamp') == 1 and me.scenes_visited.count('troll cave') == 0:
			print "-------------------------------------------------------------------------------"
			print "\nYou keep moving eager as to what's next. The forest foliage continues to become"
			print "increasingly sparse. You finally reach the edge of the forest and step into"
			print "what appears to be a meadow. The repetitious sight of tree trunks and plants..."
			print "green and brown and green and brown is replaced by towering monuments to plate"
			print "tectonics... mountains. These mountains appear to surround two sides of the"
			print "meadow with another side surrounded by the forest you just exited. To the right"
			print "of you the meadow extends as far as the eye can see. You proceed forward"
			print "towards the mountains in awe. As you draw nearer you notice a winding mountain"
			print "path.",
			
			loop = 'mountain path or more meadow'
			while loop == 'mountain path or more meadow':
				print "You stop and think about whether you should ascend up this path."
				
				print "\n(Enter only the number for your decision)"
				print "-------------------------------------------------------------------------------"
				print "1. It doesn't look too menacing... I can handle it."
				print "2. I haven't checked out the meadow enough yet." 
				print "-------------------------------------------------------------------------------"		
				meadow_path_choice = raw_input("Choice 1 or 2? ")
				me.meadow_path_choice = meadow_path_choice
				
				if meadow_path_choice == "1":
					print "\nYou head towards the mountain path excited but also nervous of what lies ahead."
					
					loop = 0
				elif meadow_path_choice == "2":
					print "\nYou turn to your left and begin heading across the meadow towards the other"
					print "side that is surrounded by mountains. You realized this will probably be the"
					print "easiest part of your trek and wanted to get some \"rest\" before proceeding up"
					print "the mountains. As you venture through the meadow you can't help but keep your"
					print "attention on the night sky. You suddenly hear the whoosh of something moving"
					print "quickly towards you."
					
					meadow_werewolf = Werewolf()
					me.enemy = meadow_werewolf
					
					# Temporary boosts given for blindsiding player	
					meadow_werewolf.agility += 9
					meadow_werewolf.attack_rating += 10
					
					print "\nYou are blindsided by whatever was running towards you... a quick glance as you"
					print "ready yourself allows you to see that it's a Werewolf!\n"
					
					me.state = 'in combat'
					me.attack()
				
					# End of temporary boosts given for blindsiding player
					meadow_werewolf.agility -= 9
					meadow_werewolf.attack_rating -= 10
					
					loop = 0
				else:
					loop = 'mountain path or more meadow'
					
class Swamp(Scene):

	def enter(self):
		me.scene_player_is_in = 'swamp'
		me.scenes_visited.append('swamp')
		if me.scenes_visited.count('meadow') == 0:
			print "-------------------------------------------------------------------------------"
			print "\nYou nervously continue forward through the forest unsure of where you are"
			print "headed. For the first time you notice the beads of sweat dripping down the side"
			print "of your neck. No doubt they're not from the temperature it's maybe sixty at"
			print "best. No, they're from anxiety... from fear... from uncertainty..."
			
			print "\nYou continue to push your way through the foliage while the dense canopy of the"
			print "forest blocks out what light the full moon above provides. You begin to feel"
			print "the ground below your feet softening with each step... mud. Every time you lift"
			print "your leg to walk you are met with resistance. The mud makes it seem like you"
			print "have suction cups stuck to the bottom of your shoes. Your once nimble trot now"
			print "resembles a tiring, awkward march."
			
			loop = 'shack in swamp'
			while loop == 'shack in swamp':
				swamp_ogre = Ogre()
				me.enemy = swamp_ogre
				
				print "\nIn the distance you see a small house. As you near it you realize it's more of"
				print "a large, wooden shack. Hmm... I could check out the shack or leave it alone and"
				print "move on."
				
				print "\n(Enter only the number for your decision)"
				check_out_shack = "might as well check out the shack."
				leave_shack_alone = "it's probably best to just disregard it and move on."
				print "-------------------------------------------------------------------------------"
				print "1. %s" % check_out_shack
				print "2. %s" % leave_shack_alone
				print "-------------------------------------------------------------------------------"
				swamp_shack_choice = raw_input("Choice 1 or 2? ")
				me.swamp_shack_choice = swamp_shack_choice
				
				if swamp_shack_choice == "1":
					print "\nYou decide that you might as well check out the shack. You cautiously make your"
					print "way towards the shack being careful not to step in the stagnant water that"
					print "surrounds the shack on two sides. Your heart is racing as you creep up to the"
					print "side of the shack. You can hardly hear yourself think over the sound of your" 
					print "heart beating. You inch near the door of the shack and slowly reach out your"
					print "hand to open the door... You are sent flying backwards as the door is thrown"
					print "open with great force!"
					
					me.current_health -= 10
					print "\nYou suffer 10 damage from being thrown back."
					me.health_check()
			
					print "\nWhat appears to be an ogre has emerged from the shack! The ogre locks eyes on"
					print "you and raises it's weapon. You quickly get back to your feet and ready your"
					print "stance for battle.\n"
					
					me.state = 'in combat'
					me.attack()
					
					loop = 0
				elif swamp_shack_choice == "2":
					print "\nYou decide that it's probably best to just disregard it and move on. You" 
					print "realize there probably isn't much good that can come from checking the shack"
					print "out."
					
					if me.luck <= 3:
						print "\nYou continue past the shack trying not to bring unwanted attention to yourself"
						print "when... you trip over a vine creating a loud splash in the stagnant, murky"
						print "water. As you get yourself back to your feet you hear the sound of the shack"
						print "door slamming open against the outside of the shack. You whip around and"
						print "discover an ogre lumbering towards you! You quickly ready your stance for"
						print "battle.\n"
						
						me.state = 'in combat'
						me.attack()
					elif me.luck >= 7:
						print "\nAs you begin to pass the shack you notice a large cleaver sticking out of the" 
						print "mud nearby. This could come in handy you think to yourself. You quickly pull"
						print "the large cleaver out of the mud and add it your inventory."
						
						Player.inventory['weapons']['Large Cleaver'] = 1
						
						print "\nYou continue on, feeling slightly more confident having found a new weapon."
						print "It doesn't take long before the denseness of the forest begins to lessen."
					else:
						print "\nYou continue on, making sure not to bring unwanted attention to yourself."
						print "It doesn't take long before the denseness of the forest begins to lessen."
					
					loop = 0
				else:
					loop = 'shack in swamp'
			
		
class TrollCave(Scene):
	
	def enter(self):
		me.scene_player_is_in = 'troll cave'
		me.scenes_visited.append('troll cave')
		print "-------------------------------------------------------------------------------"
		print "\nYou continue towards the mountains while maintaining complete awareness of your"
		print "surroundings. Your heart is still racing from your last encounter. After a"
		print "short while you are close enough to see a large opening in the side of the"
		print "mountain... a cave. You continue forward until you're just outside the entrance"
		print "to the cave. You hesitate briefly before heading inside."
		
		print "\nWith the moonlight being your only light, it doesn't take long before it"
		print "becomes nearly impossible to see even your hand in front of your face. You"
		print "begin to feel around in the darkness for the cave wall to help guide you back"
		print "when you hear the familiar sound of a crackling fire. Impossible, considering"
		print "it's pitch black in here you think to yourself."
		
		loop = 'fire in troll cave'
		while loop == 'fire in troll cave': 
			print "\nYou finally find the wall of the cave in the darkness and stop to decide"
			print "whether to..."
			
			print "\n(Enter only the number for your decision)"
			find_fire_in_troll_cave = "head further into the cave to find the source of the fire."
			leave_the_troll_cave = "head back outside into the meadow and forget that nonsense."
			print "-------------------------------------------------------------------------------"
			print "1. %s" % find_fire_in_troll_cave
			print "2. %s" % leave_the_troll_cave
			print "-------------------------------------------------------------------------------"		
			inside_troll_cave_choice = raw_input("Choice 1 or 2? ")
			me.inside_troll_cave_choice = inside_troll_cave_choice
			
			if inside_troll_cave_choice == "1":
				print "\nYou confidently begin to head further into the cave to find the source of the" 
				print "fire. Using the wall as guidance you turn the corner and see the flickering of"
				print "shadows on the cave wall. You are able to see just slightly better as you"
				print "continue around another corner. At last, you find the fire... this area of the"
				print "cave is dimly lit; however you didn't think this one through... you stumble"
				print "upon a troll sitting by it's fire! The troll rises to it's feet and heads"
				print "toward you. Quickly, you ready your stance for battle.\n"
				
				cave_troll = Troll()
				me.enemy = cave_troll
				me.state = 'in combat'
				me.attack()
				
				loop = 0
			elif inside_troll_cave_choice == "2":
				print "\nYou pause and then head back outside into the meadow and forget that nonsense."
				print "You creep along the wall back towards the cave entrance. You breathe a sigh of"
				print "relief as you step back into the meadow."
				
				loop = 0
			else:
				loop = 'fire in troll cave'
			
			
class CavePassage(Scene):
	def enter(self):
		me.scene_player_is_in = 'cave passage'
		me.scenes_visited.append('cave passage')
		print "-------------------------------------------------------------------------------"
		print "\nThe light from the fire allows you to see what looks like a passage way blocked"
		print "by a large boulder. If you're strong enough you may be able to move it."
		
		if me.strength >= 7 and me.intelligence >= 3:
			print "\nYou grip the boulder and using all your strength roll it aside just far enough"
			print "to squeeze past it. Before heading into the passage you carefully grab one of"
			print "the logs from the fire to use as a torch. You proceed to navigate the twists"
			print "and turns of the cave passage and tirelessly climb as the passage begins to"
			print "ascend sharply."
		else:
			print "\nYou grip the boulder and using all of your strength try to roll it aside to no"
			print "avail. You then begin to try and rock it back and forth hoping the slight"
			print "momentum will be enough to roll it aside. It slowly begins to move back and"
			print "forth at an increasing rate. You give it one last hard shove and begin to"
			print "squeeze past when it rocks back into place knocking you down and pinning your"
			print "leg underneath it. You scream out in pain as a pool of blood begins to"
			print "accumulate. You feel weak and dizzy as you drift off into darkness...\n"
			
			me.current_health = 0
			me.health_check()


class DragonCave(Scene):
	def enter(self):
		me.scene_player_is_in = 'dragon cave'
		me.scenes_visited.append('dragon cave')
		cave_dragon = Dragon()
		me.enemy = cave_dragon
		print "-------------------------------------------------------------------------------"
		if me.scenes_visited.count('cave passage') > 0:
			print "\nThe passage begins to level out and soon you find yourself staring into a large"
			print "cavern. Your torch reveals a enormous figure looming in the darkness before"
			print "promptly burning out."
		elif me.scenes_visited.count('other mountain') > 0:
			print "\nYou are shrouded by darkness as you venture into the cavern. You stop suddenly"
			print "as you hear the sound of something breathing."
		else:
			pass
			
		print "\n\"You've made it a lot farther than you should have.\", says a voice in your"
		print "head. You realize something is immediately wrong as the voice isn't the normal"
		print "voice you hear."
		print "\n\"Yes, I'm telepathically communicating with you... my name is Nexus..."
		print "prepare to die.\"\n"
		print "A burst of fire lights up the cavern allowing you to see that it's clearly a"
		print "Dragon. You charge at Nexus as ready as you'll ever be.\n"
			
		me.state = 'in combat'
		me.attack()
		
		
class Mountain(Scene):
	
	def enter(self):
		me.scene_player_is_in = 'mountain'
		me.scenes_visited.append('mountain')
		# The condition before the 'or' is for those who visited the swamp before the meadow 
		# The condition after the 'or' is for those  who visited the cave but didn't search for the fire;
		# it acts as a continuation for the else loop below.
		if me.scenes_visited.count('dragon cave') > 0:
			print "-------------------------------------------------------------------------------"
			if me.old_bridge_fight_choice == "1":
				print "\nYou cross the old bridge once more too tunnel visioned by your last encounter"
				print "to worry much about how dangerous it is. You maintain a tight grip and"
				print "skilfully make it to the other side. You continue along a path."
			elif me.old_bridge_fight_choice == "2":
				print "\nYou finish heading across the bridge anxious and upset about what had just"
				print "happened. It wasn't the loss of the gold that bothered you... you were more"
				print "upset that the only other human you've come across wasn't of any help. You"
				print "begin thinking about how you could have handled the situation differently."
			else:
				pass
			
			if me.scenes_visited.count('cave passage') > 0:
				if 'Chainmail Chausses' not in me.inventory['armor']:
					print "\nYour focus shifts to someone or something wearing armor laying facedown against"
					print "some large rocks just off the path. A small pool of blood surrounds their"
					print "lifeless body."
					
					print "\nYou swear you can feel the hair on the back of neck stand straight up. The"
					print "victim appears to be an Orc or something similar upon closer inspection. You"
					print "mull over the idea of plundering the chainmail armor from the fallen Orc and"
					print "quickly decide that he won't be needing it as much as you. With some difficulty"			
					print "you remove the chainmail chausses and hauberk. You add them to your inventory."
								
					Player.inventory['armor']['Chainmail Chausses'] = 1
					Player.inventory['armor']['Chainmail Hauberk'] = 1
				else:
					pass
					
			print "\nYou now notice the path splits two ways; the path on the right heads back down"
			print "to the meadow that you ventured through earlier. You're unsure where the path"
			print "on the left leads. You opt not to go back down to the meadow on account of"
			print "being tired from this long journey. You begin heading down the mountain"
			print "continuing along the path."
			
			if me.strength < 7 and me.agility < 5:
				print "\nYou attempt to navigate around a narrow ledge but lose your grip on the wall"
				print "behind you. You aren't able to steady yourself in time as you plunge forward"
				print "off the ledge. Your head slams into a rock as you begin to plummet killing you"
				print "instantly."
				me.current_health = 0
				me.health_check()
			elif me.strength < 7:
				print "\nYou attempt to navigate around a narrow ledge but lose your grip on the wall"
				print "behind you."
						
				if Player.equipment['weapon'] is not None:
					dropped_weapon = Player.equipment['weapon']
					print "\nYou are able to steady yourself; however, you lose your %s as" % dropped_weapon.weapon_name
					print "you regrip the wall behind you. You continue down the path being extra careful"
					print "as you descend."
							
					Player.equipment['weapon'] = None
					Player.inventory['weapons'].pop(dropped_weapon.weapon_name)
				else:
					print "\nYou are able to steady yourself as you regrip the wall behind you. You continue"
					print "down the path being extra careful as you descend. You don't want to make the"
					print "same mistake twice."
			elif me.agility < 5:
				print "\nYou navigate around a narrow ledge doing your best to maintain strong footing."
				print "You continue down the path but lose your footing on a sharp descent. You slide"
				print "a short distance down the path."
						
				me.current_health -= 10
				print "\nYou suffer 10 damage from sliding."
				me.health_check()
			else:
				print "\nYou skilfully navigate the narrow ledges and sharp descents of the mountain"
				print "path with ease."
					
			print "After a while you are able to see water in the distance. As you near the water"
			print "you see a hastily made raft sitting ashore. You begin to wonder if the raft"
			print "belonged to the Orc."
					
			loop = 0
		elif me.meadow_path_choice == "1" or me.scenes_visited.count('mountain') == 2 and 'Chainmail Chausses' not in me.inventory['armor']:
			print "-------------------------------------------------------------------------------"
			print "\nYou begin to ascend up the mountain along the path. The frequent twists and"
			print "turns don't allow you to see very far ahead. As you continue to climb the path"
			print "it becomes narrower and narrower. You carefully maneuver around precarious"
			print "ledges and eventually the path widens slightly. You turn a corner and nearly"
			print "lose your footing at the sight of someone or something that's wearing armor"
			print "laying facedown against some large rocks. A small pool of blood surrounds their"
			print "lifeless body."
			
			print "\nYou swear you can feel the hair on the back of neck stand straight up. The"
			print "victim appears to be an Orc or something similar upon closer inspection. You"
			print "mull over the idea of plundering the chainmail armor from the fallen Orc and"
			print "quickly decide that he won't be needing it as much as you. With some difficulty"			
			print "you remove the chainmail chausses and hauberk. You add them to your inventory."
						
			Player.inventory['armor']['Chainmail Chausses'] = 1
			Player.inventory['armor']['Chainmail Hauberk'] = 1
			
			loop = 'bridge or path'
			while loop == 'bridge or path':
				print "\nYour attention shifts as notice an old bridge made from wooden planks and rope"
				print "that is stretching across to another path in the mountains. You stop and think"
				print "about whether to continue down the path you are currently on that leads down"
				print "the other side of the mountain or to cross the old bridge."
				
				print "\n(Enter only the number for your decision)"
				cross_the_bridge = "attempt crossing the old bridge."
				down_the_path = "continue down the path you are currently on."
				print "-------------------------------------------------------------------------------"
				print "1. %s" % cross_the_bridge
				print "2. %s" % down_the_path
				print "-------------------------------------------------------------------------------"					
				mountain_path_choice = raw_input("Choice 1 or 2? ")
				me.mountain_path_choice = mountain_path_choice
				
				if mountain_path_choice == "1":
					print "\nYou decide to attempt crossing the old bridge. You then proceed to walk up to"
					print "the bridge while examining it closer."
					
					loop = 0
				elif mountain_path_choice == "2":
					print "\nYou decide to continue down the path you are currently on. \"Too risky\", you"
					print "mutter to yourself as you examine the bridge. You begin heading down the"
					print "mountain continuing along the path."
					
					if me.strength < 7 and me.agility < 5:
						print "\nYou attempt to navigate around a narrow ledge but lose your grip on the wall"
						print "behind you. You aren't able to steady yourself in time as you plunge forward"
						print "off the ledge. Your head slams into a rock as you begin to plummet killing you"
						print "instantly."
						me.current_health = 0
						me.health_check()
					elif me.strength < 7:
						print "\nYou attempt to navigate around a narrow ledge but lose your grip on the wall"
						print "behind you."
						
						if Player.equipment['weapon'] is not None:
							dropped_weapon = Player.equipment['weapon']
							print "\nYou are able to steady yourself; however, you lose your %s as" % dropped_weapon.weapon_name
							print "you regrip the wall behind you. You continue down the path being extra careful"
							print "as you descend. You don't want to make the same mistake twice."
							
							Player.equipment['weapon'] = None
							Player.inventory['weapons'].pop(dropped_weapon.weapon_name)
						else:
							print "\nYou are able to steady yourself as you regrip the wall behind you. You continue down the"
							print "path being extra careful as you descend. You don't want to make the same mistake twice."
					elif me.agility < 5:
						print "\nYou navigate around a narrow ledge doing your best to maintain stable footing."
						print "You continue down the path but lose your footing on the sharp descent. You"
						print "slide a short distance down the path."
						
						me.current_health -= 10
						print "\nYou suffer 10 damage from sliding down the path."
						me.health_check()
					else:
						print "\nYou skilfully navigate the narrow ledges and sharp descents of the mountain"
						print "path with ease."
					
					print "After a while you are able to see water in the distance. As you near the water"
					print "you see a hastily made raft sitting ashore. You begin to wonder if the raft"
					print "belonged to the Orc."
					
					loop = 0
					
				else:
					loop = 'bridge or path'
				
			
		# This is for those who visited the troll cave and exited without searching for the fire
		else:
			print "-------------------------------------------------------------------------------"
			print "\nYou begin heading towards the mountains located adjacent to the side of the"
			print "mountains containing the cave entrance. As you continue to walk alongside the"
			print "mountains you begin to worry that their might not be a safe way to scale them."
			print "A wave of hopelessness slowly begins to consume you... As you start to give up"
			print "all hope you come across a winding mountain path."
			
		
class OldBridge(Scene):

	def enter(self):
		me.scene_player_is_in = 'old bridge'
		me.scenes_visited.append('old bridge')
		old_bridge_bandit = Bandit()
		me.enemy = old_bridge_bandit	
		if me.scenes_visited.count('dragon cave') == 0:
			print "-------------------------------------------------------------------------------"							
			print "\nYou tightly grip the ropes to the bridge while walking across the heavily"
			print "weathered wood planks. Your heart pounds and climbs its way up into your throat"
			print "shortening your breath as you continue to cross the old bridge. With every step"
			print "the bridge sways back and forth..."
			
			if me.agility >= 6 and me.strength >= 6:
				print "\nYou maintain a tight grip on the ropes and skilfully continue stepping across"
				print "the planks. Finally, you make it across and immediately kneel down relishing in"
				print "the fact that you are on stable ground. No sooner than after kneeling you are"
				print "ambushed by a bandit... atleast it's appears to be a human you think to"
				print "yourself.\n"
				
				if me.enemies_killed.count('Bandit') == 0:
					old_bridge_bandit.agility += 11  
					me.state = 'in combat'
					me.attack()
					old_bridge_bandit.agility -= 11
				else:
					pass
				
				if me.charisma >= me.enemy.charisma and me.inventory['gold'] >= 40:
					print "\nYou quickly jump to your feet and distance yourself from the attacking bandit"
					print "hoping to get a word in before he attempts to strike again. You quickly offer"
					print "him 40 gold if he will let you continue on without any more trouble. He pauses"
					print "and surprisingly accepts your offer. You quickly search your knapsack for the"
					print "gold coins and hand them over to the bandit. 40 gold is removed from your"
					print "inventory."
					
					if me.enemies_killed.count('Bandit') == 0:
						me.inventory['gold'] -= 40
						old_bridge_bandit.gold += 40
						me.state = 'normal'
					else:
						pass
					
					loop = 'old bridge fight or flight'
					while loop == 'old bridge fight or flight':
						print "\nYou begin to head up the path that continued on after the old bridge when you"
						print "start thinking about what just happened. You start to fill with anger as you"
						print "think back on everything you've been through recently. None of it makes sense"
						print "to you. You know you need to decide now whether to do something about this or"
						print "just forget about it and continue on."
						
						print "\n(Enter only the number for your decision)"
						print "-------------------------------------------------------------------------------"
						print "1. Turn back and fight the bandit."
						print "2. Just forget about it and move on." 
						print "-------------------------------------------------------------------------------"					
						old_bridge_fight_choice = raw_input("Choice 1 or 2? ")
						me.old_bridge_fight_choice = old_bridge_fight_choice
						
						if old_bridge_fight_choice == "1":
							print "\nYou quietly begin heading back towards the old bridge. Your palms sweat heavily"
							print "as the bandit comes into view. He's too busy drinking from his flask to notice"
							print "you creeping up. You ready your stance and charge at him.\n"
							
							me.state = 'in combat'
							me.attack()
							
							loop = 0
						elif old_bridge_fight_choice == "2":
							print "\nYou dismiss the idea of going back for him and continue up the path."
							
							loop = 0
						else:
							loop = 'old bridge fight or flight'
				else:
					print "\nYou quickly jump to your feet and ready your stance to defend yourself better."
			else:
				print "\nYou continue stepping across the heavily worn planks doing your best to"
				print "maintain a tight grip on the ropes. As you step onto a plank it breaks beneath"
				print "your feet. You lose your grip and plummet to the ground below."
				
				me.current_health = 0
				me.health_check()
		elif me.scenes_visited.count('cave passage') > 0 and me.scenes_visited.count('old bridge') == 1:
			print "-------------------------------------------------------------------------------"
			print "\nBefore you can cross the bridge; however, you are ambushed from behind. You"
			print "turn around to see that it appears to a be bandit. Atleast it appears to be a"
			print "human... you think to yourself."
			
			old_bridge_bandit.agility += 11
			me.state = 'in combat'
			me.attack()
			old_bridge_bandit.agility -= 11
			
			if me.charisma >= old_bridge_bandit.agility and me.inventory['gold'] >= 40:
				print "\nYou quickly jump to your feet and distance yourself from the attacking bandit"
				print "hoping to get a word in before he attempts to strike again. You quickly offer"
				print "him 40 gold if he will let you continue on without any more trouble. He pauses"
				print "and surprisingly accepts your offer. You quickly search your knapsack for the"
				print "gold coins and hand them over to the bandit. 40 gold is removed from your"
				print "inventory."
					
				me.inventory['gold'] -= 40
				old_bridge_bandit.gold += 40
				me.state = 'normal'
			
			else:
				print "\nYou quickly ready your stance to defend yourself better."
		elif me.scenes_visited.count('cave passage') > 0 and me.scenes_visited.count('old bridge') == 2:
			print "-------------------------------------------------------------------------------"
			if me.agility >= 6 and me.strength >= 6:
				print "\nYou tightly grip the ropes to the bridge while walking across the heavily"
				print "weathered wood planks. Your heart pounds and climbs its way up into your throat"
				print "shortening your breath as you continue to cross the old bridge. With every step"
				print "the bridge sways back and forth..."
					
				loop = 'old bridge fight or flight from cave'
				while loop == 'old bridge fight or flight from cave':
					print "\nYou start thinking about what just happened. You start to fill with anger as"
					print "you think back on everything you've been through recently. None of it makes"
					print "sense to you. You know you need to decide now whether to do something about this or"
					print "just forget about it and continue on."
						
					print "\n(Enter only the number for your decision)"
					print "-------------------------------------------------------------------------------"
					print "1. Turn back and fight the bandit."
					print "2. Just forget about it and move on." 
					print "-------------------------------------------------------------------------------"					
					old_bridge_fight_choice = raw_input("Choice 1 or 2? ")
					me.old_bridge_fight_choice = old_bridge_fight_choice
						
					if old_bridge_fight_choice == "1":
						print "\nYou quietly make your way back across the old bridge. Your palms sweat heavily"
						print "as the bandit comes into view. He's too busy drinking from his flask to notice"
						print "you creeping up. You ready your stance and charge at him.\n"
							
						me.state = 'in combat'
						me.attack()
							
						loop = 0
					elif old_bridge_fight_choice == "2":
						print "\nYou dismiss the idea of going back for him and continue across the bridge."
							
						loop = 0
					else:
						loop = 'old bridge fight or flight from cave'
			else:
				print "\nYou continue stepping across the heavily worn planks doing your best to"
				print "maintain a tight grip on the ropes. As you step onto a plank it breaks beneath"
				print "your feet. You lose your grip and plummet to the ground below."
				
				me.current_health = 0
				me.health_check()
		elif me.scenes_visited.count('dragon cave') > 0 and me.enemies_killed.count('Bandit') > 0:
			print "-------------------------------------------------------------------------------"
			if me.agility >= 6 and me.strength >= 6:
				print "\nYou tightly grip the ropes to the bridge while walking across the heavily"
				print "weathered wood planks. Your heart pounds and climbs its way up into your throat"
				print "shortening your breath as you continue to cross the old bridge. With every step"
				print "the bridge sways back and forth..."
			else:
				print "\nYou continue stepping across the heavily worn planks doing your best to"
				print "maintain a tight grip on the ropes. As you step onto a plank it breaks beneath"
				print "your feet. You lose your grip and plummet to the ground below."
				
				me.current_health = 0
				me.health_check()

				
class OtherMountain(Scene):
	def enter(self):
		me.scene_player_is_in = 'other mountain'
		me.scenes_visited.append('other mountain')
		if me.scenes_visited.count('dragon cave') == 1:
			print "-------------------------------------------------------------------------------"
			loop = 'to bridge or to water path'
			while loop == 'to bridge or to water path':
				print "\nYou exit the cave and proceed along the mountain path. You slowly make your way"
				print "to a fork in the path. You're tired and ready to leave this all behind. You can"
				print "either start descending down sharply to the left or head forward and slowly"
				print "descend towards what looks like a bridge."
						
				print "\n(Enter only the number for your decision)"
				print "-------------------------------------------------------------------------------"
				print "1. Follow the path on the left that descends down the mountain."
				print "2. Follow the path straight ahead that slowly descends towards a bridge." 
				print "-------------------------------------------------------------------------------"									
				other_mountain_path_choice = raw_input("Choice 1 or 2? ")
				me.other_mountain_path_choice = other_mountain_path_choice
				
				if other_mountain_path_choice == "1":
					print "\nYou take a slight left and begin descending down the side of the mountain. Not"
					print "long after you are able to see water in the distance. As you near the water you"
					print "see a well made raft sitting ashore.",
					
					if me.scenes_visited.count('old bridge') > 0 and me.enemies_killed.count('Bandit') > 0:
						print "You begin to wonder if the raft belonged"
						print "to the bandit."
					elif me.scenes_visited.count('old bridge') > 0 and me.enemies_killed.count('Bandit') == 0:
						print "You begin to wonder if the raft belongs"
						print "to the bandit."
					elif me.scenes_visited.count('old bridge') == 0:
						print "You wonder who the raft belongs to."
					else:
						pass
					
					loop = 0
				elif other_mountain_path_choice == "2":
					print "\nYou continue along the path as it begins to descend slightly towards what looks"
					print "like a bridge. After awhile you are near a heavily worn bridge. Without any"
					print "hesitation you decide to cross it not wanting to have spent all this energy for"
					print "nothing."
					
					loop = 0
				else:
					loop = 'to bridge or to water path'
		elif me.scenes_visited.count('old bridge') == 1:
			print "-------------------------------------------------------------------------------"
			print "\nAs you continue along the path you begin to pick up your pace. While nervous,"
			print "you aren't nearly as afraid as you were when you started having come all this" 
			print "way."
			
			loop = 'ascending or descending path'
			while loop == 'ascending or descending path':
				print "\nYou quickly and carefully maneuver the path. You soon find yourself at a fork"
				print "in the path. You can either start descending down to the right or head forward"
				print "and continue ascending."
						
				print "\n(Enter only the number for your decision)"
				print "-------------------------------------------------------------------------------"
				print "1. Follow the path on the right that descends down the mountain."
				print "2. Follow the path straight ahead that ascends into the mountains more." 
				print "-------------------------------------------------------------------------------"									
				other_mountain_path_choice = raw_input("Choice 1 or 2? ")
				me.other_mountain_path_choice = other_mountain_path_choice
				
				if other_mountain_path_choice == "1":
					print "\nYou take a slight right and begin descending down the side of the mountain. Not"
					print "long after you are able to see water in the distance. As you near the water you"
					print "see a well made rift sitting ashore.",
					
					if me.scenes_visited.count('old bridge') > 0 and me.enemies_killed.count('Bandit') > 0:
						print "You begin to wonder if the raft"
						print "belonged to the bandit."
					elif me.scenes_visited.count('old bridge') > 0 and me.enemies_killed.count('Bandit') == 0:
						print "You begin to wonder if the raft"
						print "belongs to the bandit."
					elif me.scenes_visited.count('old bridge') == 0:
						print "You wonder who the raft belongs to."
					else:
						pass
					
					loop = 0
				elif other_mountain_path_choice == "2":
					print "\nYou continue along the path as it begins to ascend further into the mountains."
					print "After awhile you are able to see a large cave entrance ahead of you. Without"
					print "hesitation you questionably decide to enter it not wanting to have spent all"
					print "this energy for nothing."
					
					loop = 0
				else:
					loop = 'ascending or descending path'
			
			
class Water(Scene):

	def enter(self):
		me.scene_player_is_in = 'water'
		me.scenes_visited.append('water')
		water_kraken = Kraken()
		me.enemy = water_kraken
		if me.scenes_visited.count('dragon cave') > 0 or me.scenes_visited.count('old bridge') > 0:
			print "-------------------------------------------------------------------------------"					
			print "\nThe sun has started to rise over the horizon. Off in the distance you can see a"
			print "mass of land. You push the raft out into the water and climb aboard. A gust of"
			print "wind catches the sail and off you go. You make your way towards the landmass"	
			print "unsure if it will even be of any benefit to you."
			
			if random.randint(0,(20 + me.enemy.luck - me.luck)) >= 3:
				print "\nSeveral large tentacles grab hold of the raft. You're able to see the creature"
				print "as it rises closer to the surface. It's a Kraken! You're going to have to kill"
				print "it to survive.\n"
				
				water_kraken.agility += 10
				me.state = 'in combat'
				me.attack()
			else:
				print "\nYou continue to peacefully drift in the water."
		else:
			print "-------------------------------------------------------------------------------" 
			print "\nAs the sun starts to rise over the horizon you convince yourself that you are"
			print "able to see a landmass way off in the distance that may be beneficial. You push"
			print "the hastily made raft out into the water and climb aboard. A gust of wind"
			print "catches the tattered sail and slowly you begin heading towards the landmass."
			
			if random.randint(0,(10 + me.enemy.luck - me.luck)) >= 3:
				print "\nSeveral large tentacles grab hold of the raft. You're able to see the creature"
				print "as it rises closer to the surface. It's a Kraken! You're going to have to kill"
				print "it to survive.\n"
				
				water_kraken.agility += 10
				me.state = 'in combat'
				me.attack()
			else:
				print "\nYou continue to peacefully drift in the water."
				
				
class Island(Scene):
	
	def enter(self):
		print "-------------------------------------------------------------------------------"
		print "\nYour raft comes to a rest on the shore of the island. You examine the island"
		print "for signs of life and see nothing besides various plants including a palm tree."
		print "You wander the island searching for anything... ANYTHING that could be of help."
		print "You begin to lose hope and decide to fight the feeling by getting some much"
		print "needed rest. You find shade under the palm tree and place your knapsack on the"
		print "ground to use as a pillow. You begin to drift off... THUUUUD!"
		
		print "\n...................................."
		
		print "\nYou blink a couple times and slowly begin to rub your head. You can feel the"
		print "different parts of your brain booting up... similar to a computer loading it's" 
		print "processes after startup. Your unfamiliarity with the surroundings finally"
		print "begins to sink in as an overwhelming sense of dread quickly climbs up your"
		print "spine and squeezes the air out of your lungs leaving you gasping for breath."
				
		print "\nYou bolt upright, disoriented and scared. It takes you a moment to realize how"
		print "loud your gasping due to the ringing in your ears silencing you from the"
		print "outside world."
				
		print "\nYour memory is full of gaps as you begin trying to piece together what's going"
		print "on. Before you try and figure out what happened you decide you need to figure"
		print "out who you are exactly.\n"
		me.save_to_scores()
		os.system('pause')
		exit(0)

# ---------- End of Scene Base Classes/Subclasses -----------	
# -----------------------------------------------------------


# -----------------------------------------------------------
# ------------ Character Base Classes/Subclasses ------------		
class Character(object):
	
	def __init__(self):
		self.name = ""
		# Non combat related attributes
		self.charisma = 0
		self.intelligence = 0
		self.luck = 0
		# Combat related attributes
		self.agility = 0
		self.endurance = 0
		self.strength = 0
		self.max_health = 100
		self.current_health = 100
		self.armor_rating = 0
		self.weapon_rating = 0
		
	def do_damage_balanced(self, enemy):
		# Checks whether someone has been dropped to zero health
		if enemy.current_health > 0 and self.current_health > 0:
			self.damage = random.randint(5,(20 + self.attack_rating_modified))
			self.damage_after_mitigation = (self.damage - enemy.defense_rating_modified)
			# Checks whether enemy armor is strong enough to prevent damage 
			if self.damage <= enemy.defense_rating_modified and enemy.defense_rating_modified > 0:
				enemy.current_health = enemy.current_health
				print "%s's defense rating of %d prevents damage from %s." % (enemy.name, enemy.defense_rating_modified, self.name)
				print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to mitigate some of the damage
			elif self.damage > enemy.defense_rating_modified and enemy.defense_rating_modified > 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'normal'
					print "%s's defense rating of %d mitigates %d damage from %s," % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified, self.name)
					print "only allowing %d damage through." % self.damage_after_mitigation
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						enemy.loot_drop()
						self.enemies_killed.append(enemy.name)
						# This adds the points given for killing the enemy to the user's score.
						print "You gain %d points to your score." % self.enemy.score
						self.score += self.enemy.score
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.defense_rating_modified = self.defense_rating
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "---------------------------------- GAME OVER ----------------------------------"
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s's defense rating of %d mitigates %d damage from %s," % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified, self.name)
					print "only allowing %d damage through." % self.damage_after_mitigation
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether the enemy is hit directly with your attack
			elif self.damage > 0 and enemy.defense_rating_modified == 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage <= 0:
					enemy.current_health = 0
					self.state = 'normal'
					print "%s suffers %d damage from %s's attack!" % (enemy.name, self.damage, self.name)
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						enemy.loot_drop()
						self.enemies_killed.append(enemy.name)
						# This adds the points given for killing the enemy to the user's score.
						print "You gain %d points to your score." % self.enemy.score
						self.score += self.enemy.score
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.defense_rating_modified = self.defense_rating
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "---------------------------------- GAME OVER ----------------------------------"
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still is alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage
					print "%s suffers %d damage from %s's attack!" % (enemy.name, self.damage, self.name)
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy is fast enough to evade your attack
			elif self.damage == 0:
				enemy.current_health = enemy.current_health
				print "%s evades %s's attack!" % (enemy.name, self.name)
				print "%s has %d health remaining." % (enemy.name, enemy.current_health)
	
	def do_damage_aggressive(self, enemy):
		# Checks whether someone has been dropped to zero health
		if enemy.current_health > 0 and self.current_health > 0:
			self.damage = random.randint(0,(25 + self.attack_rating_modified))
			self.damage_after_mitigation = (self.damage - enemy.defense_rating_modified)
			# Checks whether enemy armor is strong enough to prevent damage 
			if self.damage <= enemy.defense_rating_modified and enemy.defense_rating_modified > 0:
				enemy.current_health = enemy.current_health
				print "%s's defense rating of %d prevents damage from %s." % (enemy.name, enemy.defense_rating_modified, self.name)
				print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to mitigate some of the damage
			elif self.damage > enemy.defense_rating_modified and enemy.defense_rating_modified > 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'normal'
					print "%s's defense rating of %d mitigates %d damage from %s," % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified, self.name)
					print "only allowing %d damage through." % self.damage_after_mitigation
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						enemy.loot_drop()
						self.enemies_killed.append(enemy.name)
						# This adds the points given for killing the enemy to the user's score.
						print "You gain %d points to your score." % self.enemy.score
						self.score += self.enemy.score
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.defense_rating_modified = self.defense_rating
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "---------------------------------- GAME OVER ----------------------------------"
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s's defense rating of %d mitigates %d damage from %s," % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified, self.name)
					print "only allowing %d damage through." % self.damage_after_mitigation
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether the enemy is hit directly with your attack
			elif self.damage > 0 and enemy.defense_rating_modified == 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage <= 0:
					enemy.current_health = 0
					self.state = 'normal'
					print "%s suffers %d damage from %s's attack!" % (enemy.name, self.damage, self.name)
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						enemy.loot_drop()
						self.enemies_killed.append(enemy.name)
						# This adds the points given for killing the enemy to the user's score.
						print "You gain %d points to your score." % self.enemy.score
						self.score += self.enemy.score
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.defense_rating_modified = self.defense_rating
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "---------------------------------- GAME OVER ----------------------------------"
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still is alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage
					print "%s suffers %d damage from %s's attack!" % (enemy.name, self.damage, self.name)
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy is fast enough to evade your attack
			elif self.damage == 0:
				enemy.current_health = enemy.current_health
				print "%s evades %s's attack!" % (enemy.name, self.name)
				print "%s has %d health remaining." % (enemy.name, enemy.current_health)
	
	def do_damage_controlled(self, enemy):
		# Checks whether someone has been dropped to zero health
		if enemy.current_health > 0 and self.current_health > 0:
			self.damage = random.randint(10,(15 + self.attack_rating_modified))
			self.damage_after_mitigation = (self.damage - enemy.defense_rating_modified)
			# Checks whether enemy armor is strong enough to prevent damage 
			if self.damage <= enemy.defense_rating_modified and enemy.defense_rating_modified > 0:
				enemy.current_health = enemy.current_health
				print "%s's defense rating of %d prevents damage from %s." % (enemy.name, enemy.defense_rating_modified, self.name)
				print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy armor is strong enough to mitigate some of the damage
			elif self.damage > enemy.defense_rating_modified and enemy.defense_rating_modified > 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage_after_mitigation <= 0:
					enemy.current_health = 0
					self.state = 'normal'
					print "%s's defense rating of %d mitigates %d damage from %s," % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified, self.name)
					print "only allowing %d damage through." % self.damage_after_mitigation
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						enemy.loot_drop()
						self.enemies_killed.append(enemy.name)
						# This adds the points given for killing the enemy to the user's score.
						print "You gain %d points to your score." % self.enemy.score
						self.score += self.enemy.score
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.defense_rating_modified = self.defense_rating
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "---------------------------------- GAME OVER ----------------------------------"
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage_after_mitigation
					print "%s's defense rating of %d mitigates %d damage from %s," % (enemy.name, enemy.defense_rating_modified, enemy.defense_rating_modified, self.name)
					print "only allowing %d damage through." % self.damage_after_mitigation
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether the enemy is hit directly with your attack
			elif self.damage > 0 and enemy.defense_rating_modified == 0:
				# Prevents the enemies health from being a negative value
				if enemy.current_health - self.damage <= 0:
					enemy.current_health = 0
					self.state = 'normal'
					print "%s suffers %d damage from %s's attack!" % (enemy.name, self.damage, self.name)
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
					# Check if drop_table exists in enemy's class
					if hasattr(enemy, 'drop_table'):
						enemy.loot_drop()
						self.enemies_killed.append(enemy.name)
						# This adds the points given for killing the enemy to the user's score.
						print "You gain %d points to your score." % self.enemy.score
						self.score += self.enemy.score
						# This resets modified stats of user back to base after battle.
						self.attack_rating_modified = self.attack_rating
						self.defense_rating_modified = self.defense_rating
					# Otherwise, the player (who is without a 'drop_table') must have died
					else:
						print "---------------------------------- GAME OVER ----------------------------------"
						me.save_to_scores()
						os.system('pause')
						exit(0)
				# Enemy still is alive after attack
				else:
					enemy.current_health = enemy.current_health - self.damage
					print "%s suffers %d damage from %s's attack!" % (enemy.name, self.damage, self.name)
					print "%s has %d health remaining." % (enemy.name, enemy.current_health)
			# Checks whether enemy is fast enough to evade your attack
			elif self.damage == 0:
				enemy.current_health = enemy.current_health
				print "%s evades %s's attack!" % (enemy.name, self.name)
				print "%s has %d health remaining." % (enemy.name, enemy.current_health)

				
# --------------- Character Subclass Enemy ------------------			
class Enemy(Character):

	def loot_drop(self):
		self.gold_dropped = self.gold
		Player.inventory['gold'] += self.gold_dropped
		self.loot_dropped_category = random.choice(self.drop_table.keys())
		if self.loot_dropped_category == 'potions':
			self.loot_dropped = random.choice(self.drop_table['potions'])
			if self.loot_dropped in Player.inventory['potions']:
				Player.inventory['potions'][self.loot_dropped] += 1
			elif self.loot_dropped not in Player.inventory['potions']:
				Player.inventory['potions'][self.loot_dropped] = 1
			# Checks whether the loot dropped begins with vowel
			if vowel_check(self.loot_dropped) == True:
				print "An %s was dropped along with %d gold! You add it to your inventory." % (self.loot_dropped, self.gold_dropped)
			else:
				print "A %s was dropped along with %d gold! You add it to your inventory." % (self.loot_dropped, self.gold_dropped)
		elif self.loot_dropped_category == 'armor':
			self.loot_dropped = random.choice(self.drop_table['armor'])
			if self.loot_dropped.armor_name in Player.inventory['armor']:
				Player.inventory['armor'][self.loot_dropped.armor_name] += 1
			elif self.loot_dropped.armor_name not in Player.inventory['armor']:
				Player.inventory['armor'][self.loot_dropped.armor_name] = 1
			# Checks whether the loot dropped begins with vowel 	
			if vowel_check(self.loot_dropped.armor_name) == True:
				print "An %s was dropped along with %d gold! You add it to your inventory." % (self.loot_dropped.armor_name, self.gold_dropped)
			else:
				print "A %s was dropped along with %d gold! You add it to your inventory." % (self.loot_dropped.armor_name, self.gold_dropped)
		elif self.loot_dropped_category == 'weapons':
			self.loot_dropped = random.choice(self.drop_table['weapons'])
			if self.loot_dropped.weapon_name in Player.inventory['weapons']:
				Player.inventory['weapons'][self.loot_dropped.weapon_name] += 1
			elif self.loot_dropped.weapon_name not in Player.inventory['weapons']:
				Player.inventory['weapons'][self.loot_dropped.weapon_name] = 1
			# Checks whether the loot dropped begins with vowel	
			if vowel_check(self.loot_dropped.weapon_name) == True:
				print "An %s was dropped along with %d gold! You add it to your inventory." % (self.loot_dropped.weapon_name, self.gold_dropped)
			else:
				print "A %s was dropped along with %d gold! You add it to your inventory." % (self.loot_dropped.weapon_name, self.gold_dropped)
		

# -------------------- Enemy Subclasses ---------------------					
class Goblin(Enemy):
	
	def __init__(self):
		Character.__init__(self)
		self.name = 'Goblin'
		# Non combat related attributes
		self.charisma = 1
		self.intelligence = 2
		self.luck = 2
		# Combat related attributes
		self.agility = 5
		self.endurance = 2
		self.strength = 2
		self.max_health = 65 + (self.endurance * 5)
		self.current_health = 75
		self.armor_rating = 4
		self.defense_rating = self.armor_rating + self.endurance
		self.weapon_rating = 2
		self.attack_rating = self.weapon_rating + self.strength
		# These are needed to allow the same function to perform battle calculations.
		self.defense_rating_modified = self.defense_rating
		self.attack_rating_modified = self.attack_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_balanced
		# Loot
		self.score = 50
		self.gold = 5
		self.drop_table = {
			'potions': ['health potion', 'attack potion'], 
			'armor': [GoblinHelm, GoblinMail],
			'weapons': [GoblinSpear],
			}

			
class Werewolf(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Werewolf'
		# Non combat related attributes
		self.charisma = 1
		self.intelligence = 1
		self.luck = 1
		# Combat related attributes
		self.agility = 7
		self.endurance = 4
		self.strength = 4
		self.max_health = 70 + (self.endurance * 5)
		self.current_health = 80
		self.armor_rating = 0
		self.defense_rating = self.armor_rating + self.endurance
		self.weapon_rating = 4
		self.attack_rating = self.weapon_rating + self.strength
		# These are needed to allow the same function to perform battle calculations.
		self.defense_rating_modified = self.defense_rating
		self.attack_rating_modified = self.attack_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_controlled
		# Loot
		self.score = 100
		self.gold = 10
		self.drop_table = {
			'potions': ['health potion'], 
			}
	

class Ogre(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Ogre'
		# Non combat related attributes
		self.charisma = 1
		self.intelligence = 2
		self.luck = 1
		# Combat related attributes
		self.agility = 2
		self.endurance = 8
		self.strength = 6
		self.max_health = 60 + (self.endurance * 5)
		self.current_health = 100
		self.armor_rating = 0
		self.defense_rating = self.armor_rating + self.endurance
		self.weapon_rating = 5
		self.attack_rating = self.weapon_rating + self.strength
		# These are needed to allow the same function to perform battle calculations.
		self.defense_rating_modified = self.defense_rating
		self.attack_rating_modified = self.attack_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# Loot
		self.score = 200
		self.gold = 20
		self.drop_table = {
			'potions': ['health potion', 'attack potion'],
			'weapons': [OgreAxe],
			}	

	
class Troll(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Troll'
		# Non combat related attributes
		self.charisma = 1
		self.intelligence = 3
		self.luck = 2
		# Combat related attributes
		self.agility = 4
		self.endurance = 6
		self.strength = 5
		self.max_health = 60 + (self.endurance * 5)
		self.current_health = 85
		self.armor_rating = 10
		self.defense_rating = self.armor_rating + self.endurance
		self.weapon_rating = 4
		self.attack_rating = self.weapon_rating + self.strength
		# These are needed to allow the same function to perform battle calculations.
		self.defense_rating_modified = self.defense_rating
		self.attack_rating_modified = self.attack_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# Loot
		self.score = 300
		self.gold = 30
		self.drop_table = {
			'potions': ['health potion'],
			'armor': [TrollPlate, TrollShield],
			'weapons': [TrollClub],
			}
		

class Bandit(Enemy):
			
	def __init__(self):
		Character.__init__(self)
		self.name = 'Bandit'
		# Non combat related attributes
		self.charisma = 4
		self.intelligence = 4
		self.luck = 4
		# Combat related attributes
		self.agility = 6
		self.endurance = 5
		self.strength = 4
		self.max_health = 75 + (self.endurance * 5)
		self.current_health = 100
		self.armor_rating = 10
		self.defense_rating = self.armor_rating + self.endurance
		self.weapon_rating = 4
		self.attack_rating = self.weapon_rating + self.strength
		# These are needed to allow the same function to perform battle calculations.
		self.defense_rating_modified = self.defense_rating
		self.attack_rating_modified = self.attack_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_aggressive
		# Loot
		self.score = 600
		self.gold = 60
		self.drop_table = {
			'potions': ['health potion'],
			'armor': [BanditCoif, BanditShield],
			'weapons': [BanditShortsword],
			}


class Dragon(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Dragon'
		# This enemy has a name because he's the main boss but more so because Alec decided he needed a name.
		self.real_name = 'Nexus'
		# Non combat related attributes
		self.charisma = 8
		self.intelligence = 8
		self.luck = 8
		# Combat related attributes
		self.agility = 8
		self.endurance = 10
		self.strength = 10
		self.max_health = 130 + (self.endurance * 5)
		self.current_health = 180
		self.armor_rating = 10
		self.defense_rating = self.armor_rating + self.endurance
		self.weapon_rating = 8
		self.attack_rating = self.weapon_rating + self.strength
		# These are needed to allow the same function to perform battle calculations.
		self.defense_rating_modified = self.defense_rating
		self.attack_rating_modified = self.attack_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_balanced
		# Loot
		self.score = 1000
		self.gold = 100
		self.drop_table = {
			'potions': ['health potion'],
			'weapons': [DragontoothDagger],
			'armor': [DragonscaleShield],
			}		


class Kraken(Enemy):

	def __init__(self):
		Character.__init__(self)
		self.name = 'Kraken'
		# Non combat related attributes
		self.charisma = 1
		self.intelligence = 6
		self.luck = 6
		# Combat related attributes
		self.agility = 6
		self.endurance = 8
		self.strength = 10
		self.max_health = 100 + (self.endurance * 5)
		self.current_health = 140
		self.armor_rating = 4
		self.defense_rating = self.armor_rating + self.endurance
		self.weapon_rating = 8
		self.attack_rating = self.weapon_rating + self.strength
		# These are needed to allow the same function to perform battle calculations.
		self.defense_rating_modified = self.defense_rating
		self.attack_rating_modified = self.attack_rating
		# This is for allowing enemies to have different attack stances.
		self.attack_type = self.do_damage_controlled
		# Loot
		self.score = 800
		self.gold = 0
		self.drop_table = {
			'potions': ['health potion'],
			}

		
# --------------- Character Subclass Player -----------------			
class Player(Character):

	inventory = {
		'gold': 5,
		'potions': {'health potion': 2, 'attack potion': 2, 'defense potion': 2 },
		'armor': {},
		'weapons': {},
	}
	
	equipment = {
		'helmet': None,
		'chest': None,
		'legs': None,
		'shield': None,
		'weapon': None,
	}
	
	def __init__(self):
		Character.__init__(self)
		self.state = 'normal'
		self.total_attribute_points = 30
		self.max_health = 100
		self.armor_rating_from_attribute = 0
		self.armor_rating_from_equipment = 0
		self.armor_rating = 0
		self.defense_rating = self.armor_rating
		self.weapon_rating_from_equipment = 0
		self.weapon_rating = 0
		self.attack_rating = self.weapon_rating
		self.scenes_visited = []
		self.enemies_killed = []
		self.scene_player_is_in = 'forest'
		self.forest_path_choice = 0
		self.swamp_shack_choice = 0
		self.meadow_path_choice = 0
		self.inside_troll_cave_choice = 0
		self.mountain_path_choice = 0
		self.old_bridge_fight_choice = 0
		self.other_mountain_path_choice = 0
		self.score = 0
		
	def quit(self):
		are_you_sure = raw_input("Are you sure you want to quit? Enter yes or no: ")
		if are_you_sure.upper() == 'YES':
			print "You choose the coward's way out..."
			print "---------------------------------- GAME OVER ----------------------------------"
			me.save_to_scores()
			os.system('pause')
			exit(0)
		elif are_you_sure.upper() == 'NO':
			print "You change your mind and continue on with your journey."
		else:
			print "Your inability to read is alarming... you don't seem like hero material."
	
	def help(self):
		print "To access any of the player commands simply type any of the following:\n"
		print 'quit 		| Give up and accept defeat'
		print 'help 		| Displays available commands'
		print 'load scores	| Displays information on past participants'
		print 'explore		| Continue on with the journey'
		print 'inventory 	| Displays user inventory'
		print 'equipment	| Displays user equipment currently worn'
		print 'equip armor 	| Prompts user to enter a piece of armor to equip'
		print 'equip weapon	| Prompts user to enter a weapon to equip'
		print 'use potion 	| Prompts user to enter a potion to drink'
		print 'enemy status	| Displays enemy status'
		print 'status 		| Displays user status'
		print 'show stances	| Displays attack stances that are available' 
		print 'attack		| Prompts user to enter attack stance to use'
		print 'escape		| Attempt to flee from the current enemy'
		
	def status(self):
		print "---------------------"
		print "Health: %d/%d" % (me.current_health, me.max_health)
		print "State: %s" % me.state
		print "Attack rating: %d" % me.attack_rating_modified
		print "Defense rating: %d" % me.defense_rating_modified
		attribute_scores()
		
	def enemy_status(self):
		print "---------------------"
		print "Health: %d/%d" % (me.enemy.current_health, me.enemy.max_health)
		print "Attack rating: %d" % me.enemy.attack_rating_modified
		print "Defense rating: %d" % me.enemy.defense_rating_modified
		print "---------------------"
		print "Intelligence: %d" % me.enemy.intelligence
		print "Luck: %d" % me.enemy.luck
		print "Charisma: %d" % me.enemy.charisma
		print "Agility: %d" % me.enemy.agility
		print "Strength: %d" % me.enemy.strength
		print "Endurance: %d" % me.enemy.endurance
		print "---------------------"
	
	def explore(self):
		if self.state != 'normal':
			print "Finish what you are doing first before trying to explore!"
		else:
			if self.scene_player_is_in == 'forest' and self.forest_path_choice == '1':
				Scenes['meadow'].enter()
			elif self.scene_player_is_in == 'forest' and self.forest_path_choice == '2':
				Scenes['swamp'].enter()
			elif self.scene_player_is_in == 'swamp':
				Scenes['meadow'].enter()
			elif self.scene_player_is_in == 'meadow' and self.meadow_path_choice == '2' and self.scenes_visited.count('troll cave') == 0:
				Scenes['troll cave'].enter()
			elif self.scene_player_is_in == 'meadow' and self.scenes_visited.count('swamp') == 0 and self.scenes_visited.count('troll cave') == 0:
				Scenes['troll cave'].enter()
			elif self.scene_player_is_in == 'troll cave' and self.inside_troll_cave_choice == '1':
				Scenes['cave passage'].enter()
			elif self.scene_player_is_in == 'cave passage':
				Scenes['dragon cave'].enter()
			elif self.scene_player_is_in == 'troll cave' and self.enemies_killed.count('Werewolf') == 0 and self.meadow_path_choice == '2':
				Scenes['meadow'].enter()
			elif self.scene_player_is_in == 'troll cave' and self.enemies_killed.count('Werewolf') == 0 and self.meadow_path_choice == 0:
				Scenes['meadow'].enter()
			elif self.scene_player_is_in == 'meadow' and self.meadow_path_choice == '1':  
				Scenes['mountain'].enter()
			elif self.scene_player_is_in == 'meadow' and self.scenes_visited.count('meadow') >= 2:
				Scenes['mountain'].enter()
			elif self.scene_player_is_in == 'meadow':
				Scenes['troll cave'].enter()
			elif self.scene_player_is_in == 'troll cave' and self.inside_troll_cave_choice == '2':
				Scenes['mountain'].enter()
			elif self.scene_player_is_in == 'mountain' and self.mountain_path_choice == '1' and self.scenes_visited.count('dragon cave') == 0:
				Scenes['old bridge'].enter()
			elif self.scene_player_is_in == 'mountain' and self.mountain_path_choice == '2' :
				Scenes['water'].enter()
			elif self.scene_player_is_in == 'mountain' and self.scenes_visited.count('dragon cave') > 0:
				Scenes['water'].enter()
			elif self.scene_player_is_in == 'mountain': 
				Scenes['mountain'].enter()
			elif self.scene_player_is_in == 'old bridge' and self.scenes_visited.count('old bridge') > 1:
				Scenes['mountain'].enter()
			elif self.scene_player_is_in == 'old bridge' and self.scenes_visited.count('cave passage') > 0:
				Scenes['old bridge'].enter()
			elif self.scene_player_is_in == 'old bridge': 
				Scenes['other mountain'].enter()
			elif self.scene_player_is_in == 'other mountain' and self.other_mountain_path_choice == '2' and self.scenes_visited.count('dragon cave') > 0:
				Scenes['old bridge'].enter()
			elif self.scene_player_is_in == 'other mountain' and self.other_mountain_path_choice == '1':
				Scenes['water'].enter()
			elif self.scene_player_is_in == 'other mountain' and self.other_mountain_path_choice == '2':
				Scenes['dragon cave'].enter()
			elif self.scene_player_is_in == 'dragon cave':
				Scenes['other mountain'].enter()
			elif self.scene_player_is_in == 'water':
				Scenes['island'].enter()
					
	def show_inventory(self):
		print "ARMOR"
		for armor in self.inventory['armor']:
			print armor
		print "------------------------"
		
		print "WEAPONS"
		for weapons in self.inventory['weapons']:
			print weapons
		print "------------------------"	
		
		print "POTIONS"
		for potions in self.inventory['potions']:
			print potions, 
			print "x%d" % self.inventory['potions'][potions]
		print "------------------------"
		
		print "GOLD: %d" % self.inventory['gold']
		
	def show_equipment(self):
		print "-----------------------------------------------------"
		for slot in self.equipment:
			if self.equipment[slot] != None:
				if slot != 'weapon':
					armor_in_slot = self.equipment[slot].armor_name
					print "You are wearing %s in the %s slot." % (armor_in_slot, slot)
				else:
					weapon_in_slot = self.equipment[slot].weapon_name
					print "You are wielding %s in the %s slot." % (weapon_in_slot, slot)
			else:
				if slot != 'weapon':
					print "You are wearing no item in the %s slot." % slot
				else:
					print "You are wielding no item in the %s slot" % slot
		print "-----------------------------------------------------"		
	def equip_armor(self):
		for the_armor in self.inventory['armor']:
			armor_instance = LookupArmor.get(the_armor)
			if armor_instance.is_equipped:
				self.equipment[armor_instance.armor_type] = armor_instance
				continue
	
	def equip_weapon(self):
		for the_weapon in self.inventory['weapons']:
			weapon_instance = LookupWeapon.get(the_weapon)
			if weapon_instance.is_equipped:
				self.equipment['weapon'] = weapon_instance
				continue
		
	def use_potion(self, potion_used):
		self.potion_used = potion_used
		if self.potion_used in self.inventory['potions']:
			if self.inventory['potions'][self.potion_used] > 0:
				self.inventory['potions'][self.potion_used] -= 1
				if self.potion_used == 'health potion':
					if self.current_health + (self.max_health / 5) > self.max_health:
						self.health_gained = self.max_health - self.current_health
						self.current_health = self.max_health
						print "You gained %d health from drinking the health potion." % self.health_gained
					else:
						self.current_health += (self.max_health / 5)
						self.health_gained = (self.max_health / 5)
						print "You gain %d health from drinking the health potion." % self.health_gained
				elif self.potion_used == 'attack potion':
					self.attack_rating_modified += 4
					print "You temporarily gain 4 attack rating from drinking the attack potion."
				elif self.potion_used == 'defense potion':
					self.defense_rating_modified += 4
					print "You temporarily gain 4 defense rating from drinking the defense potion."
			else:
				print "You ran out of that potion."
		else:
			print "You don't have a potion with that name."
					
	def escape(self):
		if self.state != 'in combat':
			print "You can only escape when you're currently fighting!"
		else:
			if random.randint(1, 20 + self.enemy.agility) >= (5 + self.agility):
				print "You were unable to escape from %s!" % self.enemy.name
				self.enemy.do_damage_balanced(self)
			else:
				print "You advance in a different direction from %s..." % self.enemy.name
				self.enemy = None
				self.state = 'normal'
	
	def show_stances(self):
		print "Controlled: Medium damage, high accuracy."
		print "Balanced: Low to high damage, medium accuracy."
		print "Aggressive: Low to very high damage, low accuracy."
	
	def attack(self):
		if self.state != 'in combat':
			print "There's nothing to attack!"
		else:
			attack_style = raw_input("Which attack stance do you use? ").title()
			if attack_style == 'Controlled':
				if self.agility >= self.enemy.agility:
					self.do_damage_controlled(self.enemy)
					self.enemy.attack_type(self)
				else:
					self.enemy.attack_type(self)
					self.do_damage_controlled(self.enemy)
			elif attack_style == 'Balanced':
				if self.agility >= self.enemy.agility:
					self.do_damage_balanced(self.enemy)
					self.enemy.attack_type(self)
				else:
					self.enemy.attack_type(self)
					self.do_damage_balanced(self.enemy)
			elif attack_style == 'Aggressive':
				if self.agility >= self.enemy.agility:
					self.do_damage_aggressive(self.enemy)
					self.enemy.attack_type(self)
				else:
					self.enemy.attack_type(self)
					self.do_damage_aggressive(self.enemy)
			else:
				print "You don't have an attack stance with that name currently available."
	
	def save_to_scores(self):
		fname = "Memory Loss Scores.txt"
		if os.path.isfile(fname):
			with open(fname, "a+") as myfile:
				myfile.write("Name: %s | Score: %d" % (me.name, me.score))
		else:
			with open(fname, "a+") as myfile:
				myfile.write("Name: %s | Score: %d" % (me.name, me.score))
	
	def load_scores(self):
		fname = "Memory Loss Scores.txt"
		if os.path.isfile(fname):
			with open(fname, "r+") as myfile:
				for line in myfile:
					print line,
		else:
			print "There are no scores to load yet."
	
	def health_check(self):
		if self.current_health == 0:
			print "You have 0 health remaining."
			print "---------------------------------- GAME OVER ----------------------------------"
			me.save_to_scores()
			os.system('pause')
			exit(0)
		else:
			print "You have %d health remaining." % me.current_health


# --------- End of Character Base Classes/Subclasses --------
# -----------------------------------------------------------


# --------------------- Scene Dictionary --------------------	
Scenes = {
	'forest': Forest(),
	'meadow': Meadow(),
	'swamp': Swamp(),
	'troll cave': TrollCave(),
	'cave passage': CavePassage(),
	'dragon cave': DragonCave(),
	'mountain': Mountain(),
	'other mountain': OtherMountain(),
	'old bridge': OldBridge(),
	'water': Water(),
	'island': Island(),
}
	

# ------------------- Commands Dictionary -------------------		
Commands = {
	'quit': Player.quit,
	'help': Player.help,
	'load scores': Player.load_scores,
	'status': Player.status,
	'enemy status': Player.enemy_status,
	'explore': Player.explore,
	'inventory': Player.show_inventory,
	'equipment': Player.show_equipment,
	'equip armor': Player.equip_armor,
	'equip weapon': Player.equip_weapon,
	'use potion': Player.use_potion,
	'escape': Player.escape,
	'show stances': Player.show_stances,
	'attack': Player.attack,
}		


# -------------------- Armor Dictionary ---------------------
LookupArmor = {
	'Goblin Helm': GoblinHelm(),
	'Goblin Mail': GoblinMail(),
	'Troll Plate': TrollPlate(),
	'Troll Shield': TrollShield(),
	'Chainmail Chausses': ChainmailChausses(),
	'Chainmail Hauberk': ChainmailHauberk(),
	'Bandit Coif': BanditCoif(),
	'Bandit Shield': BanditShield(),
	'Dragonscale Shield': DragonscaleShield(),
}


# -------------------- Weapon Dictionary --------------------
LookupWeapon = {
	'Goblin Spear': GoblinSpear(),
	'Ogre Axe': OgreAxe(),
	'Large Cleaver': LargeCleaver(),
	'Troll Club': TrollClub(),
	'Bandit Shortsword': BanditShortsword(),
	'Dragontooth Dagger': DragontoothDagger(),
}

# -----------------------------------------------------------
# --------- Instantiate Player/Start of Adventure -----------
me = Player()
print "\n-------------------------------------------------------------------------------"
print "\nYou blink a couple times and slowly begin to rub your head. You can feel the"
print "different parts of your brain booting up... similar to a computer loading it's" 
print "processes after startup. You look around and can only see branches, leaves, and"
print "trunks in every direction. Your unfamiliarity with the surroundings finally"
print "begins to sink in as an overwhelming sense of dread quickly climbs up your"
print "spine and squeezes the air out of your lungs leaving you gasping for breath."
		
print "\nYou bolt upright, disoriented and scared. It takes you a moment to realize how"
print "loud your gasping due to the ringing in your ears silencing you from the"
print "outside world."
		
print "\nYour memory is full of gaps as you begin trying to piece together what's going"
print "on. Before you try and figure out what happened you decide you need to figure"
print "out who you are exactly.\n"

me.name = raw_input("What is my name? ")
print "After a brief pause you remember that it's %s." % me.name


def attribute_scores():
	print "---------------------"
	print "Intelligence: %d" % me.intelligence
	print "Luck: %d" % me.luck
	print "Charisma: %d" % me.charisma
	print "Agility: %d" % me.agility
	print "Strength: %d" % me.strength
	print "Endurance: %d" % me.endurance
	print "Score: %d" % me.score
	print "---------------------"

	
def attribute_effects():
	me.max_health = 100 + (me.endurance * 5)
	me.current_health = me.max_health
	me.defense_rating += me.endurance
	me.attack_rating += me.strength
		
	
print "\nYou then begin trying to describe yourself."
print "You slowly start to remember your strengths and weaknesses."
print "\n-------------------------------------------------------------------------------"
print "\nYou have 30 attribute points left to assign."
print "There are six main attributes: Intelligence, Luck, Charisma, Agility, Strength,"
print "and Endurance.\n"
print "Intelligence increases decision making skills throughout the adventure."
print "Luck alters unfortunate events throughout the adventure."
print "Charisma opens up alternative dialogue options throughout the adventure."
print "Agility determines attack order, escaping battle, and safety during exploring."
print "Strength increases your attack rating and may be needed during exploring."
print "Endurance increases your defense rating and maximum health.\n"

idiot_tax = 0

while True:
	try:
		me.intelligence = int(raw_input("Please enter your Intelligence rating between 1 - 10: "))
		if me.intelligence < 1 or me.intelligence > 10:
			print "You may only assign a rating between 1 - 10 for Intelligence. Start over.\n"
			idiot_tax += 1
			me.total_attribute_points = 30
			attribute_points_remaining = 30
			continue	
		else:
			attribute_points_remaining = me.total_attribute_points - me.intelligence
			print "You have %d attribute points remaining." % attribute_points_remaining
		
		
		me.luck = int(raw_input("Please enter your Luck rating between 1 - 10: "))
		attribute_points_remaining -= me.luck
		if me.luck < 1 or me.luck > 10:
			print "You may only assign a rating between 1 - 10 for Luck. Start over.\n"
			idiot_tax +=1
			continue
		elif attribute_points_remaining < 4:
			print "You don't have enough points left to allot each attribute with atleast"
			print "a single point. Start over.\n"
			idiot_tax += 1
			continue			
		else:
			print "You have %d attribute points remaining." % attribute_points_remaining
		
		
		me.charisma = int(raw_input("Please enter your Charisma rating between 1 - 10: "))
		attribute_points_remaining -= me.charisma
		if me.charisma < 1 or me.charisma > 10:
			print "You may only assign a rating between 1 - 10 for Charisma. Start over.\n"
			idiot_tax += 1
			continue
		elif attribute_points_remaining < 3:
			print "You don't have enough points left to allot each attribute with atleast"
			print "a single point. Start over.\n"
			idiot_tax += 1
			continue
		else:
			print "You have %d attribute points remaining." % attribute_points_remaining
		
		
		me.agility = int(raw_input("Please enter your Agility rating between 1 - 10: "))
		attribute_points_remaining -= me.agility
		if me.agility < 1 or me.agility > 10:
			print "You may only assign a rating between 1 - 10 for Agility. Start over.\n"
			idiot_tax += 1
			continue
		elif attribute_points_remaining < 2:
			print "You don't have enough points left to allot each attribute with atleast"
			print "a single point. Start over.\n"
			idiot_tax += 1
			continue
		else:
			print "You have %d attribute points remaining." % attribute_points_remaining
			
		
		me.strength = int(raw_input("Please enter your Strength rating between 1 - 10: "))
		attribute_points_remaining -= me.strength
		if me.strength < 1 or me.strength > 10:
			print "You may only assign a rating between 1 - 10 for Strength. Start over.\n"
			idiot_tax += 1
			continue
		elif attribute_points_remaining < 1:
			print "You don't have enough points left to allot each attribute with atleast"
			print "a single point. Start over.\n"
			idiot_tax += 1
			continue
		else:
			print "You have %d attribute points remaining." % attribute_points_remaining
		
		
		me.endurance = int(raw_input("Please enter your Endurance rating between 1 - 10: "))
		attribute_points_remaining -= me.endurance
		if me.endurance < 1 or me.endurance > 10:
			print "You may only assign a rating between 1 - 10 for Endurance. Start over.\n"
			idiot_tax += 1
			continue
		else:
			if attribute_points_remaining > 0:
				print "You didn't use all of your attribute points. Start over.\n"
				idiot_tax += 1
				continue
			elif attribute_points_remaining < 0:
				print "You spent more than the 20 points allotted to you. Start over.\n"
				idiot_tax += 1
				continue
			elif idiot_tax > 0:
				print "\nYou rated yourself as follows:\n"
				print "Intelligence: %d; however, you lose %d point(s) because clearly you aren't as" % (me.intelligence, idiot_tax)
				print "smart as you think you are..."
				
				intelligence_after_tax = me.intelligence - idiot_tax
				if intelligence_after_tax <= 0:
					print "Your Intelligence has been reduced to 0. You clearly don't have what it takes"
					print "to be a hero."
					print "---------------------------------- GAME OVER ----------------------------------"
					me.save_to_scores()
					os.system('pause')
					exit(0)
				else:
					me.intelligence = intelligence_after_tax
					attribute_scores()
					attribute_effects()
			else:
				attribute_scores()
				attribute_effects()
		break
	except ValueError:
		print "Please enter only integers for your attribute ratings. Start over.\n"
		idiot_tax += 1

me.attack_rating_modified = me.attack_rating
me.defense_rating_modified = me.defense_rating
		
print "\n(type help to get a list of actions)"
start_the_game = Scenes['forest'].enter()

# ------------- Command Checking and Execution --------------
while(me.current_health > 0):
	command = raw_input("\nWhat do you do next? ").lower()
	if command not in Commands.keys():
		commandFound = False
		print "%s doesn't understand that command." % me.name
	else:
		for c in Commands.keys():
			if command == 'use potion':
				potion_choice = raw_input("Which potion do you want to use? ").lower()
				Commands['use potion'](me, potion_choice)
				commandFound = True
				break
			elif command == 'equip armor':
				armor_choice = raw_input("Which armor would you like to equip? ").title()
				armor_choice_instance = LookupArmor.get(armor_choice)
				if armor_choice_instance is not None:
					if armor_choice_instance.armor_name in Player.inventory['armor'] and Player.inventory['armor'][armor_choice_instance.armor_name] > 0:
						if Player.equipment[armor_choice_instance.armor_type] is not None:
							unequipped_armor = Player.equipment[armor_choice_instance.armor_type]
							unequipped_armor_name = Player.equipment[armor_choice_instance.armor_type].armor_name 
							Player.inventory['armor'][unequipped_armor_name] += 1
							me.armor_rating_from_equipment = unequipped_armor.armor_rating
							me.defense_rating_modified -= me.armor_rating_from_equipment
							Player.equipment[armor_choice_instance.armor_type].unequip()
						
						Player.inventory['armor'][armor_choice] -= 1
						armor_choice_instance.equip()
						me.armor_rating_from_equipment = armor_choice_instance.armor_rating
						me.defense_rating_modified += me.armor_rating_from_equipment
						Commands['equip armor'](me)
						CommandFound = True
						break
				else:
					print "You don't have any armor with that name in your inventory."
					break
			elif command == 'equip weapon':
				weapon_choice = raw_input("Which weapon would you like to equip? ").title()
				weapon_choice_instance = LookupWeapon.get(weapon_choice)
				if weapon_choice_instance is not None:
					if weapon_choice_instance.weapon_name in Player.inventory['weapons'] and Player.inventory['weapons'][weapon_choice_instance.weapon_name] > 0:
						if Player.equipment['weapon'] is not None:
							unequipped_weapon = Player.equipment['weapon'].weapon_name
							Player.inventory['weapons'][unequipped_weapon] += 1
							me.attack_rating_modified -= me.weapon_rating_from_equipment
							me.weapon_rating_from_equipment -= Player.equipment['weapon'].weapon_rating
							Player.equipment['weapon'].unequip()
						
						Player.inventory['weapons'][weapon_choice] -= 1
						weapon_choice_instance.equip()
						me.weapon_rating_from_equipment += weapon_choice_instance.weapon_rating
						me.attack_rating_modified += me.weapon_rating_from_equipment
						Commands['equip weapon'](me)
						CommandFound = True
						break
				else:
					print "You don't have any weapons with that name in your inventory."
					break
			elif c == command:
				Commands[c](me)
				commandFound = True
				break

