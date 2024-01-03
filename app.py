from flask import Flask, render_template, request, Response
from prompts import step11,step12
app = Flask(__name__)
import openai
from flask import request
import time



openai.api_key = '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'

def prompts_for_analysis():
    prompts = [step1
           ]
    return prompts

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/step1')
def step1():
    return render_template('step1.html')

@app.route('/step2')
def step2():
    return render_template('step2.html')

@app.route('/step3')
def step3():
    return render_template('step3.html')

@app.route('/pitch')
def pitch():
    return render_template('pitch.html')

@app.route('/more')
def more():
    return render_template('more.html')


user_inputs = {
    'step1': {'input1': '', 'input2': '', 'input3': '', 'input4': ''},
    'step2': {'input5': '', 'input6': '', 'input7': '', 'input8': ''},
    'step3': {'input9': '', 'input10': '', 'input11': '', 'input12': ''},
    'step4': {'input13': '', 'input14': '', 'input15': '', 'input16': ''},
}


@app.route('/generate_feedback', methods=['POST'])
def generate_feedback():
    # Define a list to store user inputs
    user_inputs = [request.form[f'user_input{i}'] for i in range(1, 5)]
    # try:
   # Code that might raise a ZeroDivisionError    
    pitch_input1 =user_input = user_inputs[0]
    pitch_input2 =user_input2 = user_inputs[1]
    pitch_input3 =user_input3 = user_inputs[2]
    pitch_input4 =user_input4 = user_inputs[3]
    print('i am here',pitch_input1)

    step11 = f"""Here are some notes on a presentation we are preparing. We think people believe the following now:
    |{user_input3} After our talk we want them to believe
    |{user_input4}
    The end objective of this pitch is
    |{user_input2} Based on these notes does it appear we have a clear objective for our presentation"""
        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step11}
            ],
                max_tokens=150
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        print(feedback)

        
    return render_template('index.html', user_inputs=user_inputs, feedback=feedback)



@app.route('/generate_feedback1', methods=['POST'])
def generate_feedback1():
    # Define a list to store user inputs
    user_inputs = [request.form[f'user_input{i}'] for i in range(1, 5)]
    # try:
   # Code that might raise a ZeroDivisionError    
    pitch_input5 = user_input = user_inputs[0]
    pitch_input6 =user_input2 = user_inputs[1]
    pitch_input7 = user_input3 = user_inputs[2]
    pitch_input8 =user_input4 = user_inputs[3]

    step12 = f"""Here is the introduction of a pitch
    we are planning to make | {user_input} by {user_input2}  {user_input3} {user_input4} | Is this introduction clear, compelling and interesting ?
    """
        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step12}
            ],
                max_tokens=150
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        print(feedback)


        
    return render_template('step1.html', user_inputs=user_inputs, feedback=feedback)


@app.route('/generate_feedback2', methods=['POST'])
def generate_feedback2():
    # Define a list to store user inputs
    user_inputs = [request.form[f'user_input{i}'] for i in range(1, 6)]
    # try:
   # Code that might raise a ZeroDivisionError    
    pitch_input8 =user_input = user_inputs[0]
    pitch_input9 =user_input2 = user_inputs[1]
    pitch_input10 =user_input3 = user_inputs[2]
    pitch_input11 =user_input4 = user_inputs[3]
    pitch_input12 =user_input5 = user_inputs[4]

    
    step2 =f"""

 Here are they key elements of our business pitch
   | PROBLEM - WHAT is the problem and for whom    
    {user_input} PROMISE- In clear simple terms,
   what is the benefit you are offering        
   {user_input2} PROOF 
   - Why should we believe you can do this         
     {user_input3} PAYOFF
         - Dramatic Difference (how their life will be
           better/different){user_input4}PAYOFF - Dramatic Difference 
               (how their life will be better/different)
               {user_input5}
               Based on this pitch is their clear
                 evidence this company could makea profit ?"""

        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step2}
            ],
                max_tokens=150
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        print(feedback)

        
    return render_template('step2.html', user_inputs=user_inputs, feedback=feedback)


    
@app.route('/generate_feedback3', methods=['POST'])
def generate_feedback3():
    # Define a list to store user inputs
    user_inputs = [request.form[f'user_input{i}'] for i in range(1, 3)]
    # try:
   # Code that might raise a ZeroDivisionError    
    pitch_input13 =user_input = user_inputs[0]
    pitch_input14 = user_input2 = user_inputs[1]
    

    step3= f"""This is what we want people to do at the end of this talk
      | {user_input}
      This is why they should do this 
      |{user_input2}
        Can anyone understand why they should take this action ?"""
        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step3}
            ],
                max_tokens=150
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        print(feedback)

        
    return render_template('step3.html', user_inputs=user_inputs, feedback=feedback)


