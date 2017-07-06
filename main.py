
from spy_details import spy ,Spy,ChatMessage,friends
from termcolor import colored
from steganography.steganography import Steganography

#Let's start
print "Hello!"
print "Let's  app get started"

spy_name = raw_input("Welcome to spy_chat , you must tell your spy_name first: ")


if len(spy_name)> 0 :


    print " Welcome  " + spy_name + " . Glad to have you back with us."
    spy_salutation = raw_input("Should I call you Mister or Miss? : " )
    spy_name = spy_salutation + " " + spy_name

    print "Alright "  + spy_name + ". I'd like to know a little bit more about you before we proceed. : "

    spy_age = 0
    spy_rating = 0
    spy_is_online =  False


    spy_age = int(raw_input("What is your age ?"))

#Defining age limitaions to start the chat
    if spy_age > 12 and spy_age < 50 :

        spy_rating = float(raw_input( "What is your spy_rating?" ))

        if spy_rating > 4.5 :
             print " Great ace! "
        elif spy_rating > 3.5 and spy_rating <=4.5:
            print " You are one of the good ones."
        else :
           print "We can always use somebody to help in the office."
           spy_is_online = True
           print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of : " +  str( spy_rating) + " Proud to have you onboard ."
    else :
        print  "Sorry you are not of the correct age to be a spy."
else :
    print " A spy  needs to ahve a valid name. Try again please."
#Creating variable to store older status messages
STATUS_MESSAGES = ['My name is Bond , James Bond' ,'Shaken, not stirred. ','Keeping the British end up , Sir']

friends = []

print "Hello! Let's get started"

question = 'Do you want to continue as ' +spy.salutation + " " + spy.name+ " (Y/N)?"
existing = raw_input(question)

#Function to add a status message
def add_status():
    updated_status_message = None

    if spy.current_status_message != None :
        print " Your current_status_message is %s \n " %(spy.current_status_message)
    else :
        print "You don\'t have any status message currently \n "

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input('What status message do you want to set ?')
#TO check wheather new status message is updated or not
        if len(new_status_message) > 0 :
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print STATUS_MESSAGES
    elif default.upper() == "Y" :

        item_position = 1

        for message in STATUS_MESSAGES :
            print str(item_position ) + "." + message
            item_position = item_position + 1

        message_choice = int(raw_input("\n Choose from above message"))

        if len(STATUS_MESSAGES) >= message_choice :
            updated_status_message = STATUS_MESSAGES[message_choice - 1]
        else :
            print ' BUZZZZ'


    else :
        print " The option you chose is not valid! Press either y or n."

    if updated_status_message:
        print ' Your updated status message is: %s ' % (updated_status_message)
    else :
        print 'You current did not have a status message'

    return updated_status_message
#Adding a new friend
def add_friend():

    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.? ")

    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = int(raw_input("Age"))

    new_friend.rating = float(raw_input("Spy rating"))

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy_rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else :
        print  ' Sorry! Invalid entry. We can not add spy with the details you provided'
    return  len(friends)

def select_friend():
   item_number = 0

   for friend in friends:
       print '%d. %s aged %d with rating % .2f is online' % (item_number+1, friend.name,friend.age,friend.rating)
       item_number = item_number + 1
   friend_choice = raw_input("Choose from your friends")

   friend_choice_position = int(friend_choice)-1

   return friend_choice_position

#Defining a function to send a secret message
def send_message():
    friend_choice = select_friend()
    original_image= raw_input("What is the name of the image?")
    output_path ="C:\Users\jitender singh\Desktop\secret\output.jpg"
    text = raw_input("What do you want to say?")
    if len(text)<=100:
        Steganography.encode(original_image,output_path,text)
    else:
        print"The length of message text exceeded"

    new_chat = ChatMessage(text, True)


    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready!"

#Defining a function to read a secret message
def read_message():

    sender = select_friend()

    secret_text = Steganography.decode("C:\Users\jitender singh\Desktop\secret\output.jpg")
    print (secret_text)

    new_chat = ChatMessage(secret_text, False)
    friends[sender].chats.append(new_chat)

    print 'Your secret message has been saved!'


#Let's read chat history of selected friend
def read_chats_history():
    friend = select_friend()
    print '\n'
    for  chats in friends[friend].chats:
          if chats.sent_by_me:
              print colored('[%s] %s: %s' % (chats.time.strftime("%d %B %Y"), 'you said:', chats.message),'blue')
          else :
              print colored ('[%s] %s said: %s' % (chats.time.strftime("%d %B %Y"),  friends[friend].name, chats.message),'blue')
#Let's start the chat
def start_chat(spy):

    current_status_message = None

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50 :
        print  " Authantication complete . Welcome " + spy.name + " age: " + str(spy.age) + " and rating of :" + str(spy.rating) + "Proud to have you onboard"

        show_menu = True

        while show_menu :
            menu_choices = "What do you want to do ? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close application \n "
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0 :
                menu_choice = int(menu_choice)

                #set status
                if menu_choice == 1:
                    print 'Please update your status'
                    spy.current_status_message = add_status()
                elif menu_choice == 2 :
                    print 'Please add a new friend '
                    number_of_friends = add_friend()
                    print 'You have %d friends' %(number_of_friends)
                elif menu_choice == 3:
                    print 'PLease choose to send a secret message'
                    send_message()
                elif menu_choice == 4:
                    print'PLease choose to read a secret message from sender'
                    read_message()
                elif menu_choice == 5:
                    print'Read chat history'
                    read_chats_history()
                else :
                    show_menu = False
    else :
        print "Sorry you are not of the correct age to be a spy"
if existing == "Y":
    start_chat(spy)
else :
    spy = Spy('','',0,0.0)

    spy.name = raw_input(" Welcome to spy chat , you must tell me your spy name first :")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms. ? :")

        spy.age = int(raw_input("What is your age ? "))


        spy.rating = float(raw_input("What is your spy_rating"))

        spy_is_online = True
        start_chat(spy)
    else :
        print "Please add a valid spy name"




