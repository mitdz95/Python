print('''
*******************************************************************************
    ,..-,
  ,;;f^^"""-._
 ;;'          `-.
;/               `.
||  _______________\_______________________
||  |HHHHHHHHHHPo"~~\"o?HHHHHHHHHHHHHHHHHHH|
||  |HHHHHHHHHP-._   \,'?HHHHHHHHHHHHHHHHHH|
 |  |HP;""?HH|    """ |_.|HHP^^HHHHHHHHHHHH|
 |  |HHHb. ?H|___..--"|  |HP ,dHHHPo'|HHHHH|
 `| |HHHHHb.?Hb    .--J-dHP,dHHPo'_.rdHHHHH|
  \ |HHHi.`;;.H`-./__/-'H_,--'/;rdHHHHHHHHH|
    |HHHboo.\ `|"\"/"\" '/\ .'dHHHHHHHHHHHH|
    |HHHHHHb`-|.  \|  \ / \/ dHHHHHHHHHHHHH|
    |HHHHHHHHb| \ |\   |\ |`|HHHHHHHHHHHHHH|
    |HHHHHHHHHb  \| \  | \| |HHHHHHHHHHHHHH|
    |HHHHHHHHHHb |\  \|  |\|HHHHHHHHHHHHHHH|
    |HHHHHHHHHHHb| \  |  / dHHHHHHHHHHHHHHH|
    |HHHHHHHHHHHHb  \/ \/ .fHHHHHHHHHHHHHHH|
    |HHHHHHHHHHHHH| /\ /\ |HHHHHHHHHHHHHHHH|
    |""""""""""""""""""""""""""""""""""""""|
    |,;=====.     ,-.  =.       ,=,,=====. |
    |||     '    //"\\   \\   //  ||     ' |
    |||         ,/' `\.  `\. ,/'  ``=====. |
    |||     .   //"""\\   \\_//    .     |||
    |`;=====' =''     ``=  `-'     `=====''|
    |______________________________________|
*******************************************************************************
''')
print("Welcome to 2016 NBA Finals Clutch Time Simulator.\n")
print("Your mission is to make the game winning plays to win the Championship.\n") 
print("Only answer with number or texts with first letter capitalized")
    
#https://shorturl.at/fvJU1

#Write your code below this line 👇
print("You are Lebron James and you are playing in Game 7 of the 2016 NBA Finals against the 73/9 Golden States Warriors with the MVP and greatest shooter of all time Steph Curry. You were down 1-3 earlier in the series but managed to force game 7. This is the most important and iconic momment of your career and could make you the GREATEST OF ALL TIME, LeGOAT JAMES, baa baa. However if you failed, you will be LeBUM and LeCHOKE for the rest of your life.\n")

print("Kyrie Irving misses a floater with 1:58s left in the 4th. Andre Iguodala gets the rebound and rushes down to your basket. He has a head start on you and you have 2 choices: \n1. Race him to the hoop and attempt to block the shot. \n2. Stay where you are, hoping JR Smith can steal the ball and be ready for a fast break opportunity.")

first = input("Block or Wait?\n")
if first != "Block" and first != "1":
  print("Iggy scores the basket. Warriors get the momentum and goes on to win the game.\nSeries Over.\nYou are LeBUM.")
else:
  print("\nYou sprint down the court with super sonic speed and catch up to Iggy as he jumps for a lay up.")
  second = input("Which hand(s) do you use to block the shot?\n")
  if second != "Both" and second != "Left" and second !="Right":
    print("You are confused and can't make a decision in time. Iggy scores the basket. \nWarriors get the momentum and goes on to win the game.\nSeries Over.\nYou will never be the GOAT.")
  elif second == "Left" or second == "Right":
    print("Iggy sees which hand you are going to use and switchs to the other side and scores the basket. \nWarriors get the momentum and goes on to win the game.\nSeries Over.\nYou are LeCHOKE.")
  elif second == "Both":
    print("OOOHHH BLOCKED BY JAMES!!! LEBRON JAMES WITH THE REJECTION!!!\n")

    print("Your team has the ball and need to score a basket. You are the primary ball handler. Which offensive plan are you going with?")
    third = input("1. Call for a 1 on 1 and try to drive and score at the the basket. \n2. Call for a 1 on 1 and kick out to an open teammate for a 3-point shot. \n3. Give the ball to Kyrie Irving and let im create his own shot.\n")
    if third == "1":
        print("You are tired from the previous play. You get blocked at the rim. \nWarriors get the momentum and goes on to win the game.\nSeries Over.\nYou should just retire.")
    elif third == "2":
        print("Your star teammate Kyrie Irving is closely guarded so you have to pass to Richard Jefferson in the corner. He misses. \nCurry gets the rebound. \nWarriors get the momentum and goes on to win the game.\nSeries Over.\nEveryone says you pass the ball again, no assasin mentality.")
    elif third == "3":
        print("Kyrie call ISO on Steph and made a HUGEEE side-step 3. Cooking Curry is WILDDDDDDD.")
        print("\nYou hold on the the lead and proceed to win the hardest and greatest championship in the history of basketball! \nYou are now the GOAT.")
    else:
        print("If you can't make A decision, why even play? GTFO")





