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
def welcome():
    return render_template('welcome.html')

@app.route('/index')
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
    'step2': {'input1': '', 'input2': '', 'input3': '', 'input4': ''},
    'step3': {'input1': '', 'input2': '', 'input3': '', 'input4': '','input5':'','input6':'','input7':''},
    'step4': {'input1': '', 'input2': ''},
}


@app.route('/generate_feedback', methods=['POST'])
def generate_feedback():
    # Define a list to store user inputs
    user_inputs.setdefault('step1', {})

# Update 'step1' with user inputs
    for i in range(1, 5):
        input_key = f'input{i}'
        user_inputs['step1'][input_key] = request.form[f'user_input{i}']
    # try:
#    # Code that might raise a ZeroDivisionError    
#     pitch_input1 =user_input = user_inputs[0]
#     pitch_input2 =user_input2 = user_inputs[1]
#     pitch_input3 =user_input3 = user_inputs[2]
#     pitch_input4 =user_input4 = user_inputs[3]
    # print('i am here',pitch_input1)

    
    step11 = f"""Here are some notes on a presentation we are preparing. We think people believe the following now
    |{user_inputs['step1']['input3']} After our talk we want them to believe
    |{user_inputs['step1']['input4']}
    The end objective of this pitch is
    |{user_inputs['step1']['input2']} Based on these notes does it appear we have a clear objective for our presentation?"""
        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step11}
            ],
                
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        print(feedback)

        
    return render_template('index.html', user_inputs=user_inputs, feedback=feedback)



@app.route('/generate_feedback1', methods=['POST'])
def generate_feedback1():
    # Define a list to store user inputs
    user_inputs.setdefault('step2', {})

# Update 'step1' with user inputs
    for i in range(1, 5):
        input_key = f'input{i}'
        user_inputs['step2'][input_key] = request.form[f'user_input{i}']
    # try:
   # Code that might raise a ZeroDivisionError    
    # pitch_input5 = user_input = user_inputs[0]
    # pitch_input6 =user_input2 = user_inputs[1]
    # pitch_input7 = user_input3 = user_inputs[2]
    # pitch_input8 =user_input4 = user_inputs[3]

    step12 = f"""Here is the introduction of a pitch
    we are planning to make | {user_inputs['step2']['input1']} by {user_inputs['step2']['input2']}  {user_inputs['step2']['input3']} {user_inputs['step2']['input4']} | Is this introduction clear, compelling and interesting ?
    """
        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step12}
            ],
                
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        print(feedback)


        
    return render_template('step1.html', user_inputs=user_inputs, feedback=feedback)


@app.route('/generate_feedback2', methods=['POST'])
def generate_feedback2():
    # Define a list to store user inputs
    for i in range(1, 8):
        input_key = f'input{i}'
        user_inputs['step3'][input_key] = request.form[f'user_input{i}']
    # try:
   # Code that might raise a ZeroDivisionError    
    # pitch_input8 =user_input = user_inputs[0]
    # pitch_input9 =user_input2 = user_inputs[1]
    # pitch_input10 =user_input3 = user_inputs[2]
    # pitch_input11 =user_input4 = user_inputs[3]
    # pitch_input12 =user_input5 = user_inputs[4]

    
   

    step21=f"""Here are 3 parts of a presenation we are are working on  
We aim to solve this "problem' 
|{user_inputs['step3']['input1']}
The benefit we offer is |
|{user_inputs['step3']['input2']}
The reason to believe is | 
|{user_inputs['step3']['input3']} Is the problem 
, benefit and reasons to bleieve clear ?"""

        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step21}
            ],
                
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        print(feedback)

   
    step22=f"""Earlier we shared three parts 
of a presentation. 
These are | We aim to solve this 
"problem' |{user_inputs['step3']['input1']}
The benefit we offer is |{user_inputs['step3']['input2']}
The reason to believe is | {user_inputs['step3']['input3']}
We want plan to make this promise to people
|We want plan to make this promise to people
|{user_inputs['step3']['input5']} and profits from 
 {user_inputs['step3']['input6']} Is this promise clear and 
compelling ?

Here are they key elements of our
business pitch | PROBLEM -
WHAT is the problem and for whom   
{user_inputs['step3']['input1']} PROMISE- In clear simple terms, 
what is the benefit you are offering       
{user_inputs['step3']['input2']} 
PROOF -3
PAYOFF - Dramatic Difference (how their life 
                              
  will be better/different)4 PAYOFF - Dramatic Difference 
(how their life will be better/different)
{user_inputs['step3']['input5']}
Based on this pitch is their clear evidence 
this company could makea profit ?"""
    
     # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step22}
            ],
                
            )
            # Append the response to the list
        feedback1 =  response.choices[0].message.content
        print(feedback1)


        
    return render_template('step2.html', user_inputs=user_inputs, feedback=feedback+'\n \n  Feedback 2:'+feedback1)


    
