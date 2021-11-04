import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import numbers
import winsound
import re
import requests
import bs4
import smtplib
import time
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import screen_brightness_control as sbc


sand = []

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def countdown(content):
    while content:
        mins, secs = divmod((content), 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        content -= 1
    speak("Completed")
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    print("I am your Virtual Assistant Sir. Please tell me how may I help you?")
    speak("I am your Virtual Assistant Sir. Please tell me how may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('qwertyforwork@gmail.com', 'jyppeoscgghmqlbf')
    server.sendmail('qwertyforwork@gmail.com', toaddr, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    a = 1
    while a != 0:
        # if 1:
        query = takeCommand().lower()

        if 'youtube' in query:
            print("What should I search?")
            speak("What should I search?")
            content = takeCommand()
            url = 'https://www.youtube.com/results?search_query=' + content
            webbrowser.open(url)
            print('Done')
            speak('Done')

        elif "google" in query:
            speak("opening google")
            url = 'https://www.google.com/'
            webbrowser.open(url)
            print('Done')
            speak('Done')
        elif "can do" in query:
            speak("I can send email, read news headlines, read weather forecasts, open useful application, store messages and control brightness of the computer system")
        elif "like" in query:
            speak("I like to help you in your work")
            print("I like to help you in your work")

        elif "calculator" in query:
            speak("Okay Sir, I am opening calculator")
            os.system("C:\\Windows\\System32\\calc.exe")

        elif "notepad" in query:
            speak("Okay Sir, I am opening notepad")
            os.system("C:\\Windows\\System32\\notepad.exe")
        elif "paint" in query:
            speak("Okay Sir, I am opening paint")
            os.system("C:\\Windows\\System32\\mspaint.exe")
        elif "WordPad" in query:
            speak("Okay Sir, I am opening wordpad")
            os.system("C:\\Windows\\System32\\write.exe")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'email' in query:
            try:
                speak("Whom should i sent email to?")
                to = takeCommand()
                edict = {'Vikas': 'mauryvikas12345@gmail.com',
                         'Ankit': 'akumar397800@gmail.com'}
                toaddr = edict[to]
                speak("What should I say?")
                content = takeCommand()
                sendEmail(toaddr, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir , I can not send this")

        elif "how are you" in query:
            speak("I am fine sir")

        elif "what is your name" in query:
            speak("I don't have a name yet")

        elif "who are you" in query:
            speak("I am Virtual Assistant")

        elif "why virtual friend" in query:
            speak("Because i will help you to make your life simple")

        elif "sound" in query:
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
            speak("Done sir!")

        elif "message" in query:
            speak("What message you want to store?")
            content = takeCommand()
            speak("Alright!")
            print("Alright!")
            sand.append(content)

        elif "inbox" in query:
            for x in sand:
                speak(x)
                print(x)
                speak("do you want to delete last messege")
                print("do you want to delete last messege")
                query = takeCommand()
                if "yes" in query:
                    sand.remove(x)
                if "no" in query:
                    speak("Messege not deleted")
                    print("Message not deleted")
                    pass

        elif "write" in query:
            speak("speak")
            print("speak")
            query = takeCommand()
            f = open("new.txt", "w")
            f.write(query)
            f.close()

        elif "countdown" in query:
            speak("Tell me the time in seconds:")
            content = takeCommand()

            try:
                countdown(int(content))
            except:
                speak("try again with only numbers please")

        elif 'wikipedia' in query:
            speak('What should I search')
            try:
                query = takeCommand().lower()
                results = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("try again")
                print("try again")

        elif 'weather' in query:
            print("Which city Sir?")
            speak("Which city Sir?")
            api_key = "6f06ee7a096d9b0b7d5b3c5bda07c46e"

            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            # Give city name
            city_name = takeCommand()
            print(str(city_name)+" Weather report:\n")
            complete_url = base_url + "appid=" + api_key + \
                "&q=" + city_name + "&units=metric"

            response = requests.get(complete_url)
            x = response.json()
            # print(x)
            if x["cod"] != "404":

                y = x["main"]
                current_temperature = y["temp"]

                current_pressure = y["pressure"]

                current_humidiy = y["humidity"]

                z = x["weather"]

                weather_description = z[0]["description"]

                print(" Temperature (kelvin) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (hPa) = " +
                      str(current_pressure) +
                      "\n humidity () = " +
                      str(current_humidiy) + "%" +
                      "\n description = " +
                      str(weather_description))
                speak(" Temperature (in celcius unit) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                print(" City Not Found ")

        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[random.random()]))

        elif "news" in query:
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            count = 0
            speak("How many news headline sir?   ")
            print("How many news headline sir?")
            limit = takeCommand()
            soup_page = soup(xml_page, "lxml")
            news_list = soup_page.findAll("item")
            # Print news title, url and publish date
            for news in news_list:
                print(news.title.text)
                print(news.link.text)
                speak(news.title.text)
                speak(news.link.text)
                count += 1
                if count > int(limit):
                    break

        elif "exit" in query:
            speak("See you later, Sir")
            a = 0

        elif "shutdown" in query:
            speak("Do you wish to shutdown your computer ? (yes / no): ")
            shutdown = takeCommand().lower()
            if shutdown == 'yes':
                print("Shutting down")
                speak("Shutting down in 10 second")
                os.system("shutdown /s /t 10")
            else:
                pass
        elif "restart" in query:
            speak("Do you wish to restart your computer ? (yes / no): ")
            shutdown = takeCommand().lower()
            if shutdown == 'yes':
                os.system("shutdown /r /t 25")
                speak("restarting in 25 seconds")
            else:
                pass

        elif "sleep" in query:
            speak("Do you wish to sleep your computer ? (yes / no): ")
            shutdown = takeCommand().lower()
            if shutdown == 'yes':
                os.system("shutdown /h /t 2")
            else:
                pass

        elif "Abort" in query:
            speak("Do you wish to abort shutdown or restart (yes / no): ")
            shutdown = takeCommand().lower()
            if shutdown == 'yes':
                os.system("shutdown -a")
            else:
                pass

        elif "alarm" in query:
            speak("Please enter time manually")
            alarm_hour = int(input("Set hour: "))
            alarm_minutes = int(input("Set minutes: "))
            am_pm = input("am or pm? ")
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

            print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")
            if am_pm == 'pm':  # to convert pm to military time
                alarm_hour += 12

            elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
                alarm_hour -= 12

            else:
                pass

            while True:  # infinite loop starts to make the program running until time matches alarm time

                # ringing alarm + execution condition for alarm
                if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:

                    print("\nIt's the time!")
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    break

        elif "brightness" in query:
            ans = "no"
            curr_brightness = sbc.get_brightness()
            while(ans != "yes"):
                speak("How much brightness do you want?")
                try:
                    br = takeCommand()
                    sbc.set_brightness(br)
                    speak("Do you want this much ??")
                    ans = takeCommand().lower()
                    if (ans == "no"):
                        sbc.set_brightness(curr_brightness)
                    elif (ans == "yes"):
                        speak(f"brightness has been set to {br}")
                except:
                    speak("Please speak clearly")
                    ans = "no"
            print(curr_brightness)
