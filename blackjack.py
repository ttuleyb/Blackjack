from random import shuffle

RANKS = ["2", "3", "4","5", "6", "7", "8", "9", "10", "11", "JACK", "QUEEN", "KING", "ACE"]
SUITS = ["♠", "♥", "♦", "♣"]

class Card:
    def __init__(self, given_rank, given_suit):
        self.rank = given_rank
        self.suit = given_suit

    def __repr__(self):
        return f"{self.rank} {self.suit}"

    def get_value(self):
        if self.rank in RANKS[0:-4]:
            return int(self.rank)
        elif self.rank == "A":
            return 11
        else:
            return 10

    def get_rank(self):
        return self.rank

class Deck:
    def __init__(self):
        self.deck = []

        for rank in RANKS:
            for suit in SUITS:
                card = Card(rank,suit)
                self.deck.append(card)

    def pop_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return None
    
    def shuffle(self):
        return shuffle(self.deck) #shuffles using the random module

class Hand:
    def __init__(self):
        self.hand = []
    
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.hand:
            value += card.get_value()
            rank = card.get_rank()
            if rank == "A":
                num_aces += 1
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value #return an integer representing the value of the Hand

    def show(self):
        for card in self.hand:
            print(card, end=" ")
        print()

    def first_card(self):
        return self.hand[0]

class Player:
    def __init__(self):
        self.hand = Hand()
        self.score = 0
        self.hit = 0

    def add_card(self, card):
        self.hand.add_card(card)
        self.score = self.hand.get_value()

    def show_hand(self):
        print("\nPlayer's hand: ", end="")
        self.hand.show()
        print(f"Player's score:  {self.get_score()}")

    def get_score(self):
        return self.score

class Dealer(Player):
    def __init__(self):
        super().__init__()

    def show_first_card(self):
        print(f"\nDealer's first card: is {self.hand.first_card()}")

    def show_hand(self):
        print("\nDealer's hand: ", end="")
        self.hand.show()
        print(f"Dealer's score: {self.get_score()}")

class Game():
    def replaywithoutreshuffle(self):
        #recreate the players
        self.player = Player()
        self.dealer = Dealer()
        #give the first 2 cards
        for i in range(2):
            self.dealer.add_card(self.deck.pop_card())
            self.player.add_card(self.deck.pop_card())
        #Show dealer's first card
        self.dealer.show_first_card()
        self.mainloop() #restart the game loop
    def results(self):
        #calculate and output results
        winner = ""
        playerscore = self.player.get_score()
        dealerscore = self.dealer.get_score()
        if playerscore > 21: #If the player is busted, Dealer wins
            winner = "Dealer"
        elif dealerscore > 17: #If the dealer is busted Player wins
            winner = "Player"
        elif dealerscore > playerscore: #If the dealer has higher score than the player,
            winner = "Dealer"           #Dealer wins
        elif dealerscore < playerscore: #If the player has higher score than the dealer,
            winner = "Player"           #Player wins
        elif dealerscore == playerscore:#If they have the same score, they draw
            winner = "Draw "
        # output winner
        print(winner + " Wins!")
        choice = input("Would you like to play again without reshuffling? (y/n): ")
        if choice == "y":
            self.replaywithoutreshuffle()
        else:
            exit()

    def mainloop(self):
        while True: #Do forever
            self.player.show_hand() #Show the player their hand
            print(f"Player's score is: {self.player.get_score()}") #Print the score
            if self.player.get_score() >= 21: #If the player's score is greater than 21, break out of loop
                break
            choice = input("Hit or Stand?") #Check if the player is standing or not
            if choice.lower() == "stand": #If the player is standing, break out of loop
                break
            #If not, continue
            self.player.add_card(self.deck.pop_card()) #Add the card to the deck
            playerscore = self.player.get_score()
            print(f"Player's score is: {playerscore}")
            if playerscore <= 21:
                print("Blackjack")
            elif playerscore > 21:
                print("Player is Bust")
                break
        while True:
        #     show dealer hand and score
            self.dealer.show_hand()
            if self.dealer.get_score() >= 17:
                break
            self.dealer.add_card(self.deck.pop_card())
        #     calculate dealer score
            dealerscore = self.dealer.get_score()
        # output player status (if blackjack or bust)
            print(f"Dealer's score is: {dealerscore}")
            if dealerscore <= 17:
                print("Blackjack")
            elif dealerscore > 17:
                print("Dealer is Bust")
                break
        self.results()

    def __init__(self):
        #Create variables
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        #Shuffle the deck
        self.deck.shuffle()
        #give the first 2 cards
        for i in range(2):
            self.dealer.add_card(self.deck.pop_card())
            self.player.add_card(self.deck.pop_card())
        #Show dealer's first card
        self.dealer.show_first_card()
        self.mainloop()


    

if __name__ == '__main__':
    game = Game()