@app.route('/generate_feedback3', methods=['POST'])
def generate_feedback3():
    # Define a list to store user inputs
    for i in range(1, 3):
        input_key = f'input{i}'
        user_inputs['step4'][input_key] = request.form[f'user_input{i}']
    # try:
   # Code that might raise a ZeroDivisionError    
    # pitch_input13 =user_input = user_inputs[0]
    # pitch_input14 = user_input2 = user_inputs[1]
    

    step3= f"""This is what we want people to do at the end of this talk
      | {user_inputs['step4']['input1']}
      This is why they should do this 
      |{user_inputs['step4']['input2']}
        Can anyone understand why they should take this action ?"""
        # # Loop through prompts and get responses from ChatGPT
    for prompt in prompts_for_analysis():
            # Call OpenAI API
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",  # You can choose a different engine
                messages=[
                {"role": "user", "content": step3}
            ],
                
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
    # print('i amhere ',pitch_input1)
    pitch_prompt= f"""We have been working on 
          pitch and need help with a script for the pitch 

            We have a completed pitch template 

    Questions in the template are normally proceeded by ##
    Questions asked are shown first our replies follow after a | symbol 

    Please write a script for a talk based on this content 
    Write the talk as a real talk without speaker notes Why is this pitch important to you? | {user_inputs['step1']['input1']}##What is the goal of your pitch? |{user_inputs['step1']['input2']} ##What does your audience believe before the pitch?         | {user_inputs['step1']['input3']}##What should your audience  believe after the pitch?      (and Why) | {user_inputs['step1']['input4']} ##Note: What happens in between is your pitch...  | ##In one line, what is your pitch? 
    {user_inputs['step2']['input1']} ##Up to 3 supporting arguments Argument 1 |{user_inputs['step2']['input2']}## Argument 2 | {user_inputs['step2']['input3']}## Argument 3 |{user_inputs['step2']['input4']}####Here is core content of  pitch##PROBLEM - WHAT is the problem and for whom         | {user_inputs['step3']['input1']}  ##PROOF - Why should we believe you can do this          |  {user_inputs['step3']['input2']} ##PAYOFF - Dramatic Difference (how their life will be better/different) | {user_inputs['step3']['input3']}##PROFIT (If applicable) - how will this product/service make a profit | {user_inputs['step3']['input4']}##PASSION - Why are you excited about this |{user_inputs['step3']['input5']}####What follows  is the content for the last slide of the presentation##Call to action (what after your pitch) -
    (1 Sentence)  [Try to include what they will be saying yes to in concrete terms] | {user_inputs['step4']['input1']}##Why do this (up to 3 reasons)  Note: Include why do this Now Reason | {user_inputs['step4']['input2']}##Your last line
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
                
            )
            # Append the response to the list
        feedback =  response.choices[0].message.content
        # print(feedback)
        # print('i amhere ',pitch_input1)

        
    return render_template('pitch.html', user_inputs=user_inputs, feedback=feedback)





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
#                 
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
