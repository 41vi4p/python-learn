import random
import time

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()
        
    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        return int(self.rank)
        
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop() if self.cards else None

class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def get_value(self):
        value = 0
        aces = 0
        
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
            value += card.value
            
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
        
    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

class Player:
    def __init__(self, name, bank=1000):
        self.name = name
        self.hand = Hand()
        self.bank = bank
        
    def place_bet(self, amount):
        if amount <= self.bank:
            self.bank -= amount
            return amount
        return 0

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(input("Enter your name: "))
        self.dealer = Player("Dealer")
        
    def play_round(self):
        # Get bet
        while True:
            try:
                bet = int(input(f"\nYour bank: ${self.player.bank}\nPlace your bet: $"))
                if bet > 0 and bet <= self.player.bank:
                    break
                print("Invalid bet amount!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Initial deal
        self.player.hand = Hand()
        self.dealer.hand = Hand()
        
        for _ in range(2):
            self.player.hand.add_card(self.deck.deal())
            self.dealer.hand.add_card(self.deck.deal())
            
        # Show hands
        print(f"\nDealer shows: {self.dealer.hand.cards[0]} [?]")
        print(f"Your hand: {self.player.hand} (Value: {self.player.hand.get_value()})")
        
        # Player's turn
        while self.player.hand.get_value() < 21:
            action = input("\nHit or Stand? (h/s): ").lower()
            if action == 'h':
                self.player.hand.add_card(self.deck.deal())
                print(f"Your hand: {self.player.hand} (Value: {self.player.hand.get_value()})")
            elif action == 's':
                break
                
        player_value = self.player.hand.get_value()
        if player_value > 21:
            print(f"\nBUST! Your hand: {self.player.hand} (Value: {player_value})")
            return False
            
        # Dealer's turn
        print(f"\nDealer's hand: {self.dealer.hand}")
        while self.dealer.hand.get_value() < 17:
            self.dealer.hand.add_card(self.deck.deal())
            print(f"Dealer hits: {self.dealer.hand}")
            time.sleep(1)
            
        dealer_value = self.dealer.hand.get_value()
        print(f"\nDealer's final hand: {self.dealer.hand} (Value: {dealer_value})")
        
        # Determine winner
        if dealer_value > 21 or player_value > dealer_value:
            self.player.bank += bet * 2
            print(f"\nYou win ${bet}!")
            return True
        elif player_value < dealer_value:
            print(f"\nDealer wins! You lose ${bet}")
            return False
        else:
            self.player.bank += bet
            print("\nPush! Bet returned")
            return None

    def play_game(self):
        print("\nWelcome to Blackjack!")
        while self.player.bank > 0:
            if len(self.deck.cards) < 20:
                print("\nShuffling deck...")
                self.deck = Deck()
            
            result = self.play_round()
            print(f"\nBank: ${self.player.bank}")
            
            if not input("\nPlay another round? (y/n): ").lower().startswith('y'):
                break
                
        print(f"\nGame Over! Final bank: ${self.player.bank}")

if __name__ == "__main__":
    game = Game()
    game.play_game()