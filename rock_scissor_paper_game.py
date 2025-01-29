import random
li = ["rock","scissor","paper"]
ccount = 0
ucount = 0
while True:
     inp = int(input("""
                     
     Rock-Paper-Scissor Game start:
                            1.Yes| Play
                            2.No | Exist
                     
          """))
     if inp ==  1:
            for a in range(1,6):
                   userInput = int(input("""
                                  please select any one option:
                                               1.Rock
                                               2.Scissor
                                               3.Paper
                                  
                """))
                   if userInput == 1:
                         uchoice="rock"
                   elif userInput == 2:
                         uchoice="scissor"
                   elif userInput == 3:
                         uchoice="paper"      

                   Cchoice = random.choice(li)

                   if Cchoice == uchoice:
                               print("Computer choice : ",Cchoice)
                               print("user choice : ",uchoice)
                               print("Game Draw")
                               ucount = ucount+1
                               ccount = ccount+1
                   elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and uchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                              print("Computer choice : ",Cchoice)
                              print("User choice : ",uchoice)
                              print("You win")
                              ucount = ucount+1
                   else:
                     print("Computer choice : ",Cchoice)
                     print("User choice : ",uchoice)
                     print("Computer win")
                     ccount = ccount+1      
            if ucount == ccount:
                     print("Final Game Draw....")
                     print("User Score ",ucount)
                     print("Computer Score ",ccount)
            if ucount > ccount:
                      print("Final you win the game....")
                      print("User Score ",ucount)
                      print("Computer Score ",ccount)
            if ucount < ccount:
                     print("Final Computer win the game....")
                     print("User Score ",ucount)
                     print("Computer Score ",ccount)

     else:
        break
