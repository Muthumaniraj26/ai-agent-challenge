Run Instructions
Follow these steps to set up and run the project:

#1 ----->Clone the Repository:
Clone your forked repository to your local machine.

git clone <your-repository-url>
cd <repository-name>

#2 ----->Set Up the Environment:
Create and activate a Python virtual environment.

For Windows
python -m venv venv
.\venv\Scripts\activate

For macOS/Linux
python3 -m venv venv
source venv/bin/activate

#3 ----->Install Dependencies:
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

#4 ----->Configure API Key:
Create a file named .env in the project's root directory and add your Groq API key:

GROQ_API_KEY="your_api_key_here"

#5 ------>Run the Agent and Verify:
First, run the agent to automatically generate the parser file. Then, run pytest to confirm that the generated parser is correct.

 Run the agent to create the parser
python agent.py --target icici

Run the test to verify the output
pytest

You should see 1 passed as the final output, confirming the success of the agent.
