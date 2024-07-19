import time
from PIL import Image
import requests

def Starting():
    {
        print("\nWelcome to Penguin Display Program."),
        print("\nVersion 1")
    }
def PenguinDisplay():
        im = Image.open(requests.get("https://www.freeiconspng.com/uploads/little-funny-penguin-png-2.png", stream=True).raw)
        im.show()
def Closing():
     {
     print("Thank you for running this program.")
     }

Starting()
# print("Please wait 5 seconds...\n")
# time.sleep(5.5)
PenguinDisplay()
Closing()


  
