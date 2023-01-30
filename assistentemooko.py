import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import subprocess

def takeCommand(): 
  
    r = sr.Recognizer() 
  
    
    
    
    with sr.Microphone() as source: 
        print('Listening') 
        
      r.pause_threshold = 0.7
        audio = r.listen(source) 
        
      
      try: 
            print("Recognizing") 
                      Query = r.recognize_google(audio, language='pt-br') 
            print("the command is printed=", Query) 
            except Exception as e: 
            print(e) 
            print("Diga novamente por favor") 
            return "None"
        return Query 
  
def speak(audio): 
      
    engine = pyttsx3.init() 
    
    
    voices = engine.getProperty('voices') 
      
    
    
    engine.setProperty('voice', voices[0].id) 
      
    
    engine.say(audio)   
      
    
    
    engine.runAndWait() 
  
def tellDay(): 
      
    
    
    day = datetime.datetime.today().weekday() + 1
      
    
    
    Day_dict = {1: 'Segunda', 2: 'Terça',  
                3: 'Quarta', 4: 'Quinta',  
                5: 'Sexta', 6: 'Sabado', 
                7: 'Domingo'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("Hoje é " + day_of_the_week) 
  
  
def tellTime(): 
      
    
    time = str(datetime.datetime.now()) 
      
    
    
    
    print(time) 
    hour = time[11:13] 
    min = time[14:16] 
    speak(self, "Agora são: " + hour + "h" + min + "m")     
  
def Hello(): 
      
    
    
    
    speak("Olá, eu sou seu assistente virtual. /Diga-me como posso ajudá-lo") 
  
  
def Take_query(): 
  
    
    
    Hello() 
      
    
    
    
    
    while(True): 
        
      
      query = takeCommand().lower() 
        if "abrir youtube" in query: 
            speak("Abrindo youtube ") 
                      webbrowser.open("www.youtube.com") 
            continue
        elif "abrir facebook" in query: 
            speak("Abrindo facebook ")
            webbrowser.open("www.facebook.com")
            continue
        elif "abrir instagram" in query:
            speak("Abrindo facebook ")
            webbrowser.open("www.instagram.com")
            continue
            elif "que dia é hoje" in query:
            tellDay() 
            continue
        elif "abrir google" in query: 
            speak("Abrindo google ") 
            webbrowser.open("www.google.com")
            continue
        elif "tell me the time" in query: 
            tellTime() 
            continue       
        elif "tchau" in query: 
            speak("Tchau, me chame quando precisar.....") 
            exit()
        elif "from wikipedia" in query: 
                    speak("Checar na wikipedia ")
            query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences=4)
            speak("Checando no wikipedia")
            speak(result)
            continue
        elif "abrir  firefox" in query:
            speak("Abrindo navegador FireFox Monzilla")
            subprocess.call(['C:\Program Files\Monzilla Firefox\\firefox.exe'])
            continue
        elif "abrir o chrome" in query:
            speak("Abrindo o google chrome")
            subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe'])
            continue
        elif "abrir telegram" in query:
            speak("Abrindo telegram")
            subprocess([''])
            continue
        elif "abrir steam" in query:
            speak("Abrindo a steam")
            subprocess([''])
            continue
        elif "me fale seu nome" in query: 
            speak("Eu sou Mooko sua assistente virtual") 
  
if __name__ == '__main__': 
      
    
    
    Take_query()
