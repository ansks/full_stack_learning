# # # Scope
# x = 50

# def hello():
    
#     # print('Value of x: ', x )

#     # x = 20
    
#     def double_hello():

#         print('Value of nested x: ', x)

#     double_hello()
#     # print('New value of x is {}'.format(x))


# hello()

# print('Global value of x', x)


#################### OOP ################################
# In python, everything is an object. 

# print(type(1))
# print(type('str'))
# print(type([1,2,3]))
# print(type((1,'m')))
# print(type({'A': 1}))

# How can we create our own object on which we can apply methods. This is done using class.
# Instances are specific object created in a class.
# Attributes are characterstics of the object. Methods are operation, we can perform on the object.

# my_list = [1, 2, 3]  #This is an instance of list object.
# print(type(my_list))

# Functions are lower case and Classses are Capitalised. 
# Example 1
# class Sample():
#     pass

# x = Sample()

# print(type(x))

# Example 2
# class Dog():   # Defining/Initialization of a class object named Dog. __init__ is called automatically. 

#     # Class Object Attributes

#     species  = 'mammal'

#     def __init__(self, breed, name):   # __init_ provides the reference to the object through self keyword. 
#                                  # self object which refers to Dog object has one attribute "breed".
#                                  # which is passed as during the instantiation.
        
#         self.breed = breed       # An instance of the breed. 
#         self.name = name

# my_dog = Dog(breed='lab', 
#              name='Junglee')   # Creating an instance of Dog Class. "breed", names are required as arguments. 
# # my_other_dog = Dog(breed='Husky')

# print(my_dog.breed)         # calling the instance back
# print(my_dog.name)         # calling the instance back
# print(my_dog.species)         # calling the instance back

# print(my_other_dog.breed)   # calling the instance back

## Example 3
# class Area():

#     const = 0.5

#     def __init__(self, shape_type = 't', side_a= 1, side_b = 2):
    
#         self.shape_type = shape_type
#         self.side_a = side_a
#         self.side_b = side_b

#     def area(self):
        
#         if self.shape_type == 't':
#             return Area.const * self.side_a * self.side_b
        
#         if self.shape_type == 'r':
#             return self.side_a * self.side_b
        
#     # changing values of default parameters:

#     def change_side_a(self, new_side_a):
#         self.side_a = new_side_a
        
        
# area_t = Area('t', 2, 3)
# area_d = Area()
# area_r = Area('r', 45, 40)

# # print(area_t.side_a)
# # print(area_t.side_b)

# print(area_t.area())
# print(area_d.area())
# print(area_r.area())


# area_d.change_side_a(49)
# print(area_d.area())

# area_d.side_a = 500
# print(area_d.area())


# Inheritance and Special method: 
# Inheritance: use already existing class (base class) and add more methods to increase Usuability.

# Base Class 
# class PlaneTakeOff():
#     def __init__(self, plane):
#         self.plane  = plane
#         print('1. ' + self.plane + ' airplane standby')
    
#     def boarding(self):
#         print('2. boarding complete')
    
#     def instruction(self):
#         print('3. safety instruction done')

# # Inheritence 
# class Landing(PlaneTakeOff):

#     def __init__(self, plane):
#         self.plane = plane
#         print('4. ' + plane + ' Landing sequence has started.')
    
#     def instruction(self):
#         print('5. landing instruction provided')

#     # Special method

#     def __str__(self):
#         return self.plane + ' plane is currently active.'

# airindia = PlaneTakeOff('airindia')
# airindia
# airindia.boarding()
# airindia.instruction()

# spice_jet = Landing('spice jet')
# spice_jet
# spice_jet.boarding()
# spice_jet.instruction()

# print(spice_jet)



#  OOP Problem:
#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)


from random import shuffle

class Deck:
    
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    
    # pass 

    def __init__(self, suit, cards):
        self.suit = suit
        self.cards = cards
    
    def splitting(self):
        
        deck = []

        # print(self.suit)
        # print(self.cards)

        for card_val in self.cards:
            for suit_val in self.suit:       
                deck.append(suit_val + '_' + card_val)
        
        shuffle(deck)

        player1_cards = deck[:26]
        player2_cards = deck[26:]
        
        return player1_cards, player2_cards

# my_list = [1,2,3]
# shuffle(my_list)
# print(my_list)

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, pile, hand):
        self.pile = pile
        self.hand = hand

    def add_cards(self):

        for card in self.hand:
            self.pile.append(card)
        
        return self.pile
    
    def remove_cards(self):

        for card in self.hand:
            self.pile.pop(self.pile.index(card))

        return self.pile

    # pass

class Player():

    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    
    def __init__(self, name, pile, n_cards):
        self.name = name
        self.n_cards = n_cards
        self.pile = pile

    def checkPile(self):

        if len(self.pile) >= self.n_cards:
            print('Player ' + self.name + ' has enough cards!')
            
            return True

        elif len(self.pile):
            print('Player ' + self.name + ' does not enough cards!')

            return True

        else:
            print('Player ' + self.name + ' finished his cards!\n')
            return False
        
    def play(self):
        
        cards_played = self.pile[:self.n_cards]
        print('Player '+ self.name + ' played {} cards'.format(len(cards_played)))

        return cards_played
        
    # def update_hand(self):
    #     self.hand = cards_played

    # pass

