birthdate = int(input("Enter your birth year: "))
# User inputs birth year

if birthdate < 1900:
  print("Invalid year, it should not be earlier than 1900")
  # Error message if birthdate is less than 1900
else:
  zodiacs = ["Rat (鼠 / Shǔ)",
  "Ox (牛 / Niú)",
  "Tiger (虎 / Hǔ)",
  "Rabbit (兔 / Tù)",
  "Dragon (龙 / Lóng)",
  "Snake (蛇 / Shé)",
  "Horse (马 / Mǎ)",
  "Goat (羊 / Yáng)",
  "Monkey (猴 / Hóu)",
  "Rooster (鸡 / Jī)",
  "Dog (狗 / Gǒu)",
  "Pig (猪 / Zhū)"]
  # The zodiacs

zodiacsign = (birthyear - 1900)%12
#1900 is subtracted, the difference is divided by 12, and the remainder is the index the zodiac is in

print(f"Your Chinese Zodiac Sign is : {zodiacs[zodiacsign]}")
