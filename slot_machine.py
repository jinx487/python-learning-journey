# A python slot machine
import random

def spin_row():
    symbols = ['🍒', '⭐', '🍋', '🔔', '🍉']
    return[random.choice(symbols) for _ in range(3)]

def display_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '⭐':
            return bet * 20
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🍉':
            return bet * 15
    return 0

def main():
    
    balance = 100 

    print("************************")
    print("Welcome to Python slots")
    print("symbols: 🍒 ⭐ 🍋 🔔 🍉")
    print("************************")

    while balance > 0:
        print(f"Current balance is: ${balance:.2f}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet amount must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        display_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost ths round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print("************************")
    print(f"Game over! Your balance is ${balance:.2f}")
    print("************************")

if __name__ == '__main__':
    main()