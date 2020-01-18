from simple_colors import *

##sc = magenta('hello','bold') + "world" 
##print(sc)
##print(green('hello', 'bold'))
##print(green('hello', ['bold', 'underlined']))

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

#print(strike('this should do the trick') + 'hello')

#print("\U0001F62D") cry
#print("\U0001f92c")redangry
#print("\U0001f922")green face
#print("\U0001f4a2")#annoyed
#print("\U0001f92e")#puck
#print("\U0001f634")#sleeping
#print("\U0001f60d")#heart


#===== MODERATOR =====
    #What can this bot do?
"Durian King here. I will be facilitating your MRT journey."
"Thank you for using Durian King's services and have a pleasant journey."
    #=> CHAT First Message(after button is pressed)
"Your attention please, the last train will arrive at the platform shortly. "
"Please board the train immediately, thank you."
"Use /."
"Learn all about "

    # clicks board 
"You have successfully boarded the MRT at Changi Airport Station."
"Waiting for more passengers..."
    #=>CHAT

    #=>CHAT to check role
        #check roles below

    #Arrives at next station
        #FLED
"You cannot stand the durian smell liao and have fled from the MRT." + "\U0001f922"
        #CHASED AWAY
"OHOR! Is it you carrying durian???" + "\U0001f92c" 
"The other passengers suspect that you might have brought durians on board and have thus, chased you off the MRT."

#===== CHAT =====
    #Directly after adding bot
"Welcome to the sunny island of Singapore!"
"Hi! I am " + black('Durian King', 'bold')+ " the most " + strike('infamous') + " famous fruit in Singapore." 
"But do you know that bringing me on board the MRT is illegal?" + "\U0001f62D"
"But recently my overpowering smell has been detected on some carriages..." + "\U0001f4a2"
"Let's catch and punish all the law breakers together!"
"Disclaimer: All views expressed in this game are the views of the owner. Please do not take this seriously"
    #/start

    #After /start 
"Proceed to Changi Airport MRT station platform to start your journey now."
    #press the button to open the moderator chat => MODERATOR

"Passengers:" #updates everytime someone joins
"{player} has successfully boarded the MRT!"
"Waiting for passengers to board the train..."
"Need at least {number} people for the train to set off leh." 

    #Game starts
"{number} passengers on board liao. The train will now depart. Doors closing!"
"Please hold on to the grab poles or hand grips."

    #Passing through the tunnel
"Next station, <station>."
"Next station,<station>. The service will end at<>" # force stop the game and end in draw

"Your attention please, we are now passing through a tunnel, please do not be alarmed by the change in environment."
"Also, please be reminded that durians are not allowed on board trains."

"Meanwhile...an overwhelming durian smell permeates the train..." + "\U0001f62D"
"Passengers you have "+ black('90', 'bold')+ " seconds to take action (if any)!"
"Passengers left: "
"{player}: Left/Still On Board"
    #=>MODERATOR to check role

    #Arrives at the next station
"<station>. Please mind the platform gap."
        #V1
"I can't take the durian smell anymore!" + "\U0001f92e"
"{player} flees from the MRT."
"{player} was a {role}"#same as the other version
        #V2
"COUGHS! COUGHS! Save me!!!" + "\U0001f92e"
        #V3
"I am never going near durians again!" + "\U0001f92e"
        #V4
"{player} dashes out of the MRT. BLEURGH!" + "\U0001f92e"


"The train will stop at <station> station for " + black('120', 'bold') + " seconds."
"Passenger you have 120 seconds to discuss who might have brought durians on board the train before voting commences."
     #Updates player status + start discussing=> MODERATOR

     #Voting
"The train is departing soon. Passengers who you want to chase off the MRT???"
"Passengers you have "+ black('90', 'bold')+ " seconds to vote!"
"{player} has voted to chase off {player}"

    #After voting
"The passengers cast votes liao, amid doubts and suspicions,{player} has been chased off the MRT. {player} was the {role}."

    #Game continues => #Passing through the tunnel
    #Game Ends
"The durians have overpowered everyone again!"#durians win
"The durians have been eradicated!"#sg win
    #Print player status with win/lost


#=====DESCRIPTION OF ROLES=====
### GOOD WITH SPECIAL ROLES ###

    #Durian Lover
"You are the Durian Lover!" + "\U0001f60d"
"Although you would love to bring durians on board, you are a law-abiding citizen."
"You can magically absorb all the durian smell 2 meter radius around you while the train passes through the tunnel leh."
"Tha's why, you may choose to protect a fellow passenger from the smell of durian by standing next to them." #send once
"Who you want to protect?" #repeated
        #List of choices
"You protected <passenger>."


    #Pretend sleeper
"You are the Pretend Sleeper!"+ "\U0001f634"
"When the train passes through the tunnel, you can decide whether or not to pretend to sleep at the next station a not."
"If you pretend to sleep, you will not be chased out of the mrt even after being voted out but your role will be revealed horh."
"Choose wisely as you can only pretend to sleep " + black('twice', 'bold') + "." #send once
"Would you like to pretend to sleep at the next station a not?"#repeated
        #List of choices
"You (did not) pretend to sleep at the next station."


    #Stomper
"You are the Stomper!"
"Equipped with an infrared camera, you can take a snap and check the role of another passenger when the train passes through the tunnel."
"Who you want to stomp?"#repeated
        #List of choices
"You stomped {player}."
"{player} is the {role}."


###USELESS GOOD###
    #Old Auntie
"You are the Old Auntie!"
"You are just an everyday Singaporean taking the mrt so you no skills lorh."
"You win after chasing the Durian family out of the MRT. Easy Peasy, Lemon Squeezy!"

    #Old Uncle
"You are the Old Uncle!"
"You are just an everyday Singaporean taking the mrt so you no skills lorh."
"You win after chasing the Durian family out of the MRT. Easy Peasy, Lemon Squeezy!"

###THE DURIANS###
    #Durian King 
"You are the Durian King!"
"Durian is banned on board the MRT but you heck care."
"Decide who to chase off the MRT at the next station. The passenger with the majority vote will get chased off."
"If there is no majority vote, no one gets chased off." #same as queen and maybe baby
"Who you want to chase off the MRT?" #repeated
        #List of choices
"You chased {player} off the MRT!"

    #Durian Queen
"You are the Durian Queen!"


    #Baby Durian
"You are the Baby Durian!"


#=====GAME INFO=====
"Welcome to the sunny island of Singapore!"
"Hi! I am " + black('Durian King', 'bold')+ " the most " + strike('infamous') + " famous fruit in Singapore." 
"But do you know that bringing me on board the MRT is illegal?" + "\U0001f62D"
"But recently my overpowering smell has been detected on some carriages..." + "\U0001f4a2"
"Let's catch and punish all the law breakers together!"
"Disclaimer: All views expressed in this game are the views of the owner. Please do not take this seriously"

"Board at Changi Airpot station to start your MRT journey now!"
"The Durian king and his family with a heck care attitude has time and again brought durians on board the MRT while"
"the other law-abiding Singaporeans cannot wait to chase Durian King and his family off the MRT."
"Take on randomly assigned roles of Durian Kings, Stompers, Pretend Sleepers and more..."
"A fun game of wit and deception where you can learn more about personalities who are often seen on the MRT and Singlish!"

"Add @{bot} to your telegram chat group now!" 


