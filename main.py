import os
import random
import string
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_wallet_address(currency):
    if currency == 'btc':
        prefix = random.choice(['1', '3', 'bc1'])
        length = 34 if prefix in ['1', '3'] else 42
    elif currency == 'eth':
        prefix = '0x'
        length = 42
    elif currency == 'sol':
        prefix = ''
        length = 44
    elif currency == 'ltc':
        prefix = random.choice(['L', 'M'])
        length = 34
    else:
        return "Invalid currency selected."

    address = prefix + ''.join(random.choices(string.ascii_letters + string.digits, k=length-len(prefix)))
    return address

def simulate_wallet_check(currency):
    while True:
        wallet_address = generate_wallet_address(currency)
        balance = "0"
        status = "[X]"
        private_key = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        
        print(Fore.RED + f"Balance: {balance} {currency.upper()} {status} Trying {wallet_address} Priv: {private_key}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = """
   _____                  _          _______          _     
  / ____|                | |        |__   __|        | |    
 | |     _ __ _   _ _ __ | |_ ___      | | ___   ___ | |___ 
 | |    | '__| | | | '_ \\| __/ _ \\     | |/ _ \\ / _ \\| / __|
 | |____| |  | |_| | |_) | || (_) |    | | (_) | (_) | \\__ \\
  \\_____|_|   \\__, | .__/ \\__\\___/     |_|\\___/ \\___/|_|___/
               __/ | |                                      
              |___/|_|                                      
    """
    print(Fore.CYAN + ascii_art)
    print(Style.BRIGHT + "Select a cryptocurrency: btc, eth, sol, ltc")
    currency = input("Enter your choice: ").strip().lower()

    if currency in ['btc', 'eth', 'sol', 'ltc']:
        simulate_wallet_check(currency)
    else:
        print("Invalid currency selected.")

if __name__ == "__main__":
    main()
