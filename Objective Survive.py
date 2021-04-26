import random
nameofMC = input("What is your name? ").capitalize()
def prolouge():
    print("You,", nameofMC, "are part of a Nasa space crew tasked with being the first people to inhabit Mars.\n")
    print("The year is 2032 and you wake up in the flight deck after being knocked unconcious by an impact.\n")
    print("The ship has collided with something, and it is your objective to survive.\n")
    print("The flight deck seems to be mostly intact, but you have no idea what has been damaged, or of the whereabout of your crewmates.\n")
    print("The control panel of the ship displays critical signs of damage in the crew quarters along with damage to various other areas.\nIt is up to you to decide what to do next.\n")

def actionpart():
    action1 = {1:"Make your way to the crew's quarters", 2:"Make your way to the storage to see what remains on the ship"}
    print(action1)
    choice = input("Action 1 or 2? ")
    while True:
        if choice == '1':
            print ("The crew's quarters are made up of 5 bedrooms. The quarters are located in the furthest side of the ship past the main floor, family rooms, and research room.\nThe spaceship is built in a structure that certain areas of the ship may be dropped off.\nThe only exception is the main floor and flight deck. Each of these layers have doors you must pass through.\nYou reach the door leading to the crew quarters to find that it is pitch black. Being dark means it has potentially lost all power.")
            print("The oxygen filtration system is reliant on power in each part of the ship./n You don't know how long the power has been out in the quarters. You may be able to enter without a spacesuit assuming there is still oxygen. You now are tasked with the option to rush in and save your crewmates, or better prepare for the task.")
            action2 = {1:"Enter the crew quarters to save your crew mates", 2:"Head to the airlock to recieve your spacesuit."}
            print(action2)
            choice = input("Action 1 or 2? ")
            if choice == "1":
                print("You begin to open the airlock that leads to the crew quarters. You feel a tightening in your chest from nerves of what awaits you on the other side.")
                print("As you enter you turn back to close the door behind you. You have now entered the crew quarters airlock you can't see much further than the light from the door behind you. You begin to move around the entrance of the air lock to reach the crew quarters.")
                print("When you find the door you can't see a thing through the door. It is pitch black on the other side, but with each moment you wait your crewmates may be in further danger.")
                print("You begin to open the door until it is unlocked. The pressure drops and the absence of oxygen fills the airlock.")
                print("Short on time you try and close the door to reseal the airlock but with each second passing you begin to lose conciousness. You have failed your mission.")
                break # add more to death
            elif choice == "2":
                print("You make your way to the main airlock which leads to the outside of the spacecraft. This airlock contains spacesuits normally used for spacewalks. The crew quarters are one of the parts of the ship that has artificial gravity.\n")
                print("This makes spacesuits unusable there, but since the power is out you can freely travel. You put on the space suit and head to the crew quarters.\n")
                print("Now as you walk into the airlock of the crew quarters you can't see much other than the light provided by the door behind you.\n")
                print("You turn on the external light of your spacesuit, and continue through the next door.")
                print("Once you reach the otherside your scanners show that the quarters have no oxygen and the pressure is lower than the rest of the ship.\n")
                print("You are now truly alone in space. The decisions to save the mission solely rely on you. You can continue to search the quarters, or return back to the main floor and contact HQ.\n")
                action3 = {1: "Search the quarters", 2: "Return to the main floor to contact HQ"}
                print(action3)
                choice = input("Action 1 or 2? ")
                if choice == "1":
                    print("The quarters are dark but using the light on your suit you make your way toward the hallway containing the bedrooms.\n")
                    print("The closest room to you is on the left side nearest to the airlock. You reach the door and begin inspecting it with your light\n")
                    print("The door looks as if it had been clawed into. The door is mangeled and morphed on the edges with deep scratch marks. On your left there is a small plaque.\n")
                    print("The plaque is labeled 'Alexender Tromko' indicating the crewmate who lived inside.\n")
                    print("You continue inside using your light to guide you. Looking around the room you can't seem to find your crewmate anywhere.\n")
                    print("Making your way toward the bed you see a body sized lump beneath the blanket.\n")
                    print("Standing above the body of your crewmate you notice a pool of blood soaked into the blanket.\n")
                    print("Your crewmate had been killed by someone or something... You can continue to search the remaining quarters or alert HQ of what is happening.\n")
                    action4 = {1: "Continue Searching the quarters", 2: "Return to the main floor to contact HQ"}
                    print(action4)
                    choice = input("Action 1 or 2? ")
                    if choice == "1":
                        print("You now exit the quarters of your crewmate Alexander, and begin to make your way down the dark hallway.")
                        print("You don't need to see what happened to your remaining crewmates to know they are gone, so you head to your master bedroom.")
                        print("Upon reaching the door you notice it is untouched as if what had visited your friends room had not been to yours.")
                        print("You begin to slide the door open when you hear a faint sound behind you. The sound is almost that of metal scraping against itself followed by a long silence.")
                        print("You feel like you are being watched. Heart racing you open the door and quickly shut it behind you.")
                        print("The sound of metal scraping drags down the hallway toward your door. You stand at the door frozen in fear.")
                        print(" A long pause occurs you hear nothing seconds feel like hours as your heart beats through your chest. Then as if out of a move a long black tail passes through the metal door and through your chest.")
                        print("You have failed your mission.")
                        break                    
                    elif choice == "2":
                        print("You exit the airlock the same way you came in and make your way to the flight deck to contact HQ.")
                        print("Upon reaching the flight deck the HQ appears to be unreachable as the communications for your ship seem to have been destroyed.")
                        print("Before entering the quarters you had the option to contact HQ meaning it was destroyed long after what impacted the ship. You now have two options.")
                        action5 = {1: "Attempt to restore communications" , 2: "Figure out what impacted with the ship"}
                        print(action5)
                        choice = input("Action 1 or 2? ")
                        if choice == "1":
                            print("You decide that attempted to restore communications with HQ is your best shot at making the right decision.")
                            print("The communications center is structured almost entirely through the research room.")
                            print("You make your way through the main floor toward the research room and begin opening the airlock.")
                            print("After passing through the first door you enter the research room to find that it is intact.")
                            print("The room is filled with various points of study.")
                            print("There are supplies to garden, micropscopes and trays to study potential findings, a water filtration backup, and lastly a communications area.")
                            print("The area is made up of a large box and wires that run along the ship and connect to sattelite points outside.")
                            print("Upon inspection the communications area seems fine along with the rest of the research room as if it had not been impacted.")
                            print("The only other option was to check satellite points outside the ship, which also means you will figure out what impacted the ship.")
                            print("You make your way back to the main airlock where you initially got you spacesuit.")
                            print("You open the airlock, close the door behind you and begin to prepare for your spacewalk.")
                            print("There are small clips that you must fasten to the ship to make sure you are not taken too far from the ship.")
                            print("You open the door and make your way into space latching on to the bar above the door you float down and fasten the door behind you.")
                            print("Climbing above the airlock you can now see the top of the ship.")
                            print("The ship is build into layers stacked onto one another with various rooms branching out.")
                            print("The flight deck has 3 large solar sails attatched to it giving the ship the ability to move through space.")
                            print("As long as this stays intact the ship can move through space meaning the rest of the areas are expendable. You make your way past the solar sails to see the impact.")
                            print("There is a diamond shaped object resting on the top of the ship. The object is a silverish color but it appears to almost be fully reflective.")
                            print("While inspecting the object you can also clearly see that the communcations points outside of the research room are completeley destroyed from the impact of the object.")
                            print("This thing must have passed through the cargo bay and into the back of the ship directly hitting the crew quarters.")
                            print("Being that the object is so far back you could drop it into space along with the crew quarters.\nYou also can search the object to find out what it is.")
                            action6 = {1: 'Head back inside to remove that area of the ship', 2: 'Investigate the object closer'}
                            print(action6)
                            choice = input("Action 1 or 2? ")
                            if choice == "1":
                                print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates. The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates. You open the airlock from the outside and enter the ship. After closing the door you prepare to reenter the space ship again. You know that you are alone. Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates. Making your way toward the quarters you can hear something on the inside moving around. It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point. As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.")
                                action7 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                choice = input("Action 1 or 2? ")
                                if choice == "1":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\nYou face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\nYou no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\nThe door opens into a dark room with no oxygen as you had left it previously. You step inside looking around for Alex who was crying for help. There is no one immediately near the door as you would have expected from the cries. Just as fear, and doubt enter something cries out above you and drops from the ceiling.\nYou have failed your mission.")
                                elif choice == "2":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\nYou make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.\nYou make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\nThe threat that was on the ship threatening your life is now gone.\nYour only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")                    
                                    action7 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                    print (action7)
                                    choice = input("Action 1 or 2? ")
                                    if choice == "1":
                                        print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\nYou face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\nYou no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\nThe door opens into a dark room with no oxygen as you had left it previously. You step inside looking around for Alex who was crying for help. There is no one immediately near the door as you would have expected from the cries. Just as fear, and doubt enter something cries out above you and drops from the ceiling.\nYou have failed your mission.")
                                    elif choice == "2":
                                        print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\nYou make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.\nYou make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\nThe threat that was on the ship threatening your life is now gone.\nYour only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")
                        elif choice == "2":
                            print("You make your way back to the main airlock where you initially got you spacesuit.")
                            print("You open the airlock, close the door behind you and begin to prepare for your spacewalk.")
                            print("There are small clips that you must fasten to the ship to make sure you are not taken too far from the ship.")
                            print("You open the door and make your way into space latching on to the bar above the door you float down and fasten the door behind you.")
                            print("Climbing above the airlock you can now see the top of the ship.")
                            print("The ship is build into layers stacked onto one another with various rooms branching out.")
                            print("The flight deck has 3 large solar sails attatched to it giving the ship the ability to move through space.")
                            print("As long as this stays intact the ship can move through space meaning the rest of the areas are expendable. You make your way past the solar sails to see the impact.")
                            print("There is a diamond shaped object resting on the top of the ship. The object is a silverish color but it appears to almost be fully reflective.")
                            print("While inspecting the object you can also clearly see that the communcations points outside of the research room are completeley destroyed from the impact of the object.")
                            print("This thing must have passed through the cargo bay and into the back of the ship directly hitting the crew quarters.")
                            print("Being that the object is so far back you could drop it into space along with the crew quarters.\nYou also can search the object to find out what it is.")
                            action6 = {1: 'Head back inside to remove that area of the ship', 2: 'Investigate the object closer'}
                            print(action6)
                            choice = input("Action 1 or 2? ")
                            if choice == "1":
                                print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates. The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates. You open the airlock from the outside and enter the ship. After closing the door you prepare to reenter the space ship again. You know that you are alone. Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates. Making your way toward the quarters you can hear something on the inside moving around. It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point. As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.")
                                action7 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                choice = input("Action 1 or 2? ")
                                if choice == "1":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\nYou face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\nYou no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\nThe door opens into a dark room with no oxygen as you had left it previously. You step inside looking around for Alex who was crying for help. There is no one immediately near the door as you would have expected from the cries. Just as fear, and doubt enter something cries out above you and drops from the ceiling.\nYou have failed your mission.")
                                    break
                                elif choice == "2":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\nYou make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.\nYou make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\nThe threat that was on the ship threatening your life is now gone.\nYour only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")
                                    break
                            elif choice == "2":
                                print("You decide to investigate the object that landed on your ship. You make your way across the top of the ship toward the large reflective object.\nThere are no windows doors, or anything that look familiar to your ship. You get up next to the object and it seems like a mirror you can clearly see yourself in the reflection of the object.\nYou begin to search aroundthe side to see if you can find an entry point. There is a hole in the top of the ship leading to the crew quarters. Nearest to this hole look almost like a loading dock of a large cargo plane.\nYou can climb inside and further investigate this object or Head back inside the ship.")
                                action8 ={1: "Climb inside to investigate the object further", 2: "Head back inside the ship"}
                                print(action8)
                                choice = input("Action 1 or 2? ")
                                if choice == "1":
                                    print("You climb up the long loading dock being careful not to lose your footing on its reflective surface.\n")
                                    print("On your way up the tassle attached to you is not long enough to contiunue in.\n")
                                    print("At this point you have no choice but to release yourself from the tether of your ship. You untether yourself and enter the object.\n")
                                    print("On the inside the top of the object is just a long flat white light accompanied by the same reflective floor as before.\n")
                                    print("You walk deeper into the object to see what appears to be an elevated ring with nothing but two large black rings in front of it.")
                                    print("Behind you you hear the sound of the entrance lifting to close the object.\nYou rush back toward the entrance, but are much too late as the object seals shut")
                                    print("Along with the only known exit being shut the ship has no pressurized to normal gravity.\n")
                                    print("The spacesuit now is heavy and you cannot move unless you take it off. With no other option you begin to remove the suit starting with the helmet.\n")
                                    print("The air around you appears to be breathable, but as time goes on your eyes begin to feel heavy.\nThe suit is off but your body feels heavier than before.\n")
                                    print("The air must be knocking you out once again. You fall to the ground. You have failed your mission.\n")
                                elif choice == "1":
                                    print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates.\n")
                                    print("The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongings you brought onto the ship with you will be lost in space along with the remainof your crewmates.\nYou open the airlock from the outside and enter the ship.\nAfter closing the door you prepare to reenter the space ship again. You know that you are alone.\nCommunications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.\nMaking your way toward the quarters you can hear something on the inside moving around.\nIt is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.\nAs You are about to release the crew quarters you hear a voice callout 'Help its me Alex!' Knowing everything you saw on the inside of the crew quarters you now have to make a decision.")
                                    action9 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                    print(action9)
                                    choice = input("Action 1 or 2? ")
                                    if choice == "1":
                                        print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\n")
                                        print("You face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\n")
                                        print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\n")
                                        print("The door opens into a dark room with no oxygen as you had left it previously.\n")
                                        print("You step inside looking around for Alex who was crying for help.\nThere is no one immediately near the door as you would have expected from the cries.")
                                        print("Just as fear, and doubt enter something cries out above you and drops from the ceiling. You have failed your mission.")
                                        break
                                    elif choice == "2":
                                        print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\n")
                                        print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.\nThe ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                        print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\n")
                                        print("The threat that was on the ship threatening your life is now gone.\n")
                                        print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.\n")
                                        action10 = {1: "Finish the trip to Mars", 2: "Recourse the mission back to Earth"}
                                        print(action10)
                                        choice = input("Action 1 or 2? ")
                                        if choice == "1":
                                            print("You decide that it is best you finish the mission you were sent to accomplish.\nThe ship is already on path to Mars there is nothing for you to do.\n")
                                            print("The communications are destroyed beyond repair from the object impacting with the ship.\n")
                                            print("All you can do now is let the days go by as your ship approaches Mars.\n")
                                            print("The primary floors of the ship contain enough food and water for a one way trip.\n")
                                            print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                            print("You have failed your mission, but you did make it to Mars.\n")
                                        elif choice == "2":
                                            print("You decide that it is best to recourse the ship and head back to Earth.\n")
                                            print("The complications lie in the fact that you have no contact with the ground.\n")
                                            print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.\n")
                                            
        elif choice == "2":
            print("The primary storage of the ship exists in the cargo bay. The cargo bay is a room connected to the main floor of the ship. Like the rest of the ship it is detachable to drop into space.\n")
            print("The spacecraft can remove any of the furthest layers besides the flight deck, and main floor. You make your way to the cargo bay through the main floor to find that it is completely empty.\n")
            print("The cargo bay has been exposed to the vacuum of space and you must set it free before anymore damage is done to the ship. You release the cargo bay into space, and now are tasked with the next choice.\n")
            print("After investigating the cargo bay you have no other options but go to the crew quarters\n.")
            print ("The crew's quarters are made up of 5 bedrooms. The quarters are located in the furthest side of the ship past the main floor, family rooms, and research room.\nThe spaceship is built in a structure that certain areas of the ship may be dropped off.\nThe only exception is the main floor and flight deck. Each of these layers have doors you must pass through.\nYou reach the door leading to the crew quarters to find that it is pitch black. Being dark means it has potentially lost all power.")
            print("The oxygen filtration system is reliant on power in each part of the ship./n You don't know how long the power has been out in the quarters. You may be able to enter without a spacesuit assuming there is still oxygen. You now are tasked with the option to rush in and save your crewmates, or better prepare for the task.")
            action2 = {1:"Enter the crew quarters to save your crew mates", 2:"Head to the airlock to recieve your spacesuit."}
            print(action2)
            choice = input("Action 1 or 2? ")
            if choice == "1":
                print("You begin to open the airlock that leads to the crew quarters. You feel a tightening in your chest from nerves of what awaits you on the other side.")
                print("As you enter you turn back to close the door behind you. You have now entered the crew quarters airlock you can't see much further than the light from the door behind you. You begin to move around the entrance of the air lock to reach the crew quarters.")
                print("When you find the door you can't see a thing through the door. It is pitch black on the other side, but with each moment you wait your crewmates may be in further danger.")
                print("You begin to open the door until it is unlocked. The pressure drops and the absence of oxygen fills the airlock.")
                print("Short on time you try and close the door to reseal the airlock but with each second passing you begin to lose conciousness. You have failed your mission.")
                break # add more to death
            elif choice == "2":
                print("You make your way to the main airlock which leads to the outside of the spacecraft. This airlock contains spacesuits normally used for spacewalks. The crew quarters are one of the parts of the ship that has artificial gravity.\n")
                print("This makes spacesuits unusable there, but since the power is out you can freely travel. You put on the space suit and head to the crew quarters.\n")
                print("Now as you walk into the airlock of the crew quarters you can't see much other than the light provided by the door behind you.\n")
                print("You turn on the external light of your spacesuit, and continue through the next door.")
                print("Once you reach the otherside your scanners show that the quarters have no oxygen and the pressure is lower than the rest of the ship.\n")
                print("You are now truly alone in space. The decisions to save the mission solely rely on you. You can continue to search the quarters, or return back to the main floor and contact HQ.\n")
                action3 = {1: "Search the quarters", 2: "Return to the main floor to contact HQ"}
                print(action3)
                choice = input("Action 1 or 2? ")
                if choice == "1":
                    print("The quarters are dark but using the light on your suit you make your way toward the hallway containing the bedrooms.\n")
                    print("The closest room to you is on the left side nearest to the airlock. You reach the door and begin inspecting it with your light\n")
                    print("The door looks as if it had been clawed into. The door is mangeled and morphed on the edges with deep scratch marks. On your left there is a small plaque.\n")
                    print("The plaque is labeled 'Alexender Tromko' indicating the crewmate who lived inside.\n")
                    print("You continue inside using your light to guide you. Looking around the room you can't seem to find your crewmate anywhere.\n")
                    print("Making your way toward the bed you see a body sized lump beneath the blanket.\n")
                    print("Standing above the body of your crewmate you notice a pool of blood soaked into the blanket.\n")
                    print("Your crewmate had been killed by someone or something... You can continue to search the remaining quarters or alert HQ of what is happening.\n")
                    action4 = {1: "Continue Searching the quarters", 2: "Return to the main floor to contact HQ"}
                    print(action4)
                    choice = input("Action 1 or 2? ")
                    if choice == "1":
                        print("You now exit the quarters of your crewmate Alexander, and begin to make your way down the dark hallway.")
                        print("You don't need to see what happened to your remaining crewmates to know they are gone, so you head to your master bedroom.")
                        print("Upon reaching the door you notice it is untouched as if what had visited your friends room had not been to yours.")
                        print("You begin to slide the door open when you hear a faint sound behind you. The sound is almost that of metal scraping against itself followed by a long silence.")
                        print("You feel like you are being watched. Heart racing you open the door and quickly shut it behind you.")
                        print("The sound of metal scraping drags down the hallway toward your door. You stand at the door frozen in fear.")
                        print(" A long pause occurs you hear nothing seconds feel like hours as your heart beats through your chest. Then as if out of a move a long black tail passes through the metal door and through your chest.")
                        print("You have failed your mission.")
                        break                    
                    elif choice == "2":
                        print("You exit the airlock the same way you came in and make your way to the flight deck to contact HQ.")
                        print("Upon reaching the flight deck the HQ appears to be unreachable as the communications for your ship seem to have been destroyed.")
                        print("Before entering the quarters you had the option to contact HQ meaning it was destroyed long after what impacted the ship. You now have two options.")
                        action5 = {1: "Attempt to restore communications" , 2: "Figure out what impacted with the ship"}
                        print(action5)
                        choice = input("Action 1 or 2? ")
                        if choice == "1":
                            print("You decide that attempted to restore communications with HQ is your best shot at making the right decision.")
                            print("The communications center is structured almost entirely through the research room.")
                            print("You make your way through the main floor toward the research room and begin opening the airlock.")
                            print("After passing through the first door you enter the research room to find that it is intact.")
                            print("The room is filled with various points of study.")
                            print("There are supplies to garden, micropscopes and trays to study potential findings, a water filtration backup, and lastly a communications area.")
                            print("The area is made up of a large box and wires that run along the ship and connect to sattelite points outside.")
                            print("Upon inspection the communications area seems fine along with the rest of the research room as if it had not been impacted.")
                            print("The only other option was to check satellite points outside the ship, which also means you will figure out what impacted the ship.")
                            print("You make your way back to the main airlock where you initially got you spacesuit.")
                            print("You open the airlock, close the door behind you and begin to prepare for your spacewalk.")
                            print("There are small clips that you must fasten to the ship to make sure you are not taken too far from the ship.")
                            print("You open the door and make your way into space latching on to the bar above the door you float down and fasten the door behind you.")
                            print("Climbing above the airlock you can now see the top of the ship.")
                            print("The ship is build into layers stacked onto one another with various rooms branching out.")
                            print("The flight deck has 3 large solar sails attatched to it giving the ship the ability to move through space.")
                            print("As long as this stays intact the ship can move through space meaning the rest of the areas are expendable. You make your way past the solar sails to see the impact.")
                            print("There is a diamond shaped object resting on the top of the ship. The object is a silverish color but it appears to almost be fully reflective.")
                            print("While inspecting the object you can also clearly see that the communcations points outside of the research room are completeley destroyed from the impact of the object.")
                            print("This thing must have passed through the cargo bay and into the back of the ship directly hitting the crew quarters.")
                            print("Being that the object is so far back you could drop it into space along with the crew quarters.\nYou also can search the object to find out what it is.")
                            action6 = {1: 'Head back inside to remove that area of the ship', 2: 'Investigate the object closer'}
                            print(action6)
                            choice = input("Action 1 or 2? ")
                            if choice == "1":
                                print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates. The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates. You open the airlock from the outside and enter the ship. After closing the door you prepare to reenter the space ship again. You know that you are alone. Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates. Making your way toward the quarters you can hear something on the inside moving around. It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point. As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.")
                                action7 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                choice = input("Action 1 or 2? ")
                                if choice == "1":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\nYou face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\nYou no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\nThe door opens into a dark room with no oxygen as you had left it previously. You step inside looking around for Alex who was crying for help. There is no one immediately near the door as you would have expected from the cries. Just as fear, and doubt enter something cries out above you and drops from the ceiling.\nYou have failed your mission.")
                                elif choice == "2":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\nYou make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.\nYou make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\nThe threat that was on the ship threatening your life is now gone.\nYour only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")                    
                                    action7 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                    print (action7)
                                    choice = input("Action 1 or 2? ")
                                    if choice == "1":
                                        print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\nYou face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\nYou no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\nThe door opens into a dark room with no oxygen as you had left it previously. You step inside looking around for Alex who was crying for help. There is no one immediately near the door as you would have expected from the cries. Just as fear, and doubt enter something cries out above you and drops from the ceiling.\nYou have failed your mission.")
                                    elif choice == "2":
                                        print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\nYou make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.\nYou make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\nThe threat that was on the ship threatening your life is now gone.\nYour only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")

                        elif choice == "2":
                            print("You make your way back to the main airlock where you initially got you spacesuit.")
                            print("You open the airlock, close the door behind you and begin to prepare for your spacewalk.")
                            print("There are small clips that you must fasten to the ship to make sure you are not taken too far from the ship.")
                            print("You open the door and make your way into space latching on to the bar above the door you float down and fasten the door behind you.")
                            print("Climbing above the airlock you can now see the top of the ship.")
                            print("The ship is build into layers stacked onto one another with various rooms branching out.")
                            print("The flight deck has 3 large solar sails attatched to it giving the ship the ability to move through space.")
                            print("As long as this stays intact the ship can move through space meaning the rest of the areas are expendable. You make your way past the solar sails to see the impact.")
                            print("There is a diamond shaped object resting on the top of the ship. The object is a silverish color but it appears to almost be fully reflective.")
                            print("While inspecting the object you can also clearly see that the communcations points outside of the research room are completeley destroyed from the impact of the object.")
                            print("This thing must have passed through the cargo bay and into the back of the ship directly hitting the crew quarters.")
                            print("Being that the object is so far back you could drop it into space along with the crew quarters.\nYou also can search the object to find out what it is.")
                            action6 = {1: 'Head back inside to remove that area of the ship', 2: 'Investigate the object closer'}
                            print(action6)
                            choice = input("Action 1 or 2? ")
                            if choice == "1":
                                print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates. The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates. You open the airlock from the outside and enter the ship. After closing the door you prepare to reenter the space ship again. You know that you are alone. Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates. Making your way toward the quarters you can hear something on the inside moving around. It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point. As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.")
                                action7 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                choice = input("Action 1 or 2? ")
                                if choice == "1":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\nYou face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\nYou no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\nThe door opens into a dark room with no oxygen as you had left it previously. You step inside looking around for Alex who was crying for help. There is no one immediately near the door as you would have expected from the cries. Just as fear, and doubt enter something cries out above you and drops from the ceiling.\nYou have failed your mission.")
                                    break
                                elif choice == "2":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\nYou make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.\nYou make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\nThe threat that was on the ship threatening your life is now gone.\nYour only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")
                                    break
                            elif choice == "2":
                                print("You decide to investigate the object that landed on your ship. You make your way across the top of the ship toward the large reflective object.\nThere are no windows doors, or anything that look familiar to your ship. You get up next to the object and it seems like a mirror you can clearly see yourself in the reflection of the object.\nYou begin to search aroundthe side to see if you can find an entry point. There is a hole in the top of the ship leading to the crew quarters. Nearest to this hole look almost like a loading dock of a large cargo plane.\nYou can climb inside and further investigate this object or Head back inside the ship.")
                                action8 ={1: "Climb inside to investigate the object further", 2: "Head back inside the ship"}
                                print(action8)
                                choice = input("Action 1 or 2? ")
                                if choice == "1":
                                    print("You climb up the long loading dock being careful not to lose your footing on its reflective surface.\n")
                                    print("On your way up the tassle attached to you is not long enough to contiunue in.\n")
                                    print("At this point you have no choice but to release yourself from the tether of your ship. You untether yourself and enter the object.\n")
                                    print("On the inside the top of the object is just a long flat white light accompanied by the same reflective floor as before.\n")
                                    print("You walk deeper into the object to see what appears to be an elevated ring with nothing but two large black rings in front of it.")
                                    print("Behind you you hear the sound of the entrance lifting to close the object.\nYou rush back toward the entrance, but are much too late as the object seals shut")
                                    print("Along with the only known exit being shut the ship has no pressurized to normal gravity.\n")
                                    print("The spacesuit now is heavy and you cannot move unless you take it off. With no other option you begin to remove the suit starting with the helmet.\n")
                                    print("The air around you appears to be breathable, but as time goes on your eyes begin to feel heavy.\nThe suit is off but your body feels heavier than before.\n")
                                    print("The air must be knocking you out once again. You fall to the ground. You have failed your mission.\n")
                                elif choice == "1":
                                    print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates.\n")
                                    print("The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongings you brought onto the ship with you will be lost in space along with the remainof your crewmates.\nYou open the airlock from the outside and enter the ship.\nAfter closing the door you prepare to reenter the space ship again. You know that you are alone.\nCommunications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.\nMaking your way toward the quarters you can hear something on the inside moving around.\nIt is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.\nAs You are about to release the crew quarters you hear a voice callout 'Help its me Alex!' Knowing everything you saw on the inside of the crew quarters you now have to make a decision.")
                                    action9 = {1: "Open the airlock and save who is calling for help", 2: "Release the crew Quarters regardless of the cries"}
                                    print(action9)
                                    choice = input("Action 1 or 2? ")
                                    if choice == "1":
                                        print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.\n")
                                        print("You face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.\n")
                                        print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.\n")
                                        print("The door opens into a dark room with no oxygen as you had left it previously.\n")
                                        print("You step inside looking around for Alex who was crying for help.\nThere is no one immediately near the door as you would have expected from the cries.")
                                        print("Just as fear, and doubt enter something cries out above you and drops from the ceiling. You have failed your mission.")
                                        break
                                    elif choice == "2":
                                        print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.\n")
                                        print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.\nThe decision has already been made, and you pull the lever.\nThe ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                        print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.\n")
                                        print("The threat that was on the ship threatening your life is now gone.\n")
                                        print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.\n")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive. All there is to do now is wait out the days back to Earth.\n")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.\n")
                                        print("This means that all you have to do is wait for the ship to take you home.\n")
                                        print("This was the only true way to survive.\nYour comrades died in vein, but your objective is complete.\nYou have passed the mission.\n")
                                        
                                            



def objectivesurvival():
    print("Hello", nameofMC, "welcome to Objective: Survival") 
    prolouge()
    actionpart()
    
objectivesurvival()
