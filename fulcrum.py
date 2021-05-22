#iMPoRTaNT NoTe - install PyAudio by - pipwin install PyAudio. To install pipwin - pip install pipwin 
import pyttsx3
import speech_recognition as sr
# import wikipedia as wiki - this wiki was not giving accurate results but cant uninstall it as pywhatkit is dependent on it for info() function
from mediawiki import MediaWiki as wiki
import pywhatkit #pywhatkit is one of the most functional packages I've used till now it can send whatsapp mssgs, text to handwriting and much more however whenever we import it it sends its developer's message i had to remove it coz of aesthetics. The message is - 
#Hello from the creator of pywhatkit, Ankit Raj Mahapatra.\nKindly do report bugs if any. 
#What's new: 1. Removed selenium dependent functions 2. Added pywhatkit.text_to_handwriting() which will convert text to handwritten characters. 3. Added pywhatkit.image_to_ascii_art() which will convert image to ascii art.
import webbrowser
import datetime

engine=pyttsx3.init('sapi5') #for windows from MS you may use nsss for mac os X
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''  Function to give the speech output '''
    engine.say(audio)
    print(audio+"\n")
    engine.runAndWait()

def activate():
    '''Activates the assitant with hotword ok/okay/hey/hello fulcrum --- this fn is not working for now !'''
    with sr.Microphone() as source:
        audio = sr.Recognizer().listen(source)
        try:
            hotword=sr.Recognizer().recognize_google(audio, language="en-in")
            wakeUp=""
            for wrd in hotword:
                wakeUp+=str(wrd).lower()
            if ((("fulcrum" in wakeUp) or ("crum" in wakeUp) or ("kram" in wakeUp)or ("welcome" in wakeUp) or ("falcon" in wakeUp) or ("khan" in wakeUp) or ("comm" in wakeUp)or ("cream" in wakeUp) or ("chrome" in wakeUp) or ("phal" in wakeUp)) and (("hay" in wakeUp) or ("ok" in wakeUp) or ("hey" in wakeUp) or ("okay" in wakeUp) or "hello" in wakeUp)): #i don't know Machine learning so better to adjust with what it recognises (close words to fulcrum)
                return True
            else: return False
        except Exception:
            pass
def hear():
    '''listens from mic and returns string output. This function depends on speech recognition's listen which further depends on PyAudio which wasnt installed and cant be installed directly by pip so do pip install pipwin then pipwin install PyAudio (letter case doesnt matter) and then uninstall pipwin'''
    with sr.Microphone() as source:
        print("Listening...")
        # sr.Recognizer().pause_threshold = 1 it will keep listening for 1 second after you stop saying
        #if your environment is too noisy or Fulcrum is responding every single time then you can increse the energy threshold it may also mean you have to be loud
        #sr.Recogniser().energy_threshold = 300 (default)
        audio = sr.Recognizer().listen(source)
    try:
        command = sr.Recognizer().recognize_google(audio, language="en-in") 
        # as good as Google :)
        print("You : %s\n"%command) #printing what you said ;)
        # there are many ways to format string you may haven used .format or fstrings as well
    except Exception as e:
        print("Sorry, didn't recognise that :(\n",e)
        return "FulcrumFailed" #to close our app when it no one is saying anything
    return command

def wish():
    hrs=int(datetime.datetime.now().hour) # to get whats the hour now in 24 hr format
    if hrs<12:
        speak("It is {}, good morning !".format(datetime.datetime.now().strftime("%I:%M %p")))
    elif hrs<18:
        speak("It is {}, good afternoon !".format(datetime.datetime.now().strftime("%I:%M %p")))
    elif hrs<21:
        speak("It is {}, a beautiful evening it is !".format(datetime.datetime.now().strftime("%I:%M %p")))
    else:
        speak("It is {}".format(datetime.datetime.now().strftime("%I:%M %p")))
    speak("Is there anything I can do ?")

if __name__ == "__main__":
    # print("To activate say Hey Fulcrum !") not in use right now
    while (True): # will work only after user activates the Fulcrum
        try:
            task = hear().lower().strip()
            cmnwrds=[" wiki "," wikipedia "," search ","who is "," is "," for "," it ","who was "," was "," has "," had "," do "," does "," to "," what's "," what "," you "," know "," google "," search "," date "]
#basic commands            
            if "fulcrumfailed" in task: break
            elif (("date" in task) and (("what" in task) or ("tell" in task) or ("kya" in task))):
                speak("Today is "+str(datetime.date.today().strftime("%d %B %Y"))) 
                #d means date, B means full month name, Y means year number in 4 digits
            elif (("day" in task) and (("what" in task) or ("tell" in task) or ("kya" in task))):
                speak("It is "+str(datetime.date.today().strftime("%A"))) 
            elif (("time" in task) and (("what" in task) or ("tell" in task) or ("kya" in task))):
                wish()
#searching the web               
            elif ((" wiki " in task) or (" wikipedia " in task) or (" history " in task) or ("who is" in task) or ("who was" in task)):
                for wrd in cmnwrds:
                    task=task.replace(wrd,"")
                task=task.replace(" ","_")
                task=wiki().page(task).summarize(sentences=2)
                speak(task)
            elif (("what is" in task) or ("search google" in task) or ("ask google" in task) or ("google" in task) or ("search" in task) or ("google it" in task) or ("how to" in task) or ("ka matlab" in task) or ("ka mtlb" in task)): 
                #notice the space after the search it is done as in the future im planning to add more functionalities where we can search local directories
                task=task.replace("google","")
                task=task.replace(" ask ","")
                task=task.replace("search ","")
                task=task.replace(" for ","")
                task=task.replace(" it ","")
                task=task.replace(" ","+") # making your url ready
                webbrowser.open("https://www.google.com/search?q=%s"%task) #haha i dont need pywhatkit's help :D
#YouTube :)

            elif ("open youtube " in task):
                webbrowser.open("https://youtube.com")
            elif ("play " in task):
                task=task.replace(" can ","")
                task=task.replace(" please ","")
                task=task.replace(" the ","")
                task=task.replace("play ","")
                task=task.replace(" ","+")
                pywhatkit.playonyt(task)

#everything else
            else:
                webbrowser.open("https://www.google.com/search?q=%s"%(task.replace(" ","")))
        except Exception as e: 
            print("Sorry didn't recognise that :(\n",e)
