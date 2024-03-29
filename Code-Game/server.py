import socket # for networking
import pickle # for sending/receiving objects 

# import the game
from tic_tac_toe import TicTacToe

HOST = '127.0.0.1' # this address is the "local host"
PORT = 12783       # port to listen on for clients  

# set up the server 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

client_socket, client_address = s.accept()
print(f"\nConnnected to {client_address}!")
otra = True
player_x = TicTacToe("X")
while otra:
    while True:
        host_response = input("\nBO1, BO3 o BO5: ").upper()
        if host_response == "BO1" or host_response == "BO3" or host_response == "BO5":
            break 
        else:
            print("Opcion invalida")
    host_response = host_response.upper()
    temp_host_resp = host_response
    client_response = ""

    host_response = pickle.dumps(host_response)
    client_socket.send(host_response)

    print("Waiting for client response...")
    client_response = client_socket.recv(1024)
    client_response = pickle.loads(client_response)

    tipo = ""

    if temp_host_resp == "BO1" and client_response == "Y":
        tipo = "BO1"
    elif temp_host_resp == "BO3" and client_response == "Y":
        tipo = "BO3"
    elif temp_host_resp == "BO5" and client_response == "Y":
        tipo = "BO5"

    rematch = True
    contador_x = 0
    contador_o = 0

    while rematch == True:
        partidas_totales = contador_o + contador_x + 1
        tries = 0
        
        # a header for an intense tic-tac-toe match! 
        print(f"\n\n T I C - T A C - T O E ")
        print(f"Partida N°{partidas_totales}")
        # the rest is in a loop; if either player has won, it exits 
        while (player_x.did_win("X", tipo, contador_x, contador_o) == False and player_x.did_win("O", tipo, contador_x, contador_o) == False and player_x.is_draw() == False):
            # draw grid, ask for coordinate
            print(f"\n       Your turn!")
            player_x.draw_grid()
            
            if tries >= 3:
                while True:
                    print("Ahora debe mover una X de lugar")
                    select_movement = input(f"Enter coordinate: ")
                    
                    if not player_x.ocupado(select_movement) or player_x.ocupado_rival(select_movement) == f"\033[94mO\033[0m":
                        print("No hay una X ahi")
                    else:
                    
                        notMoves = player_x.swap_position("X", select_movement)

                        if not notMoves:
                            print("No tenes movimientos. Intentá otra vez")
                            
                        else:                           
                            player_x.draw_grid()
                            break
            else:  
                while True:
                    player_coord = input(f"Enter coordinate: ")
                    if not player_x.ocupado(player_coord):
                        player_x.edit_square(player_coord)
                        tries += 1
                        break
                    else:
                        print("Ocupado")
            # draw the grid again
            player_x.draw_grid()

            # pickle the symbol list and send it 
            x_symbol_list = pickle.dumps(player_x.symbol_list)
            client_socket.send(x_symbol_list)

            # if the player won with the last move or it's a draw, exit the loop 
            if player_x.did_win("X", tipo, contador_x, contador_o) == "rojo" or player_x.is_draw() == True or player_x.did_win("X", tipo, contador_x, contador_o) == "continue" :
                break
            
            

            # wait to receive the symbol list and update it
            
            print(f"\nWaiting for other player...")
            o_symbol_list = client_socket.recv(1024)
            o_symbol_list = pickle.loads(o_symbol_list)
            player_x.update_symbol_list(o_symbol_list)

        # end game messages
        if player_x.did_win("X", tipo, contador_x, contador_o) == "continue":
            contador_x += 1
        if player_x.did_win("O", tipo, contador_x, contador_o) == "continue":
            contador_o += 1
        if player_x.did_win("X", tipo, contador_x, contador_o) == "rojo":
            player_x.colorear("red")
            print(f"\033[91mGanador color rojo\033[0m" )
            rematch = False     
        if player_x.did_win("X", tipo, contador_x, contador_o) == "continue":
            print(f"\033[91mGanador color rojo\033[0m" )
            player_x.restart()
            rematch = True
        elif player_x.is_draw() == True:
            print(f"It's a draw!")
        elif player_x.did_win("O", tipo, contador_x, contador_o) == "continue":
            player_x.restart()
            rematch = True
        else:
            rematch = False
            
        print("Victorias X: " + str(contador_x) + "Victorias O: " + str(contador_o))
            
        print(rematch)    
        
        if rematch == False:
                
            host_response = input(f"\nRematch? (Y/N): ")
            host_response = host_response.capitalize()
            temp_host_resp = host_response
            client_response = ""

            # pickle response and send it to the client 
            host_response = pickle.dumps(host_response)
            client_socket.send(host_response)

            # if the host doesn't want a rematch, we're done here
            if temp_host_resp == "N":
                otra = False
            # if the host does want a rematch, we ask the client for their opinion
            else:
                # receive client's response 
                print(f"Waiting for client response...")
                client_response = client_socket.recv(1024)

                client_response = pickle.loads(client_response)

                # if the client doesn't want a rematch, exit the loop 

                if client_response == "N":
                    print(f"\nThe client does not want a rematch.")
                    otra = False
                # if both the host and client want a rematch, restart the game
                else:
                    contador_o = 0
                    contador_x = 0
                    tries = 0
                    player_x.restart()
                    otra = True
                # ask for a rematch 

spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")
client_socket.close()

# errores victoria
