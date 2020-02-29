clients = 'pablo, gerardo, '

#Create function
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

#Update function
def update_client(old_name, new_name):
    global clients

    if old_name in clients:
        clients = clients.replace(old_name+',', new_name+',' )
        list_clients()
    else:
        print('Client its not in client\'s list')
        pass


def list_clients():
    global clients
    
    print(clients)


def print_welcome():
    print('Welcome to Project Ventas')
    print('*'*50)
    print('What would you like to do today? ')
    print('[C]reate client') 
    print('[D]elete client')
    print('[U]pdate client')   


#Privada
def _client_question():
    name_client = input('What is the client name? ') 
    return name_client


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
        pass
    elif command == 'U':
        client_name = _client_question();
        new_name = input('What its the new client name? ')
        update_client(client_name,new_name)
        pass
    else:
        print('Invalid command')
 