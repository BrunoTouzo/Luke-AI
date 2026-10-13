# imports
import controller as c

# main  function
def main():

    # creating chatbot
    chatbot:c.Chatbot = c.Chatbot()
    talking = True

    while talking:
        prompt = input("You: ").lower().strip()

        if prompt.startswith('/'):

            if prompt in ['/save_history','/save_context','/save_context_history','/sh','/sch','/shc','/sc']:
                chatbot.save_context_history()

            elif prompt in ['/ch']:
                print('----'*20)
                print('Showing conversation history:')
                for items in chatbot.context.items():
                    print(f'{items[0]}: {items[1]}')
                print('----'*20)

            elif prompt in ['/bye','/exit','/end','/close','/e']:
                talking = False
                break

            else:
                pass
        else:
            response = chatbot.chatting(prompt)
            print(f'Chat: {response}')
    print('\n**exiting**\n')


# calling main
if __name__=="__main__":
    main()