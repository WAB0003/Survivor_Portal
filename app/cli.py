from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace
from rich.console import Console
import os

from models import *
# from helpers import *

engine = create_engine('sqlite:///survivor.db')
session = sessionmaker(bind=engine)()

clear = lambda : os.system('tput reset')
console = Console()

if __name__ == '__main__':
        # Main Menu function 
    def main_menu():
        clear()
        #ASCII TEXT
        console.print(r"""
   _____   _    _   _____   __      __  _____  __      __   ____    _____  
  / ____| | |  | | |  __ \  \ \    / / |_   _| \ \    / /  / __ \  |  __ \ 
 | (___   | |  | | | |__) |  \ \  / /    | |    \ \  / /  | |  | | | |__) |
  \___ \  | |  | | |  _  /    \ \/ /     | |     \ \/ /   | |  | | |  _  / 
  ____) | | |__| | | | \ \     \  /     _| |_     \  /    | |__| | | | \ \ 
 |_____/   \____/  |_|  \_\     \/     |_____|     \/      \____/  |_|  \_\                                                                         
""",style="green")
  
        
        print("Choose an option\n")
        print("1: Contestants")
        print("2: Seasons\n")
        print("Type 'exit' to leave cli")
        first_input = input("""
>>>""")

        if first_input == "1":
            clear()
            console.print("SURVIVOR CONTESTANTS",style="bold underline green")
            character_input= input("""Type * for a list of All Characters or type the name of character
>>>""")
            manage_characters_display(character_input)
            
        elif first_input == "2":
            clear()
            console.print("SURVIVOR SEASONS",style="bold underline purple")
            season_input= input("""
Type * for a list of All Seasons or type the season NUMBER to see info
                                Type 'menu' to go back to Menu
                                Type exit to end cli
>>>""")
            manage_seasons_display(season_input)

        else: 
            print("Error")
            pass
    #!Character Page
    def manage_characters_display(character_input):
        clear()
        console.print("SURVIVOR CONTESTANTS",style="bold underline green")
        #* ALL CHARACTERS
        if character_input == "*":
            clear()
            console.print("SURVIVOR CONTESTANTS: ALL",style="bold underline green")
            all_contestants = session.query(Contestant.name).all()
            for contestant in all_contestants:
                print(contestant[0])
            next_input = input("""
Type Character Name from Above to view
                               
                               Type 'menu' to go back to Menu
                               Type exit to end cli
>>>""")
            manage_characters_display(next_input)
        elif character_input == "menu":
            main_menu()
        elif character_input == "exit":
            pass
        #* SINGLE OR MULTIPLE SURVIVOR CONTESTANTS
        else:
            clear()
            console.print("SURVIVOR CONTESTANTS",style="bold underline green")
            query = session.query(Contestant).filter(Contestant.name.like(f'%{character_input}%')).all()
            if query:
                for each_query in query:
                    print(each_query)                
            else:
                new_input = input("""No one with that name. Please type name that exists or type menu:
                      >>>""")
                manage_characters_display(new_input)
            next_input = input("""
                               Type 'menu' to go back to Menu
                               Type exit to end cli
>>>""")
            manage_characters_display(next_input)
                
                
    #!Season page Page 
    def manage_seasons_display(season_input):
        clear()
        #* ALL SEASONS DISPLAY
        if season_input == "*":
            clear()
            console.print("SURVIVOR SEASONS: ALL\n",style="bold underline purple")
            all_seasons = session.query(Season).all()
            for season in all_seasons:
                print(f'Season {season.id}: {season.name}')
            season_num = input("""
Type the season NUMBER from above to see info
                               Type 'menu' to go back to Menu
                               Type exit to end cli
>>>""")     
            season_input = int(season_num)
            manage_seasons_display(season_input)
        
        elif season_input=="exit" or season_input=="menu":
            menu_or_exit(season_input)
        #!For some reason i don't think input is  nuber
        else:            
            query = session.query(Season).filter(Season.id == int(season_input)).first()
            print(query)
            
            
            
            
    def menu_or_exit(input):
        if input=="menu":
            main_menu()
        elif input =="exit":
            pass
                
        


  # Now we call the method once outside of the definition, but inside the "__main__"
    main_menu()
    
  # Goodbye Message
    clear()
    print("Thanks for using my CLI!")