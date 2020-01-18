from simple_colors import *

##sc = magenta('hello','bold') + "world" 
##print(sc)
##print(green('hello', 'bold'))
##print(green('hello', ['bold', 'underlined']))

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

#print(strike('this should do the trick') + 'hello')

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



#===== CHAT =====
    #Directly after adding bot
"Welcome to sunny island of Singapore!"
"Hi! I am " + black('Durian King', 'bold')+ " the most " + strike('infamous') + " famous fruit in Singapore." 
"But sadly, do you know that bringing me on board the MRT is illegal?"
"But recently my overpowering smell has been detected on some carriages..."
"Let's catch and punish all the law breakers together!"
"Disclaimer: All views expressed in this game are the views of the owner. Please do not take this seriously"
    #/start

    #After /start 
"Proceed to Changi Airport MRT station platform to start your journey now."
    #press the button to open the moderator chat => MODERATOR

"Passengers:" #updates everytime someone joins
"{player} has successfully boarded the MRT!"
"Waiting for passengers to join the tour..."
"A minimum of {number} people is needed for the train to set off."

    #Game starts
"The train is now setting off."
"Please hold on to the grab poles or hand grips."

    #Passing through the tunnel
"Next station, <station>"
"Next station,<station>. The service will end at<>" # force stop the game and end in draw

"Your attention please, we are now passing through a tunnel, please do not be alarmed by the change in environment."
"Also, please be reminded that durians are not allowed on board trains."

"Meanwhile...an overwhelming durian smell permeates the train."
"Passengers you have "+ black('90', 'bold')+ " seconds to take action (if any)!"
"Passengers left: "
"{player}: Left/Still On Board"
    #=>MODERATOR to check role

    #Arrives at the next station
"<station>. Please mind the platform gap."

"I can't take the durian smell anymore! {player} flees from the MRT."
"{player} was a {role}"

"The train will stop at <station> station for " + black('120', 'bold') + " seconds."
"Passenger you have 120 seconds to discuss who might have brought durians on board the train before voting commences."
     # Updates player status + start discussing=> MODERATOR

#=====DESCRIPTION OF ROLES=====
### GOOD WITH SPECIAL ROLES ###

    #Durian Lover
"You are the Durian Lover!"
"Although you would love to bring durians on board, you are a law-abiding citizen."
"You can magically absorb all the durian smell 2 meter radius around you while the train passes through the tunnel."
"Therefore, you may choose to protect a fellow passenger from the smell of durian by standing next to them." #send once
"Choose who you want to protect." #repeated
        #List of choices
"<passenger> protected."


    #Pretend sleeper
"You are the Pretend Sleeper!"
"When the train passes through the tunnel, you can decide whether or not to pretend to sleep at the next station."
"If you pretend to sleep, you will not be chased out of the mrt even after being voted out but your role will be revealed."
"Choose wisely as you can only pretend to sleep " + black('twice', 'bold') + "." #send once
"Would you like to pretend to sleep at the nect station
        #List of choices
"You will (not) pretend to sleep at the next station."


    #Stomper
"You are the Stomper!"
"Equipped with an infrared camera, you can take a snap and check the role of another passenger when the train passes through the tunnel."
        #List of choices
"You have chosen to stomp {player}."
"{player} is the {role}."


###USELESS GOOD###
    #Aunty
"You are the Aunty!"
"You are just an everyday Singaporean taking the mrt."
"You have no special skills."
"You win with the other Singaporeans after chasing all xx out of the MRT."

    #Uncle
"Uncle"

    #Ah Boy
"Ah Boy"

    #Ah Girl
"Ah Girl"

###THE LAW BREAKERS/THE FEERLESS###
    #Durian King
"Durian King"
"DURIAN IS BAN ON THE TRAIN"

    #Durian Queen
"Durian Queen"

"Baby Durian"



#=====FUNCTIONS=====
    #/help
    #/start
    #/Player Description
    #/terms


