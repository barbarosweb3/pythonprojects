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

rock_paper_scissor = random.randint(0,2)
random_r_p_s = random.randint(0, 2)

if rock_paper_scissor == 0:
    print(rock)
    if random_r_p_s == 0:
        print(rock)
        print("Draw!")
    elif random_r_p_s == 1:
        print(paper)
        print("Paper wins!")
    elif random_r_p_s == 2:
        print(scissors)
        print("Scissors win!")
elif rock_paper_scissor == 1:
    print(paper)
    if random_r_p_s == 0:
        print(rock)
        print("Paper wins!")
    elif random_r_p_s == 1:
        print(paper)
        print("Draw!")
    elif random_r_p_s == 2:
        print(scissors)
        print("Scissors win!")
elif rock_paper_scissor == 2:
    print(scissors)
    if random_r_p_s == 0:
        print(rock)
        print("Rock wins!")
    elif random_r_p_s == 1:
        print(paper)
        print("Scissors win!")
    elif random_r_p_s == 2:
        print(scissors)
        print("Draw!")
else:
    print("Invalid option!")