# playerA = Player('A', [], 5)

# playerA.checkPile()
# playerA.play()
   

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
game_on = True

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()                       # Heart, Diamond, Spade, Club
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()    # Cards Value 

cards_played = 1 

player1_name = 'Computer'
player2_name = input('Enter your name to play against computer. \n')

game = Deck(SUITE, RANKS)

# Cards will be Shuffled and equally Distributed.
player1_pile, player2_pile = game.splitting()
print(player1_name + "'s cards \n", player1_pile, '\n' ,player2_name + "'s cards \n", player2_pile , '\n')

cards_in_play = []

while(game_on):

    # Use the 3 classes along with some logic to play a game of war!

    # Player 1 starting the game
    player1_starts = Player(player1_name, player1_pile, cards_played)
    player2_starts = Player(player2_name, player2_pile, cards_played)

    # Player played
    player1_played_cards = player1_starts.play()
    player2_played_cards = player2_starts.play()

    # cards_in_play = cards_in_play + player1_played_cards + player2_played_cards

    if player1_starts.checkPile() and player2_starts.checkPile():

        print('Player: ' + player1_name + '\n played: ', player1_played_cards, 
              '\n Card Value: ', player1_played_cards[-1].split('_')[-1],  
              '\n Card Rank: ', RANKS.index(player1_played_cards[-1].split('_')[-1]) , '\n') 
        
        print('Player: ' + player2_name + '\n played: ', player2_played_cards, 
              '\n Card Value: ', player2_played_cards[-1].split('_')[-1],  
              '\n Card Rank: ', RANKS.index(player2_played_cards[-1].split('_')[-1]) , '\n') 
        
        # Hand is being played 
        cards_in_play = cards_in_play + player1_played_cards + player2_played_cards

        print('Cards in Play: ', cards_in_play)

        if RANKS.index(player1_played_cards[-1].split('_')[-1]) > RANKS.index(player2_played_cards[-1].split('_')[-1]):
            
            print('Player ' + player1_name + ' won the round!' , '\n')

            hand_won = Hand(player1_pile, cards_in_play)
            update_pile_1 = Hand(player1_pile, player1_played_cards)
            update_pile_2 = Hand(player2_pile, player2_played_cards)

            player1_pile = update_pile_1.remove_cards()
            player2_pile = update_pile_2.remove_cards()

            player1_pile = hand_won.add_cards()

            print('Player ' + player1_name + "'s updated pile: \n", player1_pile , '\n')
            print('Player ' + player2_name + "'s updated pile: \n", player2_pile , '\n')
            
            cards_in_play = []
            # cards_played = 1

        
        elif RANKS.index(player1_played_cards[-1].split('_')[-1]) < RANKS.index(player2_played_cards[-1].split('_')[-1]):

            print('Player ' + player2_name + ' won the round!' , '\n')
            
            hand_won = Hand(player2_pile, cards_in_play)
            update_pile_1 = Hand(player1_pile, player1_played_cards)
            update_pile_2 = Hand(player2_pile, player2_played_cards)

            player1_pile = update_pile_1.remove_cards()
            player2_pile = update_pile_2.remove_cards()

            player2_pile = hand_won.add_cards()

            print('Player ' + player1_name + "'s updated pile: \n", player1_pile , '\n')
            print('Player ' + player2_name + "'s updated pile: \n", player2_pile , '\n')
            
            cards_in_play = []
            # cards_played = 1

        else:

            update_pile_1 = Hand(player1_pile, player1_played_cards)
            update_pile_2 = Hand(player2_pile, player2_played_cards)

            player1_pile = update_pile_1.remove_cards()
            player2_pile = update_pile_2.remove_cards()

            print('Player ' + player1_name + "'s updated pile: \n", player1_pile , '\n')
            print('Player ' + player2_name + "'s updated pile: \n", player2_pile , '\n')

            cards_played += 1

    else:
        if not len(player1_pile):
            print('!!!!!!!!!!!!! ++++++++++++++++++++++ !!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!! +++           ' + player2_name + '          +++ won the GAME!!!!!!!')
            print('!!!!!!!!!!!!! ++++++++++++++++++++++ !!!!!!!!!!!!!!!!!\n')
        else:
            print('!!!!!!!!!!!!! ++++++++++++++++++++++ !!!!!!!!!!!!!!!!!')
            print('!!!!!!!!!!! +++           ' + player1_name + '          +++ won the GAME!!!!!!!')
            print('!!!!!!!!!!!!! ++++++++++++++++++++++ !!!!!!!!!!!!!!!!!')

        game_on = False
    # Player(player1_name, player1_pile, )






# print(game.cards)
# print(game.suit)

# print(game.splitting())

# hand_ = Hand([1,2,3], ['hq'])

# print(hand_.hand)
# print(hand_.pile)

# hand_.add_cards()
# print(hand_.pile)

# hand_.remove_cards()

# print(hand_.pile)