from flask import Flask
from flask_ask import Ask, statement, request, context, question, session, convert_errors, version

## https://developer.amazon.com/en-US/docs/alexa/alexa-design/adaptable.html

app = Flask(__name__)
ask = Ask(app, "/")

@app.route("/")
def homepage():
    return "Olá, Mundo!"

@ask.launch
def start_skill():
    welcome_message = "Certo, estarei realizando o contato agora mesmo."
    return question(welcome_message).reprompt("Consigo acessar os contatos, enviar mensagens e realizar chamadas de emergência.")


@ask.intent('SOSIntent')
def need_help():
    notification_message = "Sinto muito, ainda não posso fazer isto."
    return statement(notification_message)