@app.route('/generate_pitch', methods=['POST'])
def generate_pitch():
    # Define a list to store user inputs
#     user_inputs = [request.form[f'user_input{i}'] for i in range(1, 3)]
#     # try:
#    # Code that might raise a ZeroDivisionError    
#     user_input = user_inputs[0]
#     user_input2 = user_inputs[1]
    print('i amhere ',pitch_input1)
    pitch_prompt= f"""We have been working on 
          pitch and need help with a script for the pitch 

            We have a completed pitch template 

    Questions in the template are normally proceeded by ##
    Questions asked are shown first our replies follow after a | symbol 

    Please write a script for a talk based on this content 
    Write the talk as a real talk without speaker notes Why is this pitch important to you? | {pitch_input1}##What is the goal of your pitch? |{pitch_input2} ##What does your audience believe before the pitch?         | {pitch_input3}##What should your audience  believe after the pitch?      (and Why) | {pitch_input4} ##Note: What happens in between is your pitch...  | ##In one line, what is your pitch? 
    {pitch_input5} ##Up to 3 supporting arguments Argument 1 | {pitch_input6}## Argument 2 | {pitch_input7}## Argument 3 |{pitch_input8}####Here is core content of  pitch##PROBLEM - WHAT is the problem and for whom         | {pitch_input9} ##PROMISE- In clear simple terms, what is the benefit you are offering         | {pitch_input10} ##PROOF - Why should we believe you can do this          |  {pitch_input11} ##PAYOFF - Dramatic Difference (how their life will be better/different) | {pitch_input12}##PROFIT (If applicable) - how will this product/service make a profit | {pitch_input13}##PASSION - Why are you excited about this | {pitch_input14}####What follows  is the content for the last slide of the presentation##Call to action (what after your pitch) -
    (1 Sentence)  [Try to include what they will be saying yes to in concrete terms] | {pitch_input15}##Why do this (up to 3 reasons)  Note: Include why do this Now Reason | {pitch_input16}##Your last line
    What do they need to remember /do |  
            | note |
            Please remove placeholders from the final pitch"""
        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": pitch_prompt}
            ],
                max_tokens=150
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        # print(feedback)
        print('i amhere ',pitch_input1)

        
    return render_template('pitch.html', user_inputs=pitch_input1, feedback=feedback)





# @app.route('/generate_feedback1', methods=['POST'])
# def generate_feedback1():
#     # Define a list to store user inputs
   
#         user_inputs = [request.form[f'user_input{i}'] for i in range(1, 5)]
#     # try:
#    # Code that might raise a ZeroDivisionError
        
        
#         user_input = user_inputs[0]
#         user_input2 = user_inputs[1]
#         user_input3 = user_inputs[2]
#         user_input4 = user_inputs[3]


#         step1 = f"""Here are some notes on a presentation we are preparing. We think people believe the following now:
#     |{user_input3} After our talk we want them to believe
#     |{user_input4}
#     The end objective of this pitch is
#     |{user_input2} Based on these notes does it appear we have a clear objective for our presentation"""
        

#     # # Loop through prompts and get responses from ChatGPT
#         for prompt in prompts_for_analysis():
#             # Combine user input and current prompt
#             # combined_prompt = f"{step1}\n\nUser's Input:\n{user_input3,user_input4,user_input2}"

#             # print(combined_prompt)
#             # Call OpenAI API
#             response = openai.ChatCompletion.create(
#                 model = "gpt-3.5-turbo",  # You can choose a different engine
#                 messages=[
#                 {"role": "user", "content": step1}
#             ],
#                 max_tokens=150
#             )
        
#         print(response)
#             # Append the response to the list
#         feedback =  response.choices[0].message.content
#         print(feedback)


    
        
#         # Call GPT-3 model to generate feedback (replace 'your_openai_api_key')
#         # You can use the OpenAI GPT-3 Python library to interact with the API
#         # For example, you can use OpenAI's `openai.Completion.create` method
#         # to generate feedback based on user inputs
#         # feedback = openai.Completion.create(model="text-davinci-002", prompt=user_inputs, ...)
#         #  = "Generated feedback from GPT-3 goes here."
        
#     return render_template('index.html', user_inputs=user_inputs, feedback=feedback)


@app.route('/progress')
def progress():
 def generate():
     x = 0
     while x <= 100:
         yield f"data:{x}\n\n"
         x += 10
         time.sleep(1)
 return Response(generate(), mimetype='text/event-stream')

@app.route('/greet', methods=['POST'])
def greet():
    if request.method == 'POST':
        user_name = request.form['username']
        greeting = f"Hello, {user_name}! Welcome to the Flask App."
        return render_template('greet.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
