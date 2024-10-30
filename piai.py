import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyttsx3
import speech_recognition as sr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import warnings
warnings.simplefilter('ignore')


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def QuerySender(Query):
    XpathInput = '/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea'
    XpathSenderButton ='/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button'
    
    # Wait for the input element to be clickable
    input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, XpathInput)))
    input_element.send_keys(Query)
    
    # Locate and click the sender button
    sender_button = driver.find_element(by=By.XPATH, value=XpathSenderButton)
    sender_button.click()
    sleep(5)



def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recogizing....")
        query = r.recognize_google(audio,language="en")
        print(f"==> Shresth : {query}")
        return query.lower()

    except:
        return ""



ScriptDir = pathlib.Path().absolute()
url = "https://pi.ai/talk"

chrome_option = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_option.add_argument(f"user_agent={user_agent}")
chrome_option.add_argument('--profile-direectory=Default')
chrome_option.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
#chrome_option.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)
driver.maximize_window()
driver.get(url=url)
sleep(5)
chatNumber = 3




def resulScalper():
    xpathofresult ='/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div'
    
    TEXT = driver.find_element(by=By.XPATH,value=xpathofresult).text
    sleep(2)
    return TEXT

def soundOnbutton():
    xpathsoundbotton = '/html/body/div/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button'
    driver.find_element(by=By.XPATH,value=xpathsoundbotton).click()
#QuerySender("Hello How are you !")
 

#soundOnbutton()

while True:
    Query = speechrecognition()
    if len(str(Query))<3:
        pass

    elif Query == None:
        pass

    else:
        QuerySender(Query=Query)
        sleep(10)
        text = resulScalper()
        engine = pyttsx3.init()
        engine.runAndWait()
        speak(text=text)
    