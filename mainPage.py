#from command import *
import sys
import operator
import time
import PyPDF2
import pyaudio
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import cv2
import random
from requests import get
import pyjokes
import pywhatkit as kit
from bs4 import BeautifulSoup
from voice import *
from ctypes import resize
from  tkinter import *
import datetime
# from PIL import ImageTK,Image
from time import strftime



tk = Tk()
tk.title('Voice Based Desktop Assistant ')
tk.geometry("700x700")
#-----------Screen Height & Width------------
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

screen_centerx = screen_width / 2
screen_centery = screen_height / 2

tk.rowconfigure(0,weight=1)
tk.columnconfigure(0,weight=1)


def time():
	string = strftime('%H:%M:%S %p')
	Label02.config(text = string)
	Label02.after(1000, time)
 
def temp():
    search = "temperature in Rajshahi"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
    tempd = temp[0] + temp[1]+ temp[2] + 'C'
    Label01.config(text = tempd)

def commandForUser():
	userInput=commandBox.get("1.0","end-1c")
    #userInput = commandBox
	#print(userInput)
	return userInput

def knowWish():
    messageAreaBox.insert(END,"\n"+"Captain: okay sir ,do you have other work " + "\n"+"\n")

def Help():
    f = open("help All Command.txt", "r")
    print(f.read())

