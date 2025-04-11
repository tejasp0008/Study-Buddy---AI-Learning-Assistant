from flask import Flask, render_template, session
from flask_session import Session
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os
from langchain import OpenAI, LLMChain, PromptTemplate

load_dotenv()

app = Flask(__name__)
app.secret_key = 'ReplaceWithYourSecretKey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

socketio = SocketIO(app, manage_session=False)

# Set up OpenAI LLM chain with langchain
api_key = os.getenv("OPENAI_API_KEY", "")
llm = OpenAI(temperature=0.7, openai_api_key=api_key)
template = "You are a helpful AI Assistant. Answer the following query in detail: {query}"
prompt = PromptTemplate.from_template(template)
chain = LLMChain(llm=llm, prompt=prompt)

def get_groq_response(query):
    groq_api_key = os.getenv("GROQ_API_KEY", "")
    # Dummy groq response; integrate real API call with groq_api_key later
    return "Groq response for: " + query

@socketio.on('send_message')
def handle_message(data):
    query = data.get('query', '')
    if not query:
        emit('receive_message', {'output': 'No input provided.'})
        return
    if query.lower().startswith("groq:"):
        response = get_groq_response(query.replace("groq:", "").strip())
    else:
        response = chain.run(query=query)
    memory = session.get('memory', [])
    memory.append({'query': query, 'response': response})
    session['memory'] = memory
    emit('receive_message', {'output': response})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
