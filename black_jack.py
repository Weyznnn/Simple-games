import random

card_pack = ('AS',2,3,4,5,6,7,8,9,10,'J','Q','K')

player_deck = []
int_deck = []

def cards_total(deck, i = int_deck):
    if 'AS' in deck:
        i[-1] = 1
        return sum(i)
    elif 'J' in deck or 'Q' in deck or 'K' in deck:
        i[-1] = 11
        return sum(i)
    else:
        return sum(i)

def main():
    while sum(int_deck) <= 21:
        player_pick = random.choice(card_pack)
        player_moves = input("Pick [p] or Stay [s]\n").lower()
        if player_moves == 'p':
            player_deck.append(player_pick)
            int_deck.append(player_pick)
        elif player_moves == 's':
            print("You win")
            break
        print(f'Your deck: {player_deck}\nTotal cards: {cards_total(player_deck)}')
    else:
        print("You lose")

if __name__ == "__main__":
    main()