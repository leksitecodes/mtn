# from django.http import JsonResponse
# from django.shortcuts import render
# from .chatbot import bot

# # View function to handle user messages and return bot responses
# def get_response(request):
#     # Get the user message from the GET request parameters
#     user_text = request.GET.get('userMessage')
    
#     # Get the bot's response by passing the user message to the bot's get_response method
#     bot_response = str(bot.get_response(user_text))
    
#     # Return the bot's response as a JSON response
#     return JsonResponse({'response': bot_response})

# def chat_page(request):
#     return render(request, 'chat.html')

# from django.http import JsonResponse
# from django.shortcuts import render

# import logging

# # Configure logging
# logger = logging.getLogger(__name__)

# # View function to handle user messages and return bot responses
# def get_response(request):
#     from .chatbot import bot
#     user_text = request.GET.get('userMessage')
#     logger.debug("Received user message: %s", user_text)
    
#     bot_response = str(bot.get_response(user_text))
#     logger.debug("Bot response: %s", bot_response)
    
#     return JsonResponse({'response': bot_response})

# def chat_page(request):
#     logger.debug("Rendering chat page")
#     return render(request, 'chat.html')

from django.http import JsonResponse
from django.shortcuts import render

def get_response(request):
    # Log the incoming request
    print("Received request:", request.GET)

    # Return a static response for debugging purposes
    return JsonResponse({'response': "This is a static response for debugging."})

def chat_page(request):
    return render(request, 'chat.html')
