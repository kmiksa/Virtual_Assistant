import pyaudio
import wave
import speech_recognition as sr
from speak import say
from commands import Commander


running = True
name = None

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()


    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )


    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)


    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Commander()

def listen():
    play_audio("./audio/start_noti.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("./audio/end_noti.wav")

    answer = ""

    try:
        answer = r.recognize_google(audio)
    except:
        print("Couldn't understand")

    return answer

def initSpeech():
   global name
   if name is None:
       say("What is your name?")
       name = listen()
   else:
       command = listen()
       print("Your command: ")
       print(command)
       if command in ['quit', 'bye', 'close', 'goodbye', 'exit']:
            global running
            running = False
       cmd.discover(command, name)


   #say(command)


while running == True:
    initSpeech()
