from openai import OpenAI

client = OpenAI(
    api_key = 'sk-None-ogsCfim1X4ztYGGYI0nMT3BlbkFJsQJ8Dk0TnqWxlyKEGV9X',
)


command='''
[7/12, 21:58] shivangi srivastva: are you saying you want to be with your beloved preet?
[7/12, 21:58] Rashmi 🥺🫶: Hnn wahi pe shaadi kr lungi sabke samne😂😂
[7/12, 21:58] Rashmi 🥺🫶: Aree meko nhi mila woh teacher...suna hai accha hai
[7/12, 22:16] shivangi srivastva: haa hes very good
[7/12, 22:16] shivangi srivastva: I'LL BE CHEERING
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person name Shivangi who speaks Hindi as well as English. She is from India and is a coder. You analyze chat history and respond like Shivangi"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message)