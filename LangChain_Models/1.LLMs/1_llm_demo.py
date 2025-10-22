from langchain_openai import OpenAI 
from dotenv import load_dotenv #Dotenc is used to load environment variables from a .env file into the environment.

load_dotenv() # Load environment variables from .env file
llm = OpenAI(model = 'gpt-3.5') # Create an instance of the OpenAI LLM.

result = llm.invoke("What is the capital of France?") # Invoke the LLM with a prompt.
print(result) # Print the result.
