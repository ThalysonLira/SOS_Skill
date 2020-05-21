from pyzenvia import Sender
from .phone_book import ContactList

def send_message(list):
    # especificando usuario e senha
    sender = Sender("account", "password")

    # get list

    # preparando mensagem
    for c in ContactList.get_list():
        to = c['number']
        contact_name = c['name']
        user = "Fulano"
        message = "{}, {} precisa de ajuda urgentemente!".format(contact_name, user)

        # enviando mensagem
        response = sender.send(to, message)

        print("{} - {}".format(response['success'], response['result']))
    return response['success']

def check_list(list):
    if list is None:
        list = ContactList()
    return list

def add_contact(name, number):
    # get list

    # add
    ContactList.add_contact({
       # 'name': name,
       # 'number': number 
    })

def remove_contact(name):
    # get list

    # search contact

    # remove
    ContactList.remove_contact({
       # 'name': name,
       # 'number': number 
    })