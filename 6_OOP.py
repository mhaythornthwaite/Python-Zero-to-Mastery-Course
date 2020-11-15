print(f'\n\n')
print(' ---------------- START ---------------- ')

# --------------------- OOP OBJECT ORIENTED PROGRAMMING -----------------------

# Intorducing the idea of OOP - Object Oriented Programming - generating our own classes or data types. Also a way of breaking down and structuring our code. So like we may define a new object say a car and in this we need to specify the engine type, the colour the number of doors etc. and we can also perform methods specific to that object.

class BigCar: #class
	pass

#porshe is an instance of (class) BigCar. We are instanstiating the class BigCar
porshe = BigCar() #instantiate
bmw = BigCar() #instantiate
audi = BigCar() #instantiate

print(type(porshe))
print(type(bmw))
print(type(audi))

#---------------- WIZARD GAME OOP MAKING CLASSES AND METHODS ------------------

class PlayerCharacter:
	membership = True # Class Object Attribute (static not dynamic) same for all objects of that class.
	def __init__(self, paid_member, name, age):
		self.paid_member = paid_member
		if self.paid_member:
		    self.name = name # attributes not a method
		    self.age = age # attribute not a method

	def shout(self): #this is a new method called .run() just for this class
		print(f'My name is {self.name}')
		return ''

	def skill(self, skill_level):
		print(f'My name is {self.name} and I am a {skill_level}')
		return ''

player1  = PlayerCharacter(True, 'matt', 25)
player2 = PlayerCharacter(False, 'Emma', 22)

print(player1.name)
print(player1.age)
print(player1.shout())
print(player1.skill('champion'))
#print(player2.name) #this produces an error message because we have not defined the age because the player has not paid. 


# ------------------- CATS EVERYWHERE EXERCISE: FUNCTIONS ---------------------

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instantiate the 3 cat objects
cat1 = Cat('pat', 4)
cat2 = Cat('percy', 7)
cat3 = Cat('blob', 2)

#Finding the oldest cat
cat_age_list = [cat1.age, cat2.age, cat3.age]
def oldest_cat(*args):
	o_cat = 0
	for cat in cat_age_list:
		if cat > o_cat:
			o_cat = cat
	print(f'The oldest cat is {o_cat} years old')

#Running the function
oldest_cat(cat_age_list)

# ------------------------------ CLASS METHODS --------------------------------

#Class method uses the @classmethod syntax and will WORK WITHOUT THE CLASS BEING INSTANTIATED and instead the method is being applied to the class as opposed to the instance. THESE ARE NOT USED THAT OFTEN. Example below:

class Example:
	def __init__(self, age):
		self.age = age

	@classmethod #have access to the class (cls)
	def adding_things_d(cls, n1, n2): #here cls is shorthand for the class
		return n1 + n2

	@classmethod
	def instantiate_class(cls, n1, n2, n3):
		return cls(n1 + n2 + n3)

	@staticmethod #dont have access to the class (cls)
	def adding_things_s(n1, n2): 
		return n1 + n2


print(f'The answer to this class method without an instance of the class is {Example.adding_things_d(2, 6)}')

#new player created using a class method, in this instance it may not be that interesting but could be useful.
eg1 = Example.instantiate_class(2, 4, 6)
print(eg1.age)


# --------------------------------- SUM UP ------------------------------------

class NameOfClass():
	class_attribute = 'some_value' #same for every instance
	def __init__(self, param1, param2): #different for every instance
		self._param1 = param1
		self._param2 = param2

	def method(self, x):
		print(f'This is param1: {self._param1}, this is x: {x}')

	@classmethod
	def class_method(cls, y):
		print(f'This is the defined class method y: {y}')

	@staticmethod
	def static_method(z):
		print(f'This is the defined static method z: {z}')

test = NameOfClass('PARAM1', 'PARAM2') #instantiate the class
test.method('X') #run method on the new instance

NameOfClass.class_method('Y') #running the class method (no instance)
NameOfClass.static_method('Z') #running the static method (no instance)
print(f'\n')

# ---------------------------- 4 PILLARS OF OOP -------------------------------

#1. ENCAPSULATION, which is the term for wrapping all the information up in an independant capsule, and a way of descibing with code that is closer to theor real world meaning, like creating the class: Car()

#2. ASTRACTION - Hiding information and giving access to only what is necessary, but this can cause a problem because if we do not have access to all the parameters or variables in a newly defined class then we may accidently overwrite them.
#This is where the idea of private vs. public comes into it. Typically we start the variable with an '_name' inside a class which will not be used in the public code, thus preventing any overwriting.

#3. INHERITANCE - New objects to take on the properties of existing objects so we can inherit classes. This allows us to have sub classes. Infact everything in python is already the base class object. So a string is both classed as an object and a string. Below, Player1 is an Archer, a User, a Test and finally an object. So we get the same object .methods for everything in python (they are all dunder methods)

class Test():
	pass

class User(Test): #The 'Test' says that this belongs to the test class
	user_paid = True

class Archer(User): 
	def __init__(self, name, strength):
		self.name = name
		self.strength = strength
	def attack(self):
		print(f'{self.name} attacks with a power of {self.strength}')
		return ''

class Wizard(User):
	def __init__(self, name, height):
		self.name = name
		self.height = height
	def attack(self):
		print(f'The wizard attacks at a mighty height of {self.height} feet.')
		return ''