def onlyText():
    userInput = commandForUser()
    messageAreaBox.insert(END, "User:"+ userInput )

        # Logic for executing tasks based on userInput
    if 'open google' in userInput:
        speak("sir, what should i search on google")
        cm = userInput.lower()
        webbrowser.open(f"{cm}")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput , 'warning')
        knowWish()

    elif 'features' in userInput:
        messageAreaBox.insert(END, "\n" + "Captain: Okay sir,Now i say All features " + "\n" +
              "01. open and Close notepad" + "\n" +
              "02. Search on Wikipedia " + "\n" +
              "03. open and Close Calculator" + "\n" +
              "04. open and Close Command Prompt" + "\n" +
              "05. Play Youtube" + "\n" +
              "06. open and Close notepad" + "\n" +
              "07. Play Music,etc.")
        # speak("okay sir,Now i say All features"
        #       "First open and Close notepad"
        #       "Second Search on Wikipedia "
        #       "Third open and Close Calculator"
        #       "Fourth open and Close Command Prompt"
        #       "Fifth Play Youtube"
        #       "Sixth open and Close notepad"
        #       "Seventh Play Music")
        knowWish()
    elif "help" in userInput or "how to operate" in userInput:
        speak("hear is the result")
        help()
        knowWish()

    elif 'wikipedia' in userInput:
        speak('Searching Wikipedia...')
        userInput = userInput.replace("wikipedia", "")
        results = wikipedia.summary(userInput, sentences=2)
        messageAreaBox.insert(END, "\n" + "Captain: " + results)
        speak("According to Wikipedia")
        speak(results)
        #print(results)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()

    elif "open calculator" in userInput:
        speak("ok sir.")
        subprocess.call("calc.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()

    elif "close calculator" in userInput:
        speak("okay sir,closing calculator")
        os.system("taskkill /f /im Calculator.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "open notepad" in userInput:
        speak("ok sir, opening notepad.")
        subprocess.Popen(['C:\\Windows\\System32\\notepad.exe'])
        #commandBox.delete('0', END)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()

    elif "close notepad" in userInput:
        speak("okay sir,closing notepad")
        os.system("taskkill /f /im notepad.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "open cmd" in userInput:
        speak("ok sir, opening Command Prompt.")
        subprocess.call("cmd.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "close cmd" in userInput:
        speak("okay sir,closing Command Prompt")
        os.system("taskkill /f /im cmd.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'play youtube' in userInput:
        speak("ok sir what shoud i play on youtube")
        cm = userInput.lower()
        kit.playonyt(f"{cm}")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()

    elif 'play music' in userInput:
        music_dir = 'F:\\Arefin00'
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        #print(rd)
        os.startfile(os.path.join(music_dir, rd))
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'play video song bangla' in userInput:
        music_dir = 'F:\\Video Song\\Bangla Song'
        vbsongs = os.listdir(music_dir)
        #print(vbsongs)
        os.startfile(os.path.join(music_dir))
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'play video song english' in userInput:
        music_dir = 'F:\\Video Song\\English Song'
        vesongs = os.listdir(music_dir)
        #print(vesongs)
        os.startfile(os.path.join(music_dir))
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput)
        knowWish()
        
    elif 'play video song hindi' in userInput:
        music_dir = 'F:\\Video Song\\Hindi Song'
        vhsongs = os.listdir(music_dir)
        #print(vhsongs)
        os.startfile(os.path.join(music_dir))
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput)
        knowWish()
        # elif 'set alarm' in userInput:
        #     nn = int(datetime.datetime.now().hour)
        #     if nn == 22:
        #         music_dir = "F:\\Alarm"
        #         songs = os.listdir(music_dir)
        #         os.startfile(os.path.join(music_dir, songs[0]))

    elif 'open stackoverflow' in userInput:
        webbrowser.open("stackoverflow.com")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open facebook' in userInput:
        webbrowser.open("facebook.com")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open freecodecamp' in userInput:
        webbrowser.open("free codecamo.org")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open w3school' in userInput:
        webbrowser.open("w3school.com")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open bangladesh rail' in userInput:
        webbrowser.open("eticket.railway.gov.bd")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open geeks for geeks' in userInput:
        webbrowser.open("geeksforgeeks.org")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput)
        knowWish()
        
    elif 'open cricbuzz' in userInput:
        webbrowser.open("cricbuzz.com")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open map' in userInput:
        webbrowser.open("maps.google.com")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open translate' in userInput:
        webbrowser.open("translate.google.com")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open chrome' in userInput:
        chromePath = "chrome.exe"
        os.startfile(chromePath)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput + "\n")
        knowWish()
        
        ############################################################################
    elif "close chrome" in userInput:
        #speak("okay sir,closing chrome")
        os.system("taskkill /f /im chrome.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open brave' in userInput:
        bravePath = "brave.exe"
        os.startfile(bravePath)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "close brave" in userInput:
        #print(userInput)
        messageAreaBox.insert(END,"\n" + "Captain: okay sir I will "+ userInput )
        #speak("okay sir,closing brave")
        os.system("taskkill /f /im brave.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "temperature" in userInput:
        search = "temperature in Rajshahi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
        tempd = temp[0] + temp[1]+ temp[2] + 'C'
        #speak(f"current{search} is {temp}")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will searching " + userInput )
        messageAreaBox.insert(END, "\n" + "Captain: Sir now temperature is  " + tempd )
        knowWish()
        
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif 'open pycharm' in userInput:
        pycharmPath = "pycharm64.exe"
        os.startfile(pycharmPath)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "close pycharm" in userInput:
        #speak("okay sir,closing pycharm")
        os.system("taskkill /f /im pycharm64.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open codeblocks' in userInput:
        codeblocksPath = "codeblocks.exe"
        os.startfile(codeblocksPath)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "close codeblock" in userInput:
        #speak("okay sir,closing code block")
        os.system("taskkill /f /im codeblocks.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'open vs code' in userInput:
        vsCodePath = "Code.exe"
        os.startfile(vsCodePath)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "close vs code" in userInput:
        #speak("okay sir,closing vs code")
        os.system("taskkill /f /im Code.exe")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "open camera" in userInput:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k == 27:
                break;
        cap.release()
        cv2.destroyAllWindows()
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()

    elif 'where i am' in userInput or 'where we are' in userInput:
        #speak("wait sir, let me check")
        #try:
        ipAdd = requests.get('https://api.ipify.org').txt
        print(ipAdd)
        url = 'https://get.geojs.io/v1/ip/geo' + ipAdd + '.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        # print(geo_data)
        city = geo_data['city']
        #print(city)
        # state =geo_data['state']
        country = geo_data['country']
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will searching where are you")
        messageAreaBox.insert(END, "\n" + "Captain: Sir, your are now in " + city + "city of " + country)
            #speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
        #except Exception as e:
            #print("sorry")
            #speak("sorry sir, due to network issue i am not able to find where we are.")
            #pass

        ############################################################
    elif 'read pdf' in userInput:
        pdf_reader()
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "IP address" in userInput:
        ip = get('https://api.ipify.org').text
        #speak(f"your IP address is {ip}")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        ############################################################
    # elif 'do some calculations' in userInput or 'can you calculate' in userInput:
    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         speak("say what you want to calculate, example: 3 plus 3")
    #         #print("listening.....")
    #         my_string = userInput
    #     print(my_string)

    #     def get_operator_fn(op):
    #         return {
    #             '+': operator.add(),
    #             '-': operator.sub(),
    #             '*': operator.mul(),
    #             '/': operator.__truediv__()
    #         }[op]

    #     def eval_binary_expr(op1, oper, op2):
    #         op1, op2 = int(op1), int(op2)
    #         return get_operator_fn(oper)(op1, op2)

    #     speak("Your result is : ")
    #     speak(eval_binary_expr(*(my_string.split())))

    elif "screenshot" in userInput or "take a screenshot" in userInput:
        #speak("sir, please tall me the name for this screenshot file")
        name = userInput.lower()
        #speak("please sir hold the screen for few second, i am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        #speak("i am done sir, the screenshot is saved in our main folder, now im ready for next command.")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
#############################################################################################################
    elif 'tell me a joke' in userInput:
        joke = pyjokes.get_jokes()
        #speak(joke)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
    elif 'switch the window' in userInput:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        # Full screen size.-----------------
    elif "minimize the window" in userInput:
        #speak("ok sir i will do this")
        pyautogui.leftClick(1247, 14, 1)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "max the window" in userInput:
        #speak("ok sir i will do this")
        pyautogui.leftClick(1247, 14, 1)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "close the window" in userInput:
        #speak("ok sir closeing the window")
        pyautogui.leftClick(1247, 14, 1)
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
# select,cut,copy,pest,undu,redu.----------------------------------------------
#         elif "select this line" in userInput:
#             time.sleep(3)
#             pyautogui.tripleClick()
#
#         elif "select this " in userInput:
#             time.sleep(3)
#             pyautogui.click()
#             speak("ok sir selected")
#
#         elif "select all" in userInput:
#             time.sleep(3)
#             pyautogui.hotkey('ctrl', 'a')
#             speak("ok sir selected all")

    # elif "copy this file" or "copy this folder" or "copy this line" or "copy this" in userInput:
    #     time.sleep(3)
    #     pyautogui.hotkey('ctrl', 'c')
    #     speak("Sir copy done.")
    #
    # elif "pest this file" or "pest this folder" or "pest this line" or "pest this" in userInput:
    #     time.sleep(3)
    #     pyautogui.hotkey('ctrl', 'v')
    #     speak("Sir pest done.")

    elif "undo" in userInput:
        pyautogui.hotkey('ctrl', 'z')
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()

    elif "redu" in userInput:
        pyautogui.hotkey('ctrl', 'y')
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()

        # ---min
        # pyautogui.leftClick(1247,14,1)
        # ---Max
        # pyautogui.leftClick(1293,12,1)
        # ---close
        # pyautogui.leftClick(1341,14,1)
        # ---------------------------------------------------------------------------
    elif "tell me news" in userInput:
        #speak("please wait sir, feteching the latest news")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput)
        knowWish()
        # ------------------sytdown,restart,sleep------------------------
    elif 'shut down the system' in userInput:
        os.system("shutdown /s /t 5")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'restart the system' in userInput:
        os.system("shutdown /r /t 5")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif "sleep the system" in userInput:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        # -------------------------Exit----------------------------------------------------
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will " + userInput )
        knowWish()
        
    elif 'no thanks' in userInput or 'exit' in userInput:
        #speak("thanks for using me sir, have a good day sir.")
        messageAreaBox.insert(END, "\n" + "Captain: Okk Sir I will Exit ")
        sys.exit()
        
        
    commandBox.delete('1.0',END)
    #speak("sir, do you have other work")
    #knowWish()

#..................................................................................................

#Design..................

tk.config(background='blue')
Label01 = Label(tk,text= temp,font=('Arial',15,'bold'),fg='blue',padx=15,pady=8,bg='white')
Label01.place(x=20,y=100)

temp()

projectNameLabel = Label(tk, bg="black",font='Helvetica 22 bold', fg="white", text="Welcome on Desktop Voice Assisstant Home Page",  pady=12, width=82, height=1)
projectNameLabel.place(x = 20,y=20)

Label02 = Label(tk,text = time,font=('Arial',15,'bold'),fg='blue',padx=14,pady=8,bg='white')
Label02.place(x = screen_width - 180,y=100)

time()

messageAreaBox = Text(tk, bg="blue",font='Helvetica 14 bold', fg="white" ,height= 20, width=90)
messageAreaBox.place(x = 250,y=150)


commandBox = Text(tk, bg="blue",font='Helvetica 14 bold', fg="white" ,height= 2, width=70)
commandBox.place(x = 250,y=screen_height-150)

sendBtn = Button(tk,text='Send',font=('Arial',15,'bold'),fg='blue',padx=15,pady=5,bg='white',command=onlyText)
sendBtn.place(x = screen_width - 505,y=screen_height-150)


speakBtn = Button(tk,text='speak' ,fg='blue',padx=15,pady=5,bg='white',command=allVoice)
speakBtn.place(x = screen_width - 380,y=screen_height-150)


tk.mainloop()

