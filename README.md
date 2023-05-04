# OpenAI Q&A Program Using ChatGPT API-KEY

This is a simple Python program that uses the OpenAI API to generate responses to user questions.

## Installation

1. Clone the repository to your local machine.
2. Install the `Requirements` Python modules by running `pip install -r requirements.txt `.
3. Create a file called `config.py` in the same directory as the program.
4. In `config.py`, define your OpenAI API key as `API_KEY`.
5. Run the program using the command `python main.py`.

## Usage

1. When prompted, enter a question to generate a response.
2. The program will use the OpenAI API to generate a response based on the question.
3. The response will be displayed in the console.

To exit the program, simply type `exit` when prompted for a question.

## Notes

- This program uses the `text-davinci-003` model by default. You can change the model by modifying the `model_engine` variable in `main.py`.
- Your OpenAI API key should be kept secure. Do not share it with others or commit it to a public repository.
