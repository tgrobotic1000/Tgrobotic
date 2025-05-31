import os

class Config:
    API_ID = int(os.getenv("25165349", "0"))
    API_HASH = os.getenv("d5ea503a893548d7d492f91fc72e8ce9", "")
    BOT_TOKEN = os.getenv("7729291712:AAEyuIgE7VLStp1tpZrKiEVrTFFjUujZJks", "")
    CHID = os.getenv("-1002662027422", "")
    SUDO = int(os.getenv("7439650239", "0"))
    MONGO_URI = os.getenv("mongodb+srv://tgrobotic:nRUEU81Zc3r5gMxK@cluster0.omkktyb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
