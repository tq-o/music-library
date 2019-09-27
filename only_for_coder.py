#song list 

songList = []

def song_add(): #Song Adding
    add_option=True

    while add_option==True:
        add_cont=True
        add_song = input( str ("Please tell me what's the song you want to add?: ") ) #add song
        
        if add_song in songList:
            print("You downloaded it already.") #downloaded already

        else:
                songList.append(add_song) #added to list
                song_print()

        while add_cont == True:

            add_option_cont= input(str("Do you want to add more? (Y/N): ")) #continue or not
            if add_option_cont == "Y":
                add_option=True
                break
                
            if add_option_cont == "N":
                add_option=False
                add_cont=False
                break

            else:
                print("Sorry, wrong input. Please type again!")
                add_cont=True
    return songList

def song_delete():
    delete_option= True
    
    while delete_option == True:    
        delete_option_cont = True
        song_delete = input(str("Please tell what song you want to remove?: ")) #ask song to delete 

        if song_delete in songList:  #song exist
            songList.remove(song_delete)
            song_print()

        else: #song not exist
            print("Song not in list bitch. Check again.")
        while delete_option_cont == True:

            delete_option_cont= input(str("Do you want to delete more? (Y/N): ")) #continue or not
            if delete_option_cont == "Y":
                delete_option = True
                break

            if delete_option_cont == "N":
                delete_option = False
                delete_option_cont = False
                break
            else:
                print("Wrong input. OMG, Are you blind?")
                delete_option_cont = True

    return song_delete

def song_exist(): #trying to fix the printing time
    songExist = True
    while songExist:
        song_exist = input(str("What song you want to SEARCH?\nPlease Enter:")) #Ask if the song is in the list 
        if song_exist in songList:
            print("Yup, you've got it!")
        
           
        else:
            print("Uh oh, I think this song is not on your list.")
            
        
        continue_question = input(str("Continue? (Y/N)"))
        if continue_question == "Y": songExist = True
        elif continue_question == "N": songExist = False
        
    return song_exist

def song_print():
    print(songList)    

