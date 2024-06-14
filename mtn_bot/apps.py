# mtn_bot/apps.py
from django.apps import AppConfig

class MtnBotConfig(AppConfig):
    name = 'mtn_bot'

    def ready(self):
        from . import chatbot_init  # Import chatbot initialization logic here
