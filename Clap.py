import sounddevice as sd 
import numpy as np 
import pyttsx3

threshold = 1
clap = False

def detect_clap(indata,frames,time,status):
    global clap
    valume_norm = np.linalg.norm(indata) * 10
    if valume_norm > threshold:
        print("claped!")
        clap = True


def listen_for_clap():
    with sd.InputStream(callback= detect_clap):
        return sd.sleep(1000)
    

#if __name__ == "__main__":
    
def MainclapExe():
    while True:
        listen_for_clap()
        if clap == True:
            break
        else:
            pass





def check_speakers():
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Get the list of available voices
        voices = engine.getProperty('voices')

        # Set the first voice (you can change this to test different voices)
        engine.setProperty('voice', voices[0].id)

        # Test the speakers by saying a test message
        engine.say("This is a test message to check if the speakers are working.")

        # Wait for the speech to finish
        engine.runAndWait()

        # If the code reaches this point without raising an exception, the speakers are working
        return True
    except Exception as e:
        # If an exception occurs (e.g., no speakers found, engine initialization failed), return False
        print(f"An error occurred: {e}")
        return False

# Test the function
#if check_speakers():
    #print("Speakers are working.")
#else:
 #   print("Speakers are not working.")

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wait_until_speaking_finished():
    engine = pyttsx3.init()
    speaking = True

    def on_end(name, completed):
        nonlocal speaking
        speaking = False

    engine.connect('finished-utterance', on_end)

    # Wait until speaking is finished
    while speaking:
        pass

# Example usage
text = "This is a test message to check if the speakers are working."
speak(text)
wait_until_speaking_finished()
print("Speaking finished.")
