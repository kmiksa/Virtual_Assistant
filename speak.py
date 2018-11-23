import pyttsx3

def say(text):
    engine = pyttsx3.init()
    #change the voice
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
    engine.say(text)
    engine.runAndWait()
