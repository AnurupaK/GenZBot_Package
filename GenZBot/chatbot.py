import os, sys
import shutil
import subprocess, platform
from .utils_list.AIModels import response
from .utils_list.backend import flask_app
from .utils_list.Images_list import *

class ChatBot:
    # Initialize the ChatBot class with default parameters and set up necessary attributes
    def __init__(self, llm='gemini', api_key=None, template_design='Plain', BotBehaviour=None, BotName="AI-BOT"):
        self.llm = llm  # Language Model (LLM) to use (e.g., gemini, openai)
        self.api_key = api_key  # API key for accessing the LLM
        self.template_design = template_design  # Template design to use for the front end (e.g., Plain, Galaxy)
        self.BotBehaviour = BotBehaviour  # Bot's behavior or instructions for the LLM
        self.BotName = BotName  # The name of the bot
        self.base_dir = 'Chatbot_Project'  # Directory where the project will be created

    # Create the project structure and files
    def CreateProject(self):
        # Check if an API key is provided, raise error if not
        if not self.api_key:
            raise ValueError("API key is required to create the project.")
        
        # Output basic information about the project being created
        print(f"Creating project with LLM: {self.llm}, Template: {self.template_design}")
        
        # Create the folder structure and necessary files
        self._create_structure()
        
        # Customize the files with the appropriate content
        self._customize_files()
        
        # Print success message
        print(f"Project created and saved as {self.base_dir}")
    
    # Create the folder structure and files for the project
    def _create_structure(self):
        # Based on the selected LLM, set up the corresponding response model and flask backend code
        if self.llm.lower() == 'gemini':
            ai_response = response.Gemini_Response(system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_gemini
        elif self.llm.lower() == 'openai':
            ai_response = response.OpenAI_Response(system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_openai
        elif self.llm.lower() == 'llama':
            ai_response = response.Groq_Response(model=self.llm.lower(), system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_llama
        elif self.llm.lower() == 'gemma':
            ai_response = response.Groq_Response(model=self.llm.lower(), system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_gemma
        elif self.llm.lower() == 'mixtral':
            ai_response = response.Groq_Response(model=self.llm.lower(), system_instruction=self.BotBehaviour)
            flask_code = flask_app.backendCode_mixtral
        else:
            raise ValueError(f"Invalid model '{self.llm.lower()}'. Valid options are: 'openai','gemini','llama', 'gemma', 'mixtral'.")
        
        # Select the appropriate template design (Plain or Galaxy)
        if self.template_design.lower() == 'plain':
            from .utils_list.templates_list.design1 import index, style, script
        elif self.template_design.lower() == 'galaxy':
            from .utils_list.templates_list.design2 import index, style, script
        else:
            raise ValueError("Invalid template designs. Valid options are Plain, Galaxy")
        
        # Folder structure for the project
        folders = [
                f"{self.base_dir}/AI_Service",
                f"{self.base_dir}/Backend",
                f"{self.base_dir}/Frontend/static",
                f"{self.base_dir}/Frontend/templates",
            ]
        
        # Files to be created and their content
        files = {
                f"{self.base_dir}/AI_Service/AIResponse.py": ai_response,
                f"{self.base_dir}/Backend/app.py": flask_code(),
                f"{self.base_dir}/Frontend/static/style.css": style.getStyle(),
                f"{self.base_dir}/Frontend/static/script.js": script.getScript(),
                f"{self.base_dir}/Frontend/templates/index.html": index.getHtml(self.BotName),
                f"{self.base_dir}/.env": "",  # API key will be added later
                f"{self.base_dir}/requirements.txt": "",  # Dependencies will be added later
            }
        
        # If the "Galaxy" template is selected, copy the related image
        if self.template_design.lower() == 'galaxy':
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
            source = os.path.join(project_root, 'GenZBot', 'utils_list', 'Images_list', 'galaxy_img.png')
            destination = os.path.join(self.base_dir, 'Frontend', 'static', 'galaxy_img.png')

            # Check if the image exists, then copy it to the appropriate directory
            if os.path.exists(source):
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                shutil.copy(source, destination)
            else:
                raise ValueError('Internal Error')
            
        # Create the project folders if they don't exist
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        
        # Write the content to the respective files
        for file_path, content in files.items():
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(content)
    
    # Customize the files with the appropriate API key and dependencies based on the selected LLM
    def _customize_files(self):
        if self.llm.lower() == "gemini":
            # Set the environment variables and dependencies for Gemini model
            env_file = os.path.join(self.base_dir, ".env")
            with open(env_file, "w", encoding='utf-8') as f:
                f.write(f'GOOGLE_API_KEY="{self.api_key}"\n')
            print("Customized .env file with the API key.")
            
            requirement_file = os.path.join(self.base_dir, "requirements.txt")
            with open(requirement_file, "w", encoding='utf-8') as f:
                f.write("flask\npython-dotenv\ngoogle-generativeai\ngunicorn==20.1.0")
            print("Customized requirements.txt file with required packages.")
        
        elif self.llm.lower() == "openai":
            # Set the environment variables and dependencies for OpenAI model
            env_file = os.path.join(self.base_dir, ".env")
            with open(env_file, "w", encoding='utf-8') as f:
                f.write(f'OPENAI_API_KEY="{self.api_key}"\n')
            print("Customized .env file with the API key.")
            
            requirement_file = os.path.join(self.base_dir, "requirements.txt")
            with open(requirement_file, "w", encoding='utf-8') as f:
                f.write("flask\npython-dotenv\nopenai\ngunicorn==20.1.0")
            print("Customized requirements.txt file with required packages.")
        
        elif self.llm.lower() in ["llama", "gemma", "mixtral"]:
            # Set the environment variables and dependencies for other models (llama, gemma, mixtral)
            if self.llm.lower() == "llama":
                key_name = 'LLAMA_API_KEY'
            elif self.llm.lower() == "gemma":
                key_name = 'GEMMA_API_KEY'
            elif self.llm.lower() == "mixtral":
                key_name = 'MIXTRAL_API_KEY'
            
            env_file = os.path.join(self.base_dir, ".env")
            with open(env_file, "w", encoding='utf-8') as f:
                f.write(f'{key_name}="{self.api_key}"\n')
            print("Customized .env file with the API key.")
            
            requirement_file = os.path.join(self.base_dir, "requirements.txt")
            with open(requirement_file, "w", encoding='utf-8') as f:
                f.write("flask\npython-dotenv\ngroq\ngunicorn==20.1.0")
            print("Customized requirements.txt file with required packages.")
    
    # Set up the virtual environment, install dependencies, and run the app
    def run(self):
        # Create a virtual environment for the project
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", os.path.join(self.base_dir, "venv")])

        # Activate the virtual environment based on the operating system (Windows or non-Windows)
        activate_script = os.path.join(self.base_dir, "venv", "Scripts", "activate") if platform.system() == 'Windows' else os.path.join(self.base_dir, "venv", "bin", "activate")

        print("Activating the virtual environment...")
        activate_command = f"source {activate_script}" if platform.system() != 'Windows' else f"{activate_script}"

        if platform.system() != 'Windows':
            subprocess.check_call(activate_command, shell=True)  
        else:
            subprocess.check_call(f"{activate_script}", shell=True)  

        # Install the dependencies from the requirements.txt file
        print("Installing dependencies...")
        subprocess.check_call([os.path.join(self.base_dir, "venv", "Scripts", "pip" if platform.system() == 'Windows' else "pip"), "install", "-r", os.path.join(self.base_dir, "requirements.txt")])

        # Run the Flask application
        print("Running the app...")
        subprocess.check_call([os.path.join(self.base_dir, "venv", "Scripts", "python" if platform.system() == 'Windows' else "python"), os.path.join(self.base_dir, "Backend", "app.py")])

        # Output success message
        print("Bot is running successfully!")
