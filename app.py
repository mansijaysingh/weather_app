from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():
    weather=None
    if request.method== "POST":
      city=request.form["city"]
      api_key="60caaec60d62470ea3543516252907"
      url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
      response=requests.get(url)
      data=response.json()
      if "current" in data:
         weather={
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temp": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
         }
      else:
         weather = {"error": "City not found"}
         
    return render_template("index.html",weather=weather)
   
if __name__ == "__main__":
    app.run(debug=True)