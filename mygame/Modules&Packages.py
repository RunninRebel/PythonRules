#a module is a piece of software that has specific functionality. 
#Modules can have a set of functions, classes, or variables defined and implemented

#Example
#game.py
#Import the draw module
import draw

#import an idividual function like  draw_game into the main script namespace using the 'from' command
from draw import draw_game

#or you can import all by using '*'. Careful doing so because any any cahnges will affect your module
from draw import *

#Can change the name to a custom name to make it unique
if visual_mode:
    #in visual mode, we draw using graphics
    import draw_visual as draw
else:
    #in textual mode, we print out text
    import draw_textual as draw
    
    

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)
    

#this means that if the script is executed, then main() will be executed
if __name__ == '_main_':
    main() 
    

#module initialization. When initialized they are set as singletons
def draw_game():
    #when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    
    def clear_screen(screen):
        ...
        
    class Screen():
        ...
        
    #initiliaze main_screen as a singleton
    main_screen = Screen()
    
    
#extending module load path, these have to be declared before your imports
#PYTHONPATH= /foo python game.py

#or through sys func
sys.path.append("/foo")

#explore built-in modules https://docs.python.org/3/library/
#import libraries like urllib which enables to create read data from URLs
import urllib

#use it in this way 
urllib.urlopen(...)

#can look at what each module does by using dir
dir(urllib)

#once you find the function you want to use, you can read more about it with help
help(urllib.urlopen)

#writting pakages
#Packages are namespaces containing multiple packages and modules. Each package MUST contain a file called _init_.py. This indicates that the directory the file is in is a Python npackage