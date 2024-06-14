from chatterbot import ChatBot  # Import the ChatBot class from the ChatterBot library
from chatterbot.trainers import ListTrainer  # Import the ListTrainer class from the ChatterBot library
from .training_lists import list_for_training, list_for_training2  # Import training data from custom modules

# Create an instance of ChatBot with the name 'mtnbot'
bot = ChatBot(
    "mtnbot",  # Name of the chatbot
    read_only=False,  # Allow the bot to be trained
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",  # Use the BestMatch logic adapter to find the best matching response
            "default_response": "I'm having a problem understanding that, sorry for the inconvenience. If you have any issue concerning our services please call us at 180 to speak with a customer service representative. Thank you",  # Default response if no good match is found
            "maximum_similarity": 0.8  # Set the threshold for response similarity
        }
    ],
     storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'  # URI for the SQLite database
)

# Create a ListTrainer instance for training the bot with a list of responses
list_trainer = ListTrainer(bot)

# Train the bot with the provided training data
list_trainer.train(list_for_training)
list_trainer.train(list_for_training2)