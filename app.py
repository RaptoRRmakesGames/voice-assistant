import speech_recognition
from gtts import gTTS
import pygame , os
pygame.mixer.init()

def get_voice_sentence():
        
    recognizer = speech_recognition.Recognizer()

    index = 1

    while True:
        
        try:
            
            with speech_recognition.Microphone(device_index=index) as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio)
                
                text = text.lower()
                
                return text
                
            
        except speech_recognition.UnknownValueError:
            
            recognizer = speech_recognition.Recognizer()
            continue
        
def speak_text(text):
    obj = gTTS(text, lang='en', slow=False)
    
    obj.save('temp_sound_file.mp3')
    
    sound = pygame.mixer.Sound('temp_sound_file.mp3')
    
    sound.play()
    
    os.remove('temp_sound_file.mp3')
    

while True:
    
    voice_message = get_voice_sentence()
    
    print(voice_message)
    
    speak_text(voice_message)


            
    
        
        