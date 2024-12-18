import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

all_list = [rock, paper, scissors]
Komp = 0  
hrac = 0  

while Komp < 3 and hrac < 3:
    user_choose = int(input("0 kámen, 1 papír, 2 nůžky\n"))
    
    if user_choose not in [0, 1, 2]:
        print("Neplatná volba!")
        continue 
    
  
    user_picture = all_list[user_choose]
    computer_choose = random.randint(0, 2)
    computer_picture = all_list[computer_choose]

   
    print(f"Uživatel si vybral:\n {user_picture}")
    print(f"Počítač si vybral:\n {computer_picture}")

    
    if user_choose == computer_choose:
        print("Remíza")
    elif user_choose == 0 and computer_choose == 1:
        print("Prohrál jsi, počítač vyhrává")
        Komp += 1
    elif user_choose == 0 and computer_choose == 2:
        print("Vyhrál jsi, počítač prohrává")
        hrac += 1
    elif user_choose == 1 and computer_choose == 0:
        print("Vyhrál jsi, počítač prohrává")
        hrac += 1
    elif user_choose == 1 and computer_choose == 2:
        print("Prohrál jsi, počítač vyhrává")
        Komp += 1
    elif user_choose == 2 and computer_choose == 0:
        print("Prohrál jsi, počítač vyhrává")
        Komp += 1
    elif user_choose == 2 and computer_choose == 1:
        print("Vyhrál jsi, počítač prohrává")
        hrac += 1

    if Komp == 3:
        print("Počítač vyhrál")
        break
    elif hrac == 3: 
        print("Vyhrál ")
        break