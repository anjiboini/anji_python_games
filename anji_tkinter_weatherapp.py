from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root=Tk()
root.title('wellcome to Thanusri weather app')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry("600x400")

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=2C32A18F-97FF-4216-9E90-E813D1BC4EC7




try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=2C32A18F-97FF-4216-9E90-E813D1BC4EC7")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

except Exception as e:
    api = "Error...."

myLabel = Label(root, text=city +"Air Quality"+ str(quality) + " " + category, font=("Helevetica",20),bg="green")
myLabel.pack()








root.mainloop()
