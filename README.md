A simple chat agent using OpenRouter API.

Note:<br>
This project has been tested with Python 3.15<br>
Dependencies required can be found in the file "requirements.txt"<br>
Rename the file ".env.example" to ".env" and fill in OPENROUTER_API_KEY with your actual api key<br>
You may change the AI model with a different one that's available in OpenRouter by changing the value of OPENROUTER_MODEL

This script uses the OpenRouter API to interact directly with an AI model hosted on OpenRouter. This current version of the script remembers your previously sent messages, similar to how a typical chat session with an AI agent usually goes.