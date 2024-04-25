def rps(p1, p2):
 if (p1.lower()=='rock' and p2.lower()=='scissors') or (p1.lower()=='scissors' and p2.lower()=='paper') or (p1.lower()=='paper' and p2.lower()=='rock'):
    return f'"{p1}","{p2}" --> "Player 1 won!"'
 elif (p2.lower()=='rock' and p1.lower()=='scissors') or (p2.lower()=='scissors' and p1.lower()=='paper') or (p2.lower()=='paper' and p1.lower()=='rock'):    
    return f'"{p1}","{p2}" --> "Player 2 won!"'
 else:
    return f'"{p1}","{p2}" --> "Draw!"'

p1="scissors"
p2="rock"
print(rps(p1,p2))