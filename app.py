from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from flask_pymongo.wrappers import MongoClient
import scraping


app = Flask(__name__)

#Use flask PyMongo to set up nongo connection
#URI is a uniform resource identifier sililiar to a URL
app.config["MONGP_URI"] = "mongodb://localhost:27017/mars_app"

@app.route("/")
def index():
    mars= mongo.db.mars.find_one()
    return render_template("index.html",mars=mars)

@app.route("/scrape")
def scrape():
    mars= mongo.db.mars
    mars_data=scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/',code=302)

if __name__ = "__main__":
    app.run()