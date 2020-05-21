from flask import Flask
from flask_ask import Ask, statement, request, context, question, session, convert_errors, version
from util.messenger import send_message, check_list, add_contact, remove_contact

## https://developer.amazon.com/en-US/docs/alexa/alexa-design/adaptable.html

app = Flask(__name__)
ask = Ask(app, "/")

@app.route("/")
def homepage():
    return "Olá, Mundo!"

@ask.launch
def start_skill():
    welcome_message = "Olá, em que posso te ajudar?"
    return question(welcome_message).reprompt("Consigo acessar os contatos e enviar mensagens de emergência.")

@ask.intent('SOSIntent', convert={'name':str, 'phone':str})
def emergency(list):

    if list is None:
        return statement("Desculpe, mas sua lista de emergência está vazia!")

    if send_message(list) == 000:
        message = "Sua mensagem foi enviada."

    return statement(message)

@ask.intent('AddContactIntent', convert={'name':str, 'phone':str})
def add(list):

    name = question("Qual o nome do contato?")
    phone = question ("Qual o número de telefone?")

    add_contact(name, phone)
    return statement("Foi adicionado um novo contato em sua lista de emergência!")

@ask.intent('RemoveContactIntent', convert={'name':str, 'phone':str})
def remove(list):

    contact = question("Qual o nome do contato?")

    remove_contact(contact)
    return statement("Foi adicionado um novo contato em sua lista de emergência!")

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Certo, até mais!")

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Certo, até mais!")

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == "__main__":
    app.run(debug=True)
