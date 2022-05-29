min,sec = (int,input("請輸入遊戲時間"))
time = min*60 + sec - 75
wave = 1
soldier = 0
while time > 0:
    soldier += 7 if wave % 3 == 0 else 6
    if wave % 2 == 0: soldier -= 1
    wave += 1
    time -= 30
print(soldier,"隻兵")