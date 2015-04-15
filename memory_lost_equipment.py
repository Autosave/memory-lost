# -----------------------------------------------------------
# ------------ Equipment Base Classes/Subclasses ------------
class Equipment(object):

	def __init__(self):
		self.equipment_type = ""
		self.armor_rating = 0
		self.weapon_rating = 0
		self.is_equipped = False

		
# ------------------- Equipment Subclasses ------------------				
class Weapon(Equipment):
			
	equipment_type = 'weapon'

		
class Armor(Equipment):

	equipment_type = 'armor'

	
# --------------------- Armor Subclasses --------------------	
class Helmet(Armor):
	
	armor_type = 'helmet'


class Chest(Armor):

	armor_type = 'chest'


class Legs(Armor):
	
	armor_type = 'legs'


class Shield(Armor):

	armor_type = 'shield'


# -------------------- General Equipment --------------------
class LargeCleaver(Weapon):

	weapon_name = 'Large Cleaver'
	weapon_rating = 2
	
	def __init__(self):
		self.weapon_name = 'Large Cleaver'
		self.weapon_rating = 2
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.weapon_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.weapon_name


class ChainmailChausses(Legs):

	armor_name = 'Chainmail Chausses'
	armor_rating = 3

	def __init__(self):
		self.armor_name = 'Chainmail Chausses'
		self.armor_rating = 3
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name
		

class ChainmailHauberk(Chest):

	armor_name = 'Chainmail Hauberk'
	armor_rating = 3

	def __init__(self):
		self.armor_name = 'Chainmail Hauberk'
		self.armor_rating = 3
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name
	
	
# --------------------- Goblin Equipment --------------------
class GoblinHelm(Helmet):
	
	armor_name = 'Goblin Helm'
	armor_rating = 2

	def __init__(self):
		self.armor_name = 'Goblin Helm'
		self.armor_rating = 2
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name


class GoblinMail(Chest):
	
	armor_name = 'Goblin Mail'
	armor_rating = 2

	def __init__(self):
		self.armor_name = 'Goblin Mail'
		self.armor_rating = 2
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name
		
		
class GoblinSpear(Weapon):

	weapon_name = 'Goblin Spear'
	weapon_rating = 2
	
	def __init__(self):
		self.weapon_name = 'Goblin Spear'
		self.weapon_rating = 2
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.weapon_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.weapon_name


# ---------------------- Ogre Equipment ---------------------		
class OgreAxe(Weapon):

	weapon_name = 'Ogre Axe'
	weapon_rating = 5
	
	def __init__(self):
		self.weapon_name = 'Ogre Axe'
		self.weapon_rating = 5
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.weapon_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.weapon_name

		
# ---------------------- Troll Equipment --------------------
class TrollPlate(Chest):

	armor_name = 'Troll Plate'
	armor_rating = 6
	
	def __init__(self):
		self.armor_name = 'Troll Plate'
		self.armor_rating = 6
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name

		
class TrollShield(Shield):

	armor_name = 'Troll Shield'
	armor_rating = 4
	
	def __init__(self):
		self.armor_name = 'Troll Shield'
		self.armor_rating = 4
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name
		
	
class TrollClub(Weapon):
	
	weapon_name = 'Troll Club'
	weapon_rating = 4
	
	def __init__(self):
		self.weapon_name = 'Troll Club'
		self.weapon_rating = 4
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.weapon_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.weapon_name
		

# --------------------- Bandit Equipment --------------------				
class BanditCoif(Helmet):
	
	armor_name = 'Bandit Coif'
	armor_rating = 4
	
	def __init__(self):
		self.armor_name = 'Bandit Coif'
		self.armor_rating = 4
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name
		
		
class BanditShield(Shield):

	armor_name = 'Bandit Shield'
	armor_rating = 6
	
	def __init__(self):
		self.armor_name = 'Bandit Shield'
		self.armor_rating = 6
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name
		
	
class BanditShortsword(Weapon):
	
	weapon_name = 'Bandit Shortsword'
	weapon_rating = 4
	
	def __init__(self):
		self.weapon_name = 'Bandit Shortsword'
		self.weapon_rating = 4
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.weapon_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.weapon_name
		
		
# --------------------- Dragon Equipment --------------------
class DragonscaleShield(Shield):

	armor_name = 'Dragonscale Shield'
	armor_rating = 10
	
	def __init__(self):
		self.armor_name = 'Dragonscale Shield'
		self.armor_rating = 10
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.armor_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.armor_name

		
class DragontoothDagger(Weapon):
	
	weapon_name = 'Dragontooth Dagger'
	weapon_rating = 8
	
	def __init__(self):
		self.weapon_name = 'Dragontooth Dagger'
		self.weapon_rating = 8
		self.is_equipped = False
	
	def equip(self):
		self.is_equipped = True
		print "You equipped %s." % self.weapon_name
		
	def unequip(self):
		self.is_equipped = False
		print "You unequipped %s." % self.weapon_name
		
# --------- End of Equipment Base Classes/Subclasses --------
# -----------------------------------------------------------