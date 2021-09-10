from tkinter import *
import requests
import json

root = Tk()
root.title("Weather app")
root.geometry("600x100")



# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=AE6249DA-23F3-4244-9149-C774EC25A4D6

# Create zipcode lookup function
def zipLookup():
    #zip.get()
    #zip_label = Label(root, text=zip.get())
    #zip_label.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=AE6249DA-23F3-4244-9149-C774EC25A4D6")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        my_label = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."



zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

submit = Button(root, text="Lookup Zipcode", command=zipLookup)
submit.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()