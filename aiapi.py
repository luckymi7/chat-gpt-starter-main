import openai
import config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY



def generateChatResponse(Prpmpt):
 messages = []
 messages.append({"role": "system", " content": "Ypu are a helpful assistant."})

 question = {}
 question['role'] = 'user'
 question['content'] = prompt
 messages.append(question)


 response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)

 try:
  answer = response['choices'][0]['message']['content']
 except:
  answer = 'Oopps you beat the AI, try a different question ,if the problem persists, come back later.'

  return answer