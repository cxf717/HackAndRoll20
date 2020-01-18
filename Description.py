from simple_colors import *

##sc = magenta('hello','bold') + "world" 
##print(sc)
##print(green('hello', 'bold'))
##print(green('hello', ['bold', 'underlined']))

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

print(strike('this should do the trick') + 'hello')

#===== MODERATOR =====
    #=> CHAT First Message(after button is pressed)
"Once again, I am Durian King and thank you for joining my " + black('damn good', 'bold') + " tour on Singapore's MRT system."
"The train will be arriving soon so please be patient."
"Use /."
"Learn all about "

    #Second Message(announcement)=> 3 second?
"Your attention please, the last train will arrive at the platform shortly. "
"Please board the train immediately, thank you."

    # clicks board 
"You have successfully boarded the MRT at Changi Airport Station and joined Durian King' tour."
"Waiting for more passengers..."
    #=>CHAT

    #=>CHAT to check role
        #check roles below



#===== CHAT =====
    #Directly after adding bot
"Welcome to sunny island of Singapore!"
"I am " + black('Durian King', 'bold')+ " the most " + strike('infamous') + " famous fruit in Singapore, but some would" 
"Despite never having taken the MRT myself, I know all there is about it!"
"Do you know that bringing durians, arguably the most infamous fruit in Singapore, on board the MRT is illegal?"
"But recently the overpowering durian smell has been detected on some carriages..."
"Let's catch and punish all the law breakers together!"
"Disclaimer: All views expressed in this game are the views of the owner. Please do not take this seriously"
    #/start

    #After /start 
"Proceed to Changi Airport MRT station platform to start your journey now."
    #press the button to open the moderator chat => MODERATOR

"Tour members:" #updates everytime someone joins
"{player} has successfully boarded the MRT!"
"Waiting for more people to join the tour..."
"Tour requires a minimum of 8 people to start"

    #Game starts
"The tour is now starting...please wait while your particulars are being updated."

    #Passing through the tunnel
"Next station, <station>"
"Next station,<station>. The service will end at<>" # force stop the game and end in draw

"Your attention please, we are now passing through a tunnel, please do not be alarmed by the change in environment."
"Also, please be reminded that durians are not allowed on board trains."

"Meanwhile...an overwhelming durian smell permeates the train."
"Tour members you have "+ black('90', 'bold')+ " seconds to take action (if any)!"
"Members left: "
"{player}: Left/Still On Board"
    #=>MODERATOR to check role

    #Arrives at the next station
"<station>. Please mind the platform gap."

"I can't take the durian smell anymore! {player} flees from the MRT."
"{player} was a {role}"

"The train has arrived at <station> station."
"Tour members you have " + black('120', 'bold') + " seconds to discuss who might have brought durians on board the train before voting commences."
     # Updates player status + start discussing=> MODERATOR

#=====DESCRIPTION OF ROLES=====
### GOOD WITH SPECIAL ROLES ###

    #Durian Lover
"You are the Durian Lover!"
"Although you would love to bring durians on board, you are a law-abiding citizen."
"You can magically absorb all the durian smell 2 meter radius around you while the train passes through the tunnel."
"Therefore, you may choose to protect a fellow tour member from the smell of durian by standing next to them."
        #List of chioces
"<tour member> protected."


    #Pretend sleeper
"You are the Pretend Sleeper!"
"When the train passes through the tunnel, you can decide whether or not to pretend to sleep at the next station."
"If you pretend to sleep, you will not flee from the mrt even after being voted out but your role will be revealed."
"Choose wisely when you would like to pretend to sleep as you can only do so twice."
        #List of choices
"You will (not) pretend to sleep at the next station."


    #Stomper
"You are the Stomper!"
"Equipped with an infrared camera, you can take a snap and check the role of another tour member when the train passes through the tunnel."
"Your local version of citizen reporters here in Singapore that captures your everymove and posts them online"
"ROLE IG: equipped with infrared camera to help catch the lawless while MRT passesthrough the tunnel"

###USELESS GOOD###
    #Aunty
"Aunty"

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


