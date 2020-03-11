#imports
import sys


#Listado
clients = ['pablo','gerardo']


#Create function
def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already in the client\'s list')


#Update function
def update_client(old_name, new_name):
    global clients

    if old_name in clients:
        name_index = clients.index(old_name)
        clients[name_index] = new_name
        list_clients()
    else:
        _not_register()
        pass


#Delete function
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
        list_clients()
    else:
        _not_register()
        pass


#Search function
def search_client(client_name):
    global clients
    

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def list_clients():
    global clients
    
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx, client))


#Command list
def print_welcome():
    print('Welcome to Project Ventas')
    print('*'*50)
    print('What would you like to do today? ')
    print('[C]reate client') 
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')   


#Privada
def _client_question():
    name_client = None

    while not name_client:    
        name_client = input('What is the client name? ')

        if name_client == 'exit':
            name_client = None
            break 
    #Cierra el programa    
    if not name_client:
        sys.exit()

    return name_client

def _not_register():
    print('Client its not in client\'s list')


#Start point of the code
if __name__ == '__main__':
    print_welcome()
    command = input()
    command = command.upper();

    if command == 'C':
        client_name = _client_question();
        create_client(client_name)
        list_clients()

    elif command == 'D':
        client_name = _client_question()
        delete_client(client_name)

    elif command == 'U':
        client_name = _client_question()
        new_name = input('What its the new client name? ')
        update_client(client_name,new_name)

    elif command == 'S':
        client_name = _client_question()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('Client {} not found'.format(client_name))
        
    else:
        print('Invalid command')
 