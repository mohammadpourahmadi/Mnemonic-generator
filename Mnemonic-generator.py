from mnemonic import Mnemonic
mnemo = Mnemonic("english")
num = 0
with open("list.txt", "a") as file:
     #Instead of 10000, put any number you like, any number will make the same number of memory words
     for words in range(10000):
         words = mnemo.generate(strength=128) + "\n"
         file.write(words)
         print(num, words)
         
     
