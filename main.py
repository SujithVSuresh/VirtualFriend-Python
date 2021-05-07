import pyttsx3
friend = pyttsx3.init()
speech = input("say something: ")
voices = friend.getProperty('voices')  #getting details of current voice
print(voices)
friend.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female
friend.say(speech)
friend.runAndWait()
