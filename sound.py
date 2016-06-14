''' Script to execute commands using your voice
    python - 2.x required 
'''

# import required modules 
import pyaudio,os
import speech_recognition as sr

#function to open web browser
def cBrowser():
        os.system("path of chrome browser ")

#function to open a text editor
def editor():
        os.system("path of text editor ")
#function to open a media file present on the local computer
def media():
        os.system("path of any media file ")

#main file to execute 
def execute(source):
    print 'say something:'
    audio = r.listen(source)
    user = r.recognize_google(audio)
    print(user)
    if user == "internet":
        cBrowser()
    elif user == "editor":
        editor()
    elif user == "music":
        media()

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            execute(source)