Player1 = Archer('Robin', 30)
Player1.attack()
Player2 = Wizard('Gandolf', 9)
Player2.attack()
print(Player1.user_paid)
print(Player2.user_paid)

print(f'Is Player 1 a User? {isinstance(Player1, User)}')

#so we can have many parent classes but it appears through testing we may only have one __init__(). 

#4. POLYMORPHISM - A method can have the same name but act differently depending on which class calls them. I.e. a METHOD can have MANY FORMS. So we've already seen this above. When we call .attack() on the different players we get a different result depending on which class of fighter they were. Domostrated again below:

for char in [Player1, Player2]:
	char.attack()

# ------------------------ PETS EVERYWHERE EXERCISE ---------------------------

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self):
    	print('Simon meow')

class Sally(Cat):
    def sing(self):
    	print('Sally meaow')

class Poppy(Cat):
	def sing(self):
		print('Poppy mooo')

#This is possible because Simon is a class type which loops bac to the parent which is Cat and that is where the __init__() is.
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Poppy('Poppy', 1)]

for cat in my_cats:
	cat.sing()

my_pets = Pets(my_cats)

my_pets.walk()
print(f'\n')

# -------------------------- TWO __init__ FUNCTIONS ---------------------------

class User():
	def __init__(self, email):
		self.email = email

	def logged_in(self):
		print('logged in')

class Wizard(User):
	def __init__(self, name, power, email):
		super().__init__(email) #connects to the email in the user class
		self.name = name
		self.power = power

	def attack(self):
		print(f'attaching with power: {self.power}')

p1 = Wizard('Gandalf', 22, 'm.h@yahoo.co.uk')
p1.attack()

# ------------------------------ INTROSPECTION --------------------------------
#when the code is running it allows you to determine the type of an object

print(dir(p1)) #all of the methods the p1 instance has available.


# ----------------------------- DUNDER METHODS --------------------------------

class Toy():
	def __init__(self, color, age):
		self.color = color
		self.age = age
		self.my_dict = {
			'name': 'Fred',
			'calling card': 'whadup'
		}

	def __str__(self):
		return f'your colour is {self.color}'

	def __call__(self):
		return 'Calling this object'

	def __getitem__(self, i):
		return self.my_dict[i]


action_figure = Toy('red', 8)

#the power of special methods or dunder methods comes in when we modify them

print(action_figure.__str__()) #class is Toy so the method is modified
print('action figure'.__str__()) #class is string so method not modified

#the function str() uses the dunder method so the following will return an identical result to above.

print(str(action_figure)) 
print(str('action figure'))

print(action_figure()) #__call__ dunder method is action how functions use () to define an object the function will be called upon. So by defining this function in the class we can use the short had to run the defined method, in this case it says 'calling this object'

print(action_figure['calling card']) #This uses the __getitem__ dunder just modified but I'm not sure how we're calling the method in this instance


# --------------------------- SUPER LIST EXERCISE -----------------------------

#print(type([1,2,3,4]))

init_list = [1, 2, 3, 4, 2, 3]

class SuperList(list):
	def __init__(self, a):
		self.list = a
		pass

	def __len__(self):
		return 1000

super_list_1 = SuperList(init_list)

print(len(super_list_1))

print(super_list_1.list) #prints list
print(super_list_1.list[2]) #prints 2nd index
super_list_1.list.append(9) #appends number 9 to the list
print(super_list_1.list) #prints this new list with 9 appended
print(super_list_1) #super_list_1 without defining that we want the list is simply an empty list because we defined the parent class as a list

print(issubclass(SuperList, list)) #useful if we have many subclasses

# -------------------------- MULTIPLE INHERITANCE -----------------------------

#this is inheriting multiple classes for a single newly defined class, useful if we want the class to have access to the methods and attributes we define in all the classes. 
#So back to the wizards and archers:

class User(): 
	user_paid = True

class Archer(User): 
	def __init__(self, name, strength):
		self.name = name
		self.strength = strength
	def attack_a(self):
		print(f'{self.name} attacks with a power of {self.strength}')
		return ''

class Wizard(User):
	def __init__(self, name, height):
		self.name = name
		self.height = height
	def attack_w(self):
		print(f'The {self.name} attacks at a mighty height of {self.height} feet.')
		return ''

class HybridBorg(Wizard, Archer): #now has access to wizard, archers and user
	def __init__(self, name, strength, height):
		Archer.__init__(self, name, strength) 
		Wizard.__init__(self, name, height)

#above two lines ping the defined attributes: name, strength and height, off to the correct class to make the defined methods in that class work.

Morph_player_1 = HybridBorg('borg', 33, 9)

Morph_player_1.attack_a()
Morph_player_1.attack_w()

#Notice now that whereas before we could have attack method defined in both classes, to get an object with multiple inheritance to work we can not have this. Therefore we have had to sub-divide the attacks. If this is not done Wizard will be done first because of: HybridBorg(Wizard, Archer) (see below also)

#-------------------------- METHOD RESOLUTION ORDER ---------------------------

class A:
	num = 10

class B(A):
	num = 7

class C(A):
	num = 4

class D(B, C):
	pass

#MRO is D B C A because we defined it that way in class D(B, C)
print(D.mro()) #this tells us the above without having to work it out  
print(D.num)

#this can get quite confusing when we skip lines in the tree such as:
# class E(D, A). Does B and C come before A?
#algorithm for doing this is DEPTH ORDER SEARCH. Understanding this is out of scope has has recently been changed but it's important to know that mro can be used to find the result of this algorithm






# ----------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')