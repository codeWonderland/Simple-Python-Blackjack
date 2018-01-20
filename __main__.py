import random


def print_status(player_cards, dealer_cards):
    print("\n")
    print("Player's total is " + str(calculate_score(player_cards)) + ":\n")
    print(player_cards)
    print("\n")

    print("Dealer's total is " + str(calculate_score(dealer_cards)) + ":\n")
    print(dealer_cards)
    print("\n")


def calculate_score(cards):
    score = 0
    has_ace = False

    for card in cards:
        try:
            card_value = int(card)
            score += card_value
        except ValueError:
            if card == "A":
                has_ace = True
            else:
                score += 10

    if has_ace:
        if score + 11 > 21:
            score += 1
        else:
            score += 11

    return score


def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    player_cards = []
    dealer_cards = []

    random.shuffle(deck)

    print("Dealer draws first card.")
    dealer_cards.append(deck.pop(-1))
    print("Player receives two _cards.")
    player_cards.append(deck.pop(-1))
    player_cards.append(deck.pop(-1))
    print_status(player_cards, dealer_cards)

    while True:
        print("Do you want to (H)it, (S)tay, or (Q)uit?")
        selection = input()
        selection = selection.upper()

        if selection == "H":
            player_cards.append(deck.pop(-1))
            print_status(player_cards, dealer_cards)

            if calculate_score(player_cards) > 21:
                print("You busted! You lose!")
                return 0
        elif selection == "S":
            break
        else:
            return 0

    print("Dealer draws rest of cards.")

    while calculate_score(dealer_cards) > 17:
        dealer_cards.append(deck.pop(-1))

    print_status(player_cards, dealer_cards)

    if calculate_score(dealer_cards) > 21:
        print("Dealer busts! You win!")
    elif calculate_score(dealer_cards) > calculate_score(player_cards):
        print("Dealer wins!")
    elif calculate_score(player_cards) > calculate_score(dealer_cards):
        print("You win!")
    else:
        print("It's a tie!")

    return


if __name__ == "__main__":
    main()
