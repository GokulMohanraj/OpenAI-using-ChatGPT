# Import the openai module and the config module that contains the API key
import openai
import config

# Retrieve the API key from the config module
Api_key = config.API_KEY

# Set the API key for the openai module
openai.api_key = Api_key

# Define the OpenAI model to use
model_engine = "text-davinci-003"

# Start a loop that will run until the user types 'exit'
while True:

    # Prompt the user to enter a question
    question = input('\nAsk your question : ')

    # If the user enters an empty string, prompt them to enter something
    if question == '':
        print('please enter something to search..')

    # If the user enters a question, generate a response
    else:
        # If the user types 'exit', end the loop
        if question != 'exit':
            # Generate a response using the OpenAI API
            responce = openai.Completion.create(
                prompt = question,
                model = model_engine,
                max_tokens = 1000,
                n = 1
            )

            # Print the response
            for result in responce.choices:
                print(result.text)

        # If the user types 'exit', end the loop
        else:
            print('Thankyou....')
            break
