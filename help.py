from flask import Flask
from flask_ask import Ask, statement, request, context, question, session, convert_errors, version
from messenger import send_message

## https://developer.amazon.com/en-US/docs/alexa/alexa-design/adaptable.html

app = Flask(__name__)
ask = Ask(app, "/")

@app.route("/")
def homepage():
    return "Olá, Mundo!"

@ask.launch
def start_skill():
    welcome_message = "Certo, estarei realizando o contato agora mesmo."
    return question(welcome_message).reprompt("Consigo acessar os contatos e enviar mensagens de emergência.")

@ask.intent('SOSIntent', convert={'contact': str})
def emergency():
    # conectar com alexa
    if send_message() == 000:
        message = "Sua mensagem foi enviada."

    return statement(message)

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