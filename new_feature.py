import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "Ace":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print("Hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

    def play(self):
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

        game_over = False

        while not game_over:
            print("Player's turn")
            self.player_hand.display()
            self.dealer_hand.display()

            choice = input("Do you want to [Hit] or [Stand]? ").lower()
            while choice not in ["hit", "stand"]:
                choice = input("Do you want to [Hit] or [Stand]? ").lower()
            if choice == "hit":
                self.player_hand.add_card(self.deck.deal())
                self.player_hand.calculate_value()
                self.dealer_hand.calculate_value()
                if self.player_hand.get_value() > 21:
                    print("Bust! Dealer wins!")
                    game_over = True
            else:
                player_hand_value = self.player_hand.get_value()
                dealer_hand_value = self.dealer_hand.get_value()
                print("Final Results")
                print("Player's Hand:", end=" ")
                self.player_hand.display()
                print("Dealer's Hand:", end=" ")
                self.dealer_hand.display()
                if player_hand_value > dealer_hand_value:
                    print("You win!")
                elif player_hand_value == dealer_hand_value:
                    print("Tie!")
                else:
                    print("Dealer wins!")
                game_over = True

if __name__ == "__main__":
    game = Game()
    game.play()
