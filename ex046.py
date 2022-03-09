import emoji
from time import sleep
start= str(input('inicie...'))
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('-='*14)
print(emoji.emojize('\033[1;31;40mFeliz ano novo!\033[m \033[33m:fireworks: :fireworks: :fireworks: :fireworks: \033[m', use_aliases=True))
print('-='*14)