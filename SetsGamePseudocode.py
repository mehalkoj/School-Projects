import random

computer = []

player = []

for i in range(0,5):
    m = random.randint(1,6)
    computer.append(m)
    n = random.randint(1, 6)
    player.append(n)
c_count = 0
p_count = 0
for i in range(1,7):
    m = computer.count(i)
    c_count = max(c_count,m)
    n = player.count(i)
    p_count = max(p_count, n)
print("Computer rolled:", computer)
print("Player rolled:", player)
print("Computer has",c_count,"of a kind")
print("Player has",p_count,"of a kind")
if c_count>p_count:
    print("Computer wins")
elif c_count<p_count:
    print("Player wins")
else:
    print("It is a tie game.")

