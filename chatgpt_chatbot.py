from openai import OpenAI
client = OpenAI(api_key="***") #Use your personal key here
# Or alternatively create an activate OpenAI Environment and add your personal API key in the .env file

assistant_type = input("What type of assistant would you like: ")
gpt_assistant_type = "Hi ChatGPT, You are a "+assistant_type
print("ChatGPT: Hi, I'm ChatGPT. I'm your ", assistant_type)

conversation = [{"role":"system", "content": gpt_assistant_type}]

chat_completion = client.chat.completions.create(model =  "gpt-3.5-turbo", messages = conversation)
reply = chat_completion["choices"][0]["message"]["content"]
conversation.append({"role": "assistant", "content": reply})

#  shown here is OpenAI response object
#     <OpenAIObject chat.completion id=chatcmpl-7UkgnSDzlevZxiy0YjZcLYdUMz5yZ at 0x118e394f0> JSON: {
#   "id": "chatcmpl-7UkgnSDzlevZxiy0YjZcLYdUMz5yZ",
#   "object": "chat.completion",
#   "created": 1687563669,
#   "model": "gpt-3.5-turbo-0301",
#   "choices": [
#     {
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": "The reply from the model"
#       },
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 39,
#     "completion_tokens": 3,
#     "total_tokens": 42
#   }
# }
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit", "end chat"]:
            break

        else:
            conversation.append(
             {"role": "user", "content": user_input},
            )
            chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo", messages = conversation
            )
        reply = chat_completion["choices"][0]["message"]["content"]
        print("ChatGPT: ", reply)
        conversation.append({"role": "assistant", "content": reply})

