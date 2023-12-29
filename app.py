from flask import Flask, render_template, request
from prompts import step1
app = Flask(__name__)
import openai
from flask import request


openai.api_key = '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'

def prompts_for_analysis():
    prompts = [step1
           ]
    return prompts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_feedback', methods=['POST'])
def generate_feedback():
    # Define a list to store user inputs
    user_inputs = [request.form[f'user_input{i}'] for i in range(1, 5)]
    print(len(user_inputs))
    user_input = user_inputs[0]
    user_input2 = user_inputs[1]
    user_input3 = user_inputs[2]
    user_input4 = user_inputs[3]

    step1 = f"""Here are some notes on a presentation we are preparing. We think people believe the following now:
    |{user_input3} After our talk we want them to believe
    |{user_input4}
    The end objective of this pitch is
    |{user_input2} Based on these notes does it appear we have a clear objective for our presentation"""
   
    print(step1)
    generated_feedback = []

    # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
        # Combine user input and current prompt
        # combined_prompt = f"{prompt}\n\nUser's Input:\n{user_inputs}"

        # print(combined_prompt)
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",  # You can choose a different engine
            messages=[
            {"role": "user", "content": step1}
        ],
            max_tokens=150
        )
    
    print(response)
        # Append the response to the list
    feedback =  response.choices[0].message.content
    print(feedback)
    
    # Call GPT-3 model to generate feedback (replace 'your_openai_api_key')
    # You can use the OpenAI GPT-3 Python library to interact with the API
    # For example, you can use OpenAI's `openai.Completion.create` method
    # to generate feedback based on user inputs
    # feedback = openai.Completion.create(model="text-davinci-002", prompt=user_inputs, ...)
    #  = "Generated feedback from GPT-3 goes here."
    
    return render_template('index.html', user_inputs=user_inputs, feedback=feedback)


@app.route('/greet', methods=['POST'])
def greet():
    if request.method == 'POST':
        user_name = request.form['username']
        greeting = f"Hello, {user_name}! Welcome to the Flask App."
        return render_template('greet.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
