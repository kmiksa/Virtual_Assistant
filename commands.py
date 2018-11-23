from speak import say
import os
import requests
from get_answer import Fetcher

class Commander():
    def __init__(self):
        self.confirm = ['yes', 'yeah', 'sure', 'yup', 'confirm']
        self.cancel = ['no', 'negative', 'nope', "don't", 'wait', 'cancel']



    def discover(self, text, name):
        if "what" in text and "your name" in text:
            self.respond("My name is python commander. How are you?" + name)
        else:
            #"search" in text and "google" in text:
            self.respond("Okay, here are some results" + name)
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)
        #elif "math" in text or "calculator" in text:
        #    self.respond("Cool! what do you want to count?")


    def respond(self, response):
        print(response)
        say(response)


