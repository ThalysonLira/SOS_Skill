from pyzenvia import Sender

def send_message():
    # especificando usuario e senha
    sender = Sender("account", "password")

    # preparando mensagem
    to = "contact"
    contact_name = "name"
    user = "name"
    message = "{}, {} precisa de ajuda urgentemente!".format(contact_name, user)

    # enviando mensagem
    response = sender.send(to, message)

    print(response['success'])
    print(response['result'])
    return response['success']