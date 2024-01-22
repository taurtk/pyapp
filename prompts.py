# step1 = 



step11 = """Here are some notes on a presentation we are preparing 
We think people believe the following now |
{user_input3} .After our talk we want them to believe |{user_input4}.
 The end objective of this pitch is |{user_input2}Based on the these
   notes does it appear we have a clear objective for our presentation.
"""


step12 = """"Here is the introduction of a pitch
 we are planning to make | {user_input} by {user_input1}  {user_input2} {user_input3} | Is this introduction clear, compelling and interesting ?"
"""


step21="Here are 3 parts of a presenation we are are working on  
We aim to solve this "problem' 
|1
The benefit we offer is |2
The reason to believe is | 3  Is the problem 
, benefit and reasons to bleieve clear ?"



step22="Earlier we shared three parts 
of a presentation. 
These are | We aim to solve this 
"problem' |1  
The benefit we offer is |2 
The reason to believe is | 3
We want plan to make this promise to people
|We want plan to make this promise to people
|5 and profits from 
 6 Is this promise clear and 
compelling ?

Here are they key elements of our
business pitch | PROBLEM -
WHAT is the problem and for whom   
1 PROMISE- In clear simple terms, 
what is the benefit you are offering       
2  
PROOF -3
PAYOFF - Dramatic Difference (how their life 
                              
  will be better/different)4 PAYOFF - Dramatic Difference 
(how their life will be better/different)
5
Based on this pitch is their clear evidence 
this company could makea profit ?"

step2 ="""

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




step3= """Earlier we shared three parts of a
 presentation. These are | We aim to solve this 
 "problem' |{user_input} 
 The benefit we offer is |{user_input2} 
   The reason to believe is | {user_input3} We want plan to 
     make this promise to people |We want plan to make this 
     promise to people |{user_input4}
       from products soldIs this promise clear and compelling ?"""

pitch_prompt= """We have been working on 
          pitch and need help with a script for the pitch 

            We have a completed pitch template 

    Questions in the template are normally proceeded by ##
    Questions asked are shown first our replies follow after a | symbol 

    Please write a script for a talk based on this content 
    Write the talk as a real talk without speaker notes Why is this pitch important to you? | {user_input1}##What is the goal of your pitch? |{user_input2} ##What does your audience believe before the pitch?         | {user_input3}##What should your audience  believe after the pitch?      (and Why) | {user_input4} ##Note: What happens in between is your pitch...  | ##In one line, what is your pitch? 
    {user_input5} ##Up to 3 supporting arguments Argument 1 | {user_input6}## Argument 2 | {user_input7}## Argument 3 |{user_input8}####Here is core content of  pitch##PROBLEM - WHAT is the problem and for whom         | {user_input9} ##PROMISE- In clear simple terms, what is the benefit you are offering         | {user_input10} ##PROOF - Why should we believe you can do this          |  {user_input11} ##PAYOFF - Dramatic Difference (how their life will be better/different) | {user_input12}##PROFIT (If applicable) - how will this product/service make a profit | {user_input13}##PASSION - Why are you excited about this | {user_input14}####What follows  is the content for the last slide of the presentation##Call to action (what after your pitch) -
    (1 Sentence)  [Try to include what they will be saying yes to in concrete terms] | {user_input15}##Why do this (up to 3 reasons)  Note: Include why do this Now Reason 1 | {user_input16}## Reason 2 | {user_input17}## Reason 23  {user_input18}##Your last line
    What do they need to remember /do |  
            | note |
            Please remove placeholders from the final pitch"""


# step3 ="""This is what we want people to do 
# at the end of this talk | 
# Please try our ecommerce site periods.co.in 
# This is why they should do this |it is free to use 
# and learn more about menstrual health and well-beingtry
#  to register your self and use our free periods & 
#  pregnancy tracking appGet suggestions based on it and 
#  discounts on products Can anyone understand why they 
#  should take this action ?"""