# imports
import controller as c

def main():

    # creating chatbot
    chatbot:c.Chatbot = c.Chatbot()
    talking = True

    while talking:
        prompt = input("You: ").lower().strip()
        if prompt in ['/bye','/exit','/end','close']:
            talking = False
            break
        response = chatbot.chatting(prompt)
        print(f'Chat: {response}')
    print('\n**exiting**\n')

main()