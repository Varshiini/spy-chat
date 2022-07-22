def start_chat(spy_name,spy_salutation,spy_age,spy_rating):
    welcome = 'authentication complete . welcome \n'
    name:' spy_salutation + spy_name \n'
    age:'+spy_age \n'
    rating:'+spy_rating \n'
    'proud to have you onboard'

show_menu=True
while show_menu:
     menu_choices="what do you want to do:\n "
     "1.add status\n"\
     "2.add friend\n"\
     "3.send message\n"\
     "4.real message\n"\
     "5.read chats\n"\
     "6.close\n\n"
     result=input(menu_choices)
     if(result==1):
         current_status=add_status(current_status)
     elif(result==2):
         no_of_friends=add_friend()
         print("you have %d friends"%(no_of_friends))
     elif(result==3):
         send_msg()
     elif(result==4):
          read_msg()
     elif(result==5):
          read_chat()
          show_menu=False
else:
    print("wrong choice,try again!")
    exit()






