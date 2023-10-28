from command import Command
import numpy as np
from buttons import Buttons
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import csv
scaler = StandardScaler()
# Load the model from the saved file
with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)
# Load the scaler from the saved file
with open('Scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
class Bot:

    def __init__(self):
        #< - v + < - v - v + > - > + Y
        self.fire_code=["<","!<","v+<","!v+!<","v","!v","v+>","!v+!>",">+Y","!>+!Y"]
        self.exe_code = 0
        self.start_fire=True
        self.remaining_code=[]
        self.my_command = Command()
        self.buttn= Buttons()
    
        
    def fight(self,current_game_state,player):
        #python Videos\gamebot-competition-master\PythonAPI\controller.py 1
        #start of my code
        
        if player == "1":
            if self.exe_code != 0:
                self.run_command([], current_game_state.player1)
            
            # Prepare the input data for prediction
            input_data = np.array([
            current_game_state.player1.player_id,
            current_game_state.player1.health,
            current_game_state.player1.x_coord,
            current_game_state.player1.y_coord,
            current_game_state.player1.is_jumping,
            current_game_state.player1.is_crouching,
            current_game_state.player1.player_buttons,
            current_game_state.player1.is_player_in_move,
            current_game_state.player1.move_id
        ]).reshape(1, -1)
            # Apply the same scaling as used during training
            input_data = scaler.transform(input_data)
            # Predict the button inputs using the model
            predicted_buttons = model.predict(input_data)
            
            # Set the predicted buttons as the player's buttons
            self.my_command.player_buttons = predicted_buttons
            
        elif player == "2":
            if self.exe_code != 0:
                self.run_command([], current_game_state.player2)
            
            # Prepare the input data for prediction
            input_data = np.array([
            current_game_state.player2.player_id,
            current_game_state.player2.health,
            current_game_state.player2.x_coord,
            current_game_state.player2.y_coord,
            current_game_state.player2.is_jumping,
            current_game_state.player2.is_crouching,
            current_game_state.player2.player_buttons,
            current_game_state.player2.is_player_in_move,
            current_game_state.player2.move_id
        ]).reshape(1, -1)
            # Apply the same scaling as used during training
            input_data = scaler.transform(input_data)
            # Predict the button inputs using the model
            predicted_buttons = model.predict(input_data)
            
            # Set the predicted buttons as the player's buttons
            self.my_command.player2_buttons = predicted_buttons
        
        return self.my_command

        """
        # Specify the CSV file path
        csv_file = 'GameData.csv'
        
        # Write data to the CSV file
       # Append data to the CSV file
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
            current_game_state.timer,
            current_game_state.fight_result,
            current_game_state.has_round_started,
            current_game_state.is_round_over,
            current_game_state.player1.player_id,
            current_game_state.player1.health,
            current_game_state.player1.x_coord,
            current_game_state.player1.y_coord,
            current_game_state.player1.is_jumping,
            current_game_state.player1.is_crouching,
            current_game_state.player1.is_player_in_move,
            current_game_state.player1.move_id,
            current_game_state.player2.player_id,
            current_game_state.player2.health,
            current_game_state.player2.x_coord,
            current_game_state.player2.y_coord,
            current_game_state.player2.is_jumping,
            current_game_state.player2.is_crouching,
            current_game_state.player2.is_player_in_move,
            current_game_state.player2.move_id,
            current_game_state.player1.player_buttons.up,
            current_game_state.player1.player_buttons.down,
            current_game_state.player1.player_buttons.right,
            current_game_state.player1.player_buttons.left,
            current_game_state.player1.player_buttons.select,
            current_game_state.player1.player_buttons.start,
            current_game_state.player1.player_buttons.Y,
            current_game_state.player1.player_buttons.B,
            current_game_state.player1.player_buttons.X,
            current_game_state.player1.player_buttons.A,
            current_game_state.player1.player_buttons.L,
            current_game_state.player1.player_buttons.R,
            current_game_state.player2.player_buttons.up,
            current_game_state.player2.player_buttons.down,
            current_game_state.player2.player_buttons.right,
            current_game_state.player2.player_buttons.left,
            current_game_state.player2.player_buttons.select,
            current_game_state.player2.player_buttons.start,
            current_game_state.player2.player_buttons.Y,
            current_game_state.player2.player_buttons.B,
            current_game_state.player2.player_buttons.X,
            current_game_state.player2.player_buttons.A,
            current_game_state.player2.player_buttons.L,
            current_game_state.player2.player_buttons.R
                    ])

        print("Data successfully stored in data.csv.")

        #end of my code upto here
        if player=="1":
            #print("1")
            #v - < + v - < + B spinning

            if( self.exe_code!=0  ):
               self.run_command([],current_game_state.player1)
            diff=current_game_state.player2.x_coord - current_game_state.player1.x_coord
            if (  diff > 60 ) :
                toss=np.random.randint(3)
                if (toss==0):
                    #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player1)
                    self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
                elif ( toss==1 ):
                    self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player1)
                else: #fire
                    self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
            elif (  diff < -60 ) :
                toss=np.random.randint(3)
                if (toss==0):#spinning
                    #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player1)
                    self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
                elif ( toss==1):#
                    self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player1)
                else: #fire
                    self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
            else:
                toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
                if ( toss>=1 ):
                    if (diff>0):
                        self.run_command(["<","<","!<"],current_game_state.player1)
                    else:
                        self.run_command([">",">","!>"],current_game_state.player1)
                else:
                    self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player1)
            self.my_command.player_buttons=self.buttn

        elif player=="2":

            if( self.exe_code!=0  ):
               self.run_command([],current_game_state.player2)
            diff=current_game_state.player1.x_coord - current_game_state.player2.x_coord
            if (  diff > 60 ) :
                toss=np.random.randint(3)
                if (toss==0):
                    #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player2)
                    self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
                elif ( toss==1 ):
                    self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player2)
                else:
                    self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
            elif ( diff < -60 ) :
                toss=np.random.randint(3)
                if (toss==0):
                    #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player2)
                    self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
                elif ( toss==1):
                    self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player2)
                else:
                    self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
            else:
                toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
                if ( toss>=1 ):
                    if (diff<0):
                        self.run_command(["<","<","!<"],current_game_state.player2)
                    else:
                        self.run_command([">",">","!>"],current_game_state.player2)
                else:
                    self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player2)
            self.my_command.player2_buttons=self.buttn
        return self.my_command
"""


    def run_command( self , com , player   ):

        if self.exe_code-1==len(self.fire_code):
            self.exe_code=0
            self.start_fire=False
            print ("compelete")
            #exit()
            # print ( "left:",player.player_buttons.left )
            # print ( "right:",player.player_buttons.right )
            # print ( "up:",player.player_buttons.up )
            # print ( "down:",player.player_buttons.down )
            # print ( "Y:",player.player_buttons.Y )

        elif len(self.remaining_code)==0 :

            self.fire_code=com
            #self.my_command=Command()
            self.exe_code+=1

            self.remaining_code=self.fire_code[0:]

        else:
            self.exe_code+=1
            if self.remaining_code[0]=="v+<":
                self.buttn.down=True
                self.buttn.left=True
                print("v+<")
            elif self.remaining_code[0]=="!v+!<":
                self.buttn.down=False
                self.buttn.left=False
                print("!v+!<")
            elif self.remaining_code[0]=="v+>":
                self.buttn.down=True
                self.buttn.right=True
                print("v+>")
            elif self.remaining_code[0]=="!v+!>":
                self.buttn.down=False
                self.buttn.right=False
                print("!v+!>")

            elif self.remaining_code[0]==">+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.right=True
                print(">+Y")
            elif self.remaining_code[0]=="!>+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.right=False
                print("!>+!Y")

            elif self.remaining_code[0]=="<+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.left=True
                print("<+Y")
            elif self.remaining_code[0]=="!<+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.left=False
                print("!<+!Y")

            elif self.remaining_code[0]== ">+^+L" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print(">+^+L")
            elif self.remaining_code[0]== "!>+!^+!L" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.L= False #not (player.player_buttons.L)
                print("!>+!^+!L")

            elif self.remaining_code[0]== ">+^+Y" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print(">+^+Y")
            elif self.remaining_code[0]== "!>+!^+!Y" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.Y= False #not (player.player_buttons.L)
                print("!>+!^+!Y")


            elif self.remaining_code[0]== ">+^+R" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print(">+^+R")
            elif self.remaining_code[0]== "!>+!^+!R" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.R= False #ot (player.player_buttons.R)
                print("!>+!^+!R")

            elif self.remaining_code[0]== ">+^+A" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print(">+^+A")
            elif self.remaining_code[0]== "!>+!^+!A" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.A= False #not (player.player_buttons.A)
                print("!>+!^+!A")

            elif self.remaining_code[0]== ">+^+B" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print(">+^+B")
            elif self.remaining_code[0]== "!>+!^+!B" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.B= False #not (player.player_buttons.A)
                print("!>+!^+!B")

            elif self.remaining_code[0]== "<+^+L" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print("<+^+L")
            elif self.remaining_code[0]== "!<+!^+!L" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.L= False  #not (player.player_buttons.Y)
                print("!<+!^+!L")

            elif self.remaining_code[0]== "<+^+Y" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print("<+^+Y")
            elif self.remaining_code[0]== "!<+!^+!Y" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.Y= False  #not (player.player_buttons.Y)
                print("!<+!^+!Y")

            elif self.remaining_code[0]== "<+^+R" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print("<+^+R")
            elif self.remaining_code[0]== "!<+!^+!R" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!<+!^+!R")

            elif self.remaining_code[0]== "<+^+A" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print("<+^+A")
            elif self.remaining_code[0]== "!<+!^+!A" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.A= False  #not (player.player_buttons.Y)
                print("!<+!^+!A")

            elif self.remaining_code[0]== "<+^+B" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print("<+^+B")
            elif self.remaining_code[0]== "!<+!^+!B" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.B= False  #not (player.player_buttons.Y)
                print("!<+!^+!B")

            elif self.remaining_code[0]== "v+R" :
                self.buttn.down=True
                self.buttn.R= not (player.player_buttons.R)
                print("v+R")
            elif self.remaining_code[0]== "!v+!R" :
                self.buttn.down=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!v+!R")

            else:
                if self.remaining_code[0] =="v" :
                    self.buttn.down=True
                    print ( "down" )
                elif self.remaining_code[0] =="!v":
                    self.buttn.down=False
                    print ( "Not down" )
                elif self.remaining_code[0] =="<" :
                    print ( "left" )
                    self.buttn.left=True
                elif self.remaining_code[0] =="!<" :
                    print ( "Not left" )
                    self.buttn.left=False
                elif self.remaining_code[0] ==">" :
                    print ( "right" )
                    self.buttn.right=True
                elif self.remaining_code[0] =="!>" :
                    print ( "Not right" )
                    self.buttn.right=False

                elif self.remaining_code[0] =="^" :
                    print ( "up" )
                    self.buttn.up=True
                elif self.remaining_code[0] =="!^" :
                    print ( "Not up" )
                    self.buttn.up=False
            self.remaining_code=self.remaining_code[1:]
        return
