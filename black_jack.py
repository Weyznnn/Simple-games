import random

card_pack = ('AS',2,3,4,5,6,7,8,9,10,'J','Q','K')

player_deck = {}

def cards_total(deck:dict = player_deck):
    if 'AS' in deck.keys() and 'J' in deck.keys() or 'Q' in deck.keys() or 'K' in deck.keys():
        return 21 + sum(deck.values()) - 12
    else:
        return sum(deck.values())

def main():
    while cards_total() <= 21:
        player_pick = random.choice(card_pack)
        player_moves = input("Pick [p] or Stay [s]\n").lower()
        if player_moves == 'p':
            player_deck.update({player_pick: 11 if card_pack.index(player_pick) >= 10 else card_pack.index(player_pick) + 1})
        elif player_moves == 's':
            print("You win")
            break
        print(f'Your deck: {player_deck.keys()}\nTotal cards: {cards_total()}')
    else:
        print("You lose")

if __name__ == "__main__":
    main()