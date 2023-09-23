import time
from playsound import playsound
def countdown(seconds):
    while seconds>=0: #or "while seconds:"
        mins=int(seconds/60)
        sec=int(seconds%60)
        timer=f"{mins}:{sec}"
        print(timer)
        time.sleep(1)
        seconds=seconds-1
    print("Time up!")
    playsound("C:/Users/Renju/Desktop/New folder/C101_StudentActivity1_Soundfile-main/mixkit-sound.wav")




seconds=int(input("Enter time in seconds: "))
countdown(seconds)