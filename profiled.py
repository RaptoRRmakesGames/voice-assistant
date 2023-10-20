import cProfile
from app import get_voice_sentence

cProfile.run('print(get_voice_sentence())')