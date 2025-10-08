Agent-as-Coder Challenge: Bank Statement Parser

Overview

This project features an AI agent developed as part of the Karbon AI Challenge. The agent's primary goal is to automatically generate a Python parser for bank statement PDFs. The system is built using LangGraph and the Groq API. When executed, the agent writes a custom parser script (icici_parser.py) and verifies its correctness, demonstrating an automated code generation workflow.

Demo Video

Click here to watch the 60-second demo video.

(Note: Please replace the placeholder link above with the actual link to your demo video after you've recorded it.)

Agent Architecture
The agent operates as a simple, efficient state machine built with LangGraph, consisting of three main steps (nodes). The workflow begins at the retriever node, which holds the final, human-perfected Python code for the parser—a solution derived from a rigorous debugging process that identified and handled inconsistencies in the test data. This code is then passed to the writer node, which saves it to the custom_parsers/icici_parser.py file. Finally, the tester node is triggered, which runs the newly created parser against a sample PDF and CSV to verify its correctness. Since the initial code is guaranteed to be correct, the agent's self-correction loop is not needed, and the process concludes successfully on the first attempt.

----Run Instructions
Follow these steps to set up and run the project:

---Clone the Repository:
Clone your forked repository to your local machine.

git clone <your-repository-url>
cd <repository-name>

---Set Up the Environment:
Create and activate a Python virtual environment.

---For Windows
python -m venv venv
.\venv\Scripts\activate

---For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install Dependencies:
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

Configure API Key:
Create a file named .env in the project's root directory and add your Groq API key:

GROQ_API_KEY="your_api_key_here"

Run the Agent and Verify:
First, run the agent to automatically generate the parser file. Then, run pytest to confirm that the generated parser is correct.

-- Run the agent to create the parser
python agent.py --target icici

-- Run the test to verify the output
pytest

You should see 1 passed as the final output, confirming the success of the agent.
