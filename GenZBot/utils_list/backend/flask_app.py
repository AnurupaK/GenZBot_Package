##Gemini
def backendCode_gemini():
    return """
from flask import Flask, request, jsonify, render_template
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))
from AIResponse import  get_gemini_response

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")


@app.route('/')
def home():
    return render_template('index.html')

    
@app.route('/api/aiResponse',methods=['POST'])
def text_response():
    data = request.get_json()
    input = data['Userinput']
    print("User Input",input)
    
    response = get_gemini_response(input)
    print(response)
    return jsonify({'botResponse': response})
    
if __name__ == "__main__":
    app.run(debug=True)
"""

##OpenAI
def backendCode_openai():
    return """
from flask import Flask, request, jsonify, render_template
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))
from AIResponse import get_openai_response, clear_conversation_history

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")


@app.route('/')
def home():
    clear_conversation_history()
    return render_template('index.html')

    
@app.route('/api/aiResponse',methods=['POST'])
def text_response():
    data = request.get_json()
    input = data['Userinput']
    print("User Input",input)
    
    response = get_openai_response(input)
    print(response)
    return jsonify({'botResponse': response})
    
if __name__ == "__main__":
    app.run(debug=True)
"""

##Llama
def backendCode_llama():
    return """
from flask import Flask, request, jsonify, render_template
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))
from AIResponse import get_llama_response, clear_conversation_history

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")


@app.route('/')
def home():
    clear_conversation_history()
    return render_template('index.html')

    
@app.route('/api/aiResponse',methods=['POST'])
def text_response():
    data = request.get_json()
    input = data['Userinput']
    print("User Input",input)
    
    response = get_llama_response(input)
    print(response)
    return jsonify({'botResponse': response})
    
if __name__ == "__main__":
    app.run(debug=True)
"""


##Gemma
def backendCode_gemma():
    return """
from flask import Flask, request, jsonify, render_template
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))
from AIResponse import get_gemma_response, clear_conversation_history

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")


@app.route('/')
def home():
    clear_conversation_history()
    return render_template('index.html')

    
@app.route('/api/aiResponse',methods=['POST'])
def text_response():
    data = request.get_json()
    input = data['Userinput']
    print("User Input",input)
    
    response = get_gemma_response(input)
    print(response)
    return jsonify({'botResponse': response})
    
if __name__ == "__main__":
    app.run(debug=True)
"""


##Mixtral
def backendCode_mixtral():
    return """
from flask import Flask, request, jsonify, render_template
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))
from AIResponse import get_mixtral_response, clear_conversation_history

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")


@app.route('/')
def home():
    clear_conversation_history()
    return render_template('index.html')

    
@app.route('/api/aiResponse',methods=['POST'])
def text_response():
    data = request.get_json()
    input = data['Userinput']
    print("User Input",input)
    
    response = get_mixtral_response(input)
    print(response)
    return jsonify({'botResponse': response})
    
if __name__ == "__main__":
    app.run(debug=True)
"""


