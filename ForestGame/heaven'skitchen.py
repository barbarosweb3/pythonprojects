print(r"""\  
  ____________________          ____________________
  |                    |   ____ |                    |
  |  CAN  YOU GIVE ME  |  /    \I  -BUT I CAN ADD A  |
  |  ONE GOOD  REASON  | (  NO     PITCHFORK  AND A  |  /\
  |  WHY I SHOULD LET  |  \____/I  TAIL TO THAT "GO  | (  )
  |  YOU IN?           |        |  TO HELL" ICON.    | _)(_     _
  |_______________ .___|        |_____. _____________|~ __ ~-._ \"~-.
                  \|                  |/    (_ /~,^ .r~T  T~i. ^.~\ _)
                   `                  '      \ \/ ,^|| |  | ||^. \/ /
                _____                ___ _    Y  /  || |[]| ||  \  Y
     .--.     .^  ,^^\.-.           {___~ )   | Y   || |  | ||   Y |
    / __ \   / ) / -- )_ \           c|..^o   | |   || |[]| ||   | |
   / ( (\ \ /(   ) ,>.| ) \           |c_,|  <| |===||=|  |=||===| |>
    ( ( (\ Y  __ (/ o Y).--^-------.   )_/l  <| |===||=|[]|=||===| |>
     ( ( (\l)/  \    )I | [~~~~~~~\|   `--.\---x.   || |  | ||   | |
   (  ( ( (|Y    Y (  |\| | \ _____\__ _ _/r~)  )\_ ||_|[]|_||_ _| |  _.
     ( \ \ ||    |____>-| |  T   = |.__\\<\`^  ", \~|| |  | || ~ | |"~
    \   \ (\|  '~~ Y____|_I__l_n___|_  / `---c~~^. Y'~^|_.^"`|_.-^-|__,-~
   ( \ ( ( (|      | | |   [=o H .=.]_ `-I~T~Y     |-          __
      ( \ \ l      | | l___[___H____] ~"_| | |    ,t     __  "~  ~"
     \ ( \ \I\     | |[_________H____] / | l_j_.-T |--"~~  ~"-.__,.--"~
      \ \ \ ||`----^-' :\_______H__/   \/|       | |-.._
       (   \|;     :   | |.. .. H.|^,__.-|   :   : |_   _.--~~"--..
          \ |   _  l _ : ||| || H||   __ !   |   ' l "~"  -Row ._  _.-"
           _|,-' ~"-' ~-.L|^.||_H|^-"~  ~"-.    ._  \_.-"~-.__   "~
         "~     ._   __,--.__~~     ~-._     _.   "~~         ~~~"
                  ~~"        ~~"        "~~~"
""")

print("You are on your way back home. However, you need to go through a dense forest.")
print("You are driving, carefully. However, one cannot be fully focused if there is something bothering them.")

print("You are at a cross road.")
choice = input('You\'re trying to decide which way is better. '
              'Type "Left" or "Right" and let\'s see where it goes.\n')

if choice == "Left":
    print("You are at a dead end.\nGame Over!")
elif choice == "Right":
    print("You are following the dense forest. It's midnight. It's you versus the nature.")
    option = input('While driving through, you think you see someone by the road. Type "Stop" to stop and look or "Drive" to keep driving.\n')

    if option == "Stop":
        print("You were a lovely person! R.I.P!")
    elif option == "Drive":
        print("When you look at the back from your rear view mirror and you see that there is nobody standing there.")
        preference = input('You just breath deeply and when you turn your hues on the road you see a roadblock. A tree stand on the road.'
                         'Type "Stop" to stop and look around and type "Crash" to welcome your end.\n')
        if preference == "Stop":
            print("Welcome to heaven, mate!")
        elif preference == "Crash":
            print("Well well well, look who has come!")
        else:
            print("You have taken an arrow to the knee and your adventurous days are over!")
    else:
        print("You are adventurous, aren't you? R.I.P!")
else:
    print("Invalid choice. You are dead!")
