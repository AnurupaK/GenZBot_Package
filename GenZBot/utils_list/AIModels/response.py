# Gemini_Response function generates code for a Gemini-based chatbot
def Gemini_Response(system_instruction=None):
    if system_instruction is None:
        system_instruction = "You are a helpful, friendly, and concise chatbot designed to assist users by providing clear, accurate, and relevant information."
    
    return f"""
# Import necessary libraries and load environment variables
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

# API key setup and Gemini model configuration
api_key_gemini = os.getenv("GOOGLE_API_KEY")
if not api_key_gemini:
    raise ValueError("API key for Google Generative AI is not set in the environment variables.")

genai.configure(api_key=api_key_gemini)

# Chatbot setup with instructions
generation_config = {{
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 100,
    "response_mime_type": "text/plain",
}}

instruction = "{system_instruction}"

gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=instruction
)

# Function to interact with Gemini AI and get responses
chat_session_gemini = gemini.start_chat(history=[])

def get_gemini_response(prompt):
    try:
        response  = chat_session_gemini.send_message(prompt)
        return response.text
    except Exception as e:
        return "Oops! it seems I didn't get your question"
"""

# Groq_Response function generates code for different LLMs (Llama, Gemma, Mixtral) chatbots
def Groq_Response(model, system_instruction=None):
    if model.lower() == "llama":
        key_name = "LLAMA_API_KEY"
        model_name = "llama-3.1-8b-instant"
        function_name = "get_llama_response"
    elif model.lower() == "gemma":
        key_name = "GEMMA_API_KEY"
        model_name = "gemma2-9b-it"
        function_name = "get_gemma_response"
    elif model.lower() == "mixtral":   
        key_name = "MIXTRAL_API_KEY"
        model_name = "mixtral-8x7b-32768"
        function_name = "get_mixtral_response"
    else:
        raise ValueError(f"Invalid model '{model}'. Valid options are: 'openai','gemini','llama', 'gemma', 'mixtral'.")

    system_instruction = system_instruction or "You are a helpful, friendly, and concise chatbot designed to assist users by providing clear, accurate, and relevant information."

    return f"""
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# API key setup and Groq client initialization
api_key = os.getenv("{key_name}")
if not api_key:
    raise ValueError("API key for {model} AI is not set in the environment variables.")

client = Groq(api_key=api_key)

# Function to reset chat history
conversation_history = []

def clear_conversation_history():
    global conversation_history
    conversation_history = []

# Function to get responses from the selected LLM model
def {function_name}(prompt):
    global conversation_history
    conversation_history.append({{"role": "user", "content": prompt}})

    response = client.chat.completions.create(
        model='{model_name}',
        messages=[{{"role": "system", "content": "{system_instruction}"}}] + conversation_history,
        temperature=1,
        max_tokens=500,
        top_p=1
    )

    ai_message = response.choices[0].message.content
    conversation_history.append({{"role": "assistant", "content": ai_message}})

    return ai_message
"""

# OpenAI_Response function generates code for an OpenAI-based chatbot
def OpenAI_Response(system_instruction=None):
    if system_instruction is None:
        system_instruction = "You are a helpful, friendly, and concise chatbot designed to assist users by providing clear, accurate, and relevant information."
    
    return f"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# API key setup and OpenAI client initialization
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("API key for OpenAI is not set in the environment variables.")

client = OpenAI(api_key=openai_api_key)

# Function to reset chat history
conversation_history = []

def clear_conversation_history():
    global conversation_history
    conversation_history = []

# Function to get responses from OpenAI model
def get_openai_response(prompt):
    global conversation_history
    conversation_history.append({{"role": "user", "content": prompt}})

    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[{{"role": "system", "content": "{system_instruction}"}}] + conversation_history,
        temperature=1,
        max_tokens=500,
        top_p=1
    )

    ai_message = response.choices[0].message.content
    conversation_history.append({{"role": "assistant", "content": ai_message}})

    return ai_message
"""
