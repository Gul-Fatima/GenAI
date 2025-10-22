from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv #Dotenc is used to load environment variables from a .env file into the environment.

load_dotenv() # Load environment variables from .env file
model = ChatOpenAI(model = 'gpt-3.5') # Create an instance of the OpenAI LLM.

result = model.invoke("What is the capital of France?") # Invoke the LLM with a prompt.
print(result) # Print the result.
