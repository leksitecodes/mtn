from django.http import JsonResponse
from django.shortcuts import render
from .chatbot import bot

# View function to handle user messages and return bot responses
def get_response(request):
    # Get the user message from the GET request parameters
    user_text = request.GET.get('userMessage')
    
    # Get the bot's response by passing the user message to the bot's get_response method
    bot_response = str(bot.get_response(user_text))
    
    # Return the bot's response as a JSON response
    return JsonResponse({'response': bot_response})

def chat_page(request):
    return render(request, 'chat.html')