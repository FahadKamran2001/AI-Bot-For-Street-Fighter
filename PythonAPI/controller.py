import socket
import json
import csv
from game_state import GameState
#from bot import fight
import sys
from bot import Bot
def connect(port):
    #For making a connection with the game
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", port))
    server_socket.listen(5)
    (client_socket, _) = server_socket.accept()
    print ("Connected to game!")
    return client_socket

def send(client_socket, command):
    #This function will send your updated command to Bizhawk so that game reacts according to your command.
    command_dict = command.object_to_dict()
    pay_load = json.dumps(command_dict).encode()
    client_socket.sendall(pay_load)

def receive(client_socket):
    #receive the game state and return game state
    pay_load = client_socket.recv(4096)
    input_dict = json.loads(pay_load.decode())
    game_state = GameState(input_dict)

    return game_state

def main():
     # Specify the CSV file path
    """csv_file = 'GameData.csv'
    
    # Write data to the CSV file
    # Append data to the CSV file
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ 'Timer', 'fight_result',
                        'has_round_started', 'is_round_over','player1_id', 'player1_health', 'player1_x_coord', 'player1_y_coord',
                        'player1_is_jumping', 'player1_is_crouching', 'player1_is_player_in_move',
                        'player1_move_id', 'player2_id', 'player2_health', 'player2_x_coord',
                        'player2_y_coord', 'player2_is_jumping', 'player2_is_crouching',
                        'player2_is_player_in_move', 'player2_move_id', 'player1_button_up',
                        'player1_button_down', 'player1_button_right',
                        'player1_button_left', 'player1_button_select',
                        'player1_button_start', 'player1_button_Y',
                        'player1_button_B', 'player1_button_X',
                        'player1_button_A', 'player1_button_L',
                        'player1_button_R', 'player2_button_up',
                        'player2_button_down', 'player2_button_right',
                        'player2_button_left', 'player2_button_select',
                        'player2_button_start', 'player2_buttons.Y',
                        'player2_button_B', 'player2_button_X',
                        'player2_button_A', 'player2_button_L',
                        'player2_button_R'])"""
    if (sys.argv[1]=='1'):
        client_socket = connect(9999)
    elif (sys.argv[1]=='2'):
        client_socket = connect(10000)
    current_game_state = None
    #print( current_game_state.is_round_over )
    bot=Bot()
    while (current_game_state is None) or (not current_game_state.is_round_over):

        current_game_state = receive(client_socket)
        bot_command = bot.fight(current_game_state,sys.argv[1])
        send(client_socket, bot_command)
if __name__ == '__main__':
   main()
