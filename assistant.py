from gtts import gTTS
import speech_recognition as sr 
import os
import webbrowser
import smtplib


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

# listen


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print('I am ready for you command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print('You said: ' + command + '/n')

            # loop back to continue to listen for commands
        except sr.UnknownValueError:
            assistant(myCommand())
        return command


def assistant(command):
    # if 'open Reddit python' in command:
    #     chrome_path = '/usr/bin/google-chrome'
    #     url = 'https://www.reddit.com/r/python'
    #     webbrowser.get(chrome_path).open(url)

    if 'whats up ' in command:
        talkToMe('chill')

    if 'email' in command:
        talkToMe('Who is the recipient')
        recipient = myCommand()

    if 'john' in recipient:
        talkToMe('What should I say')
        content = myCommand()

        # init gmail smtp
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        # identify with the server
        mail.ehlo()

        # encrypt session
        mail.starttls()
        # loggin
        mail.login('alvinkhamron@gmail.com', '')

        # send message
        mail.sendmail('person name', 'emailaddress@blah.com', content)
        # close the connection
        mail.close()

        talkToMe('Email sent')


talkToMe('I am ready for your command')
while True:
    assistant(myCommand())