# Install the dependency in the active environment with: python -m pip install ollama
from ollama import chat  # pyright: ignore[reportMissingImports]

prompt = input("Enter your prompt: ")
response = chat('llama3.2', messages=[
  {'role': 'user', 'content': prompt}
])
print(response)