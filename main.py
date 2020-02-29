clients = 'pablo, gerardo, '

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print('Client already in the client\'s list')

def _add_coma():
    global clients
    
    clients += ','


def list_clients():
    global clients
    
    print(clients)

def print_welcome():
    print('Welcome to Project Ventas')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client') 
    print('[D]elete client')  

#Start point of the code
if __name__ == '__main__':
    print_welcome()
    command = input()

    if command == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == D:
        pass
    else:
        print('Invalid command')
 