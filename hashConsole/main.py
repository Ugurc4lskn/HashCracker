
import argparse, hashlib, os, time
from colorama import Fore, init 


init(autoreset=True)

parser = argparse.ArgumentParser(description='Hash Kırma Aracı')

parser.add_argument('--word', help='Şifrelenen metni girin')
parser.add_argument('--wordlist', help='wordlist yolunu girin')
parser.add_argument("--hash", help="Hash değerini girin")

args = parser.parse_args()
word_ = (args.word)
wordlist_ = (args.wordlist)
hash_  = args.hash

if os.path.exists(wordlist_):
    with open(wordlist_, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            lineControl = (str(line).strip())
            control = (hashlib.new(name=(hash_), data=(lineControl).encode("utf-8")).hexdigest())
            
            if control == str(word_):
                print(Fore.GREEN+f"Bulundu ! Şifre:  {Fore.WHITE+lineControl}")
                break

            print(Fore.RED+f"Bulunamadı ! Denenen:  {Fore.WHITE+lineControl}")
            
            os.system('cls' if os.name == 'nt' else 'clear')
        
            
           
