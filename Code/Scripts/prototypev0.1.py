import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Soul-Bro Blackjack Prototype")
font = pygame.font.Font(None, 36)

class Card:
    def __init__(self, rank):
        self.rank = rank
        self.value = 10 if rank in ['J', 'Q', 'K'] else 11 if rank == 'A' else int(rank) if rank.isdigit() else 0

    def get_special(self):
        specials = {
            'A' : "Roll D20 vs Demon; winner steals 1 soul chip.",
            '2' : "Roll D20; 10+ steal 1 soul.",
            '3' : "Cord of 3: +1 to all rolls this round.",
            '4' : "Cord of 4: +2 to all rolls this round.",
            '5' : "Cord of 5: +3 to all rolls this round.",
            '6' : "Cord of 6: +3 to all rolls this round.",
            '7' : "Cord of 7: +3 to all rolls this round.",
            '8' : "Cord of 8: +3 to all rolls this round.",
            '9' : "Cord of 9: +3 to all rolls this round.",
            '10': "Cord of 10: +3 to all rolls this round.",
            'J' : "Cord of J: +3 to all rolls this round.",
            'Q' : "Cord of Q: +3 to all rolls this round.",
            'K' : "Cord of K: +3 to all rolls this round.",
            # Add others similarly...
        }
        return specials.get(self.rank, "No special.")

class Deck:
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(rank) for _ in range(4) for rank in ranks]  # 4 suits
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.class_ = player_class  # e.g., 'Fighter'
        self.hand = []
        self.soul_chips = 10

    def hand_value(self):
        value = sum(c.value for c in self.hand)
        aces = sum(1 for c in self.hand if c.rank == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

# Game Loop Example
deck = Deck()
players = [Player("Hank", "Fighter"), Player("Demon King", "Demon")]  # Simplified 1v1
current_player = players[0]
demon = players[1]

# Deal initial cards
for p in players:
    p.hand = [deck.draw(), deck.draw()]

running = True
while running:
    screen.fill((0, 100, 0))  # Green table
    # Render hands (text for prototype)
    text = font.render(f"{current_player.name} Hand: {', '.join(c.rank for c in current_player.hand)} Value: {current_player.hand_value()}", True, (255, 255, 255))
    screen.blit(text, (50, 50))
    # Add event handling for hit/stand (keyboard for proto)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # Hit
                card = deck.draw()
                current_player.hand.append(card)
                print(f"Drew {card.rank}: {card.get_special()}")
                # Activate special logic here...
            elif event.key == pygame.K_s:  # Stand
                # Switch to Demon logic...
                pass
    pygame.display.flip()

pygame.quit()