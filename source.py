import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #to get detail of voice
engine.setProperty('voice', voices[1].id) 

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")    
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")       
    
    else:
        speak("Good Evening!")      
   
def speak(audio):   
    engine.say(audio)    
    engine.runAndWait() 

def listener():   
     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")    
        except Exception as e:
            print("Say that again please...")  
            return "None" 
        return query

if __name__=="__main__" : 
    greet()
    speak("Who am I talking to")
    name=listener()   
    speak(f'Hello {name}, I am JUFKA, your virtual assistant. Please tell me how may I help you')
    while True:
        query = listener().lower()        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "who made you" in query or "who created you" in query:
            speak("I was made by three crazy friends. Jumana Fiza Kavya. Hence my name is JUFKA.")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
        elif 'day' in query:
            day = datetime.datetime.today().weekday() + 1
      
            Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)
        elif "weather" in query:
            api_key = '17c55ab872189919f68ef501c43f62e0'
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = listener()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            data = response.json()
             
            if data["cod"] != "404":
                y = data['main']
                current_temperature = y["temp"]
                speak(f"Current temperature in {city_name} is {current_temperature}")
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy))
                
            else:
                speak(" City Not Found ")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
