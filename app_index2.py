import pyrebase # For initializing firebaseSDK  with OPTION 1
import os  # To access ENV firebase variables in .env file
from flask import *

import firebase_admin               # For initializing firebase with OPTION 2
import google.cloud
from firebase_admin import credentials, firestore  # For initializing firebase SDK and firestore with OPTION 2

from dotenv import load_dotenv
# Explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Get the configuration information from the Firebase project
# Go to project settings > select the web app > choose Config (under firebase SDK snippet)

import pyrebase

config = {
  "apiKey": os.environ['FIREBASE_API_KEY'],
  "authDomain": os.environ['FIREBASE_AUTH_DOMAIN'],
  "databaseURL": os.environ['FIREBASE_DATABASE_URL'],
  "storageBucket": os.environ['FIREBASE_STORAGE_BUCKET'],
  "serviceAccount": "./firebase-private-key.json"
}

firebase = pyrebase.initialize_app(config)
# Adding a service account will authenticate as an admin by default for all database queries
# OPTION 1 - INITIALIZE FIREBASE SDK
firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()


COLLECTION_01="epa-method-9-records"
COLLECTION_02="epa-method-22-records"
COLLECTION_03="method-9-field-cert-records"

COLLECTION_NAME="epa-method-9-records"
DOC_NUMBER="record-0002"

def get_collections(collection_name):
    db = firebase.database()
    docs = db.child(collection_name).get()

    counter=0
    # https://github.com/thisbejim/Pyrebase
    for doc in docs.each():

        # print(doc.key())
        # print(doc.val())
        counter = counter + 1
    print("number of docs in collection : ", counter)

def add_new_method9_form(collectionName, docNumber):
# https://github.com/thisbejim/Pyrebase
# To view data- go to Firebase > Database (Realtime Database) > Data
# https://form-automation-method9.firebaseio.com/
# 
    data={
	  "section_0": {"doc_id":"", "date_created":"", "date_completed":"", "author":"", "reviewer":"", "approver":"", "date_approved":""},
      "section_a": {"company_name":"", "street_address":"", "city":"", "state":"", "zip":"", "phone_key_contact":"", "source_id_number":""},   
      "section_b": {"process_equipment":"", "process_equip_op_mode":"", "control_equipment":"", "control_equip_op_mode":""},
      "section_c1": {"describe_emission_unit":""},
      "section_c2": {"height_above_ground_level":"", "start_hagl":"", "end_hagl":"", 
	  				 "relative_height_to_observer":"", "start_rhto":"", "end_rhto":"",
	  				 "distance_from_observer":"", "start_distfo":"", "end_distfo":"",
	  				 "direction_from_observer":"", "start_dirfo":"", "end_dirfo":""},
	  "section_d": {"describe_emissions":"", "start_de":"", "end_de":"", 
	  				"if_water_drop_plume":"", "attached":"", "detached":"", 
					"point_in_plume_at_which_opacity_was_determined":"", "start_pipawowd":"", "end_pipawowd":""},
      "section_e": {"describe_plume_background":"", "start_dpb":"", "end_dpb":"", 
					"background":"", "start_b":"", "end_b":"", 
					"sky_conditions":"", "start_sc":"", "end_sc":"", 
					"wind_speed":"", "start_ws":"", "end_ws":"", 
					"wind_direction":"", "start_wd":"", "end_wd":"", 
					"ambient_temp":"", "start_temp":"", "end_temp":"", 
					"wet_bulb_temp":"", "start_wbt":"", "end_wbt":""},
      "section_g": {"additional_information":""},
      "section_h1": {"observation_date":"", "start_time":"", "end_time":""},	 	  
      "section_h2": [{"row01a":1, "row01b":"", "row01c":"", "row01d":"","row01e":"", "row01f":""},
	  				 {"row02a":2, "row02b":"", "row02c":"", "row02d":"","row02e":"", "row02f":""},
	  				 {"row03a":3, "row03b":"", "row03c":"", "row03d":"","row03e":"", "row03f":""},
	  				 {"row04a":4, "row04b":"", "row04c":"", "row04d":"","row04e":"", "row04f":""},
	  				 {"row05a":5, "row05b":"", "row05c":"", "row05d":"","row05e":"", "row05f":""},
	  				 {"row06a":6, "row06b":"", "row06c":"", "row06d":"","row06e":"", "row06f":""},
	  				 {"row07a":7, "row07b":"", "row07c":"", "row07d":"","row07e":"", "row07f":""},
	  				 {"row08a":8, "row08b":"", "row08c":"", "row08d":"","row08e":"", "row08f":""},
	  				 {"row09a":9, "row09b":"", "row09c":"", "row09d":"","row09e":"", "row09f":""},
	  				 {"row10a":10, "row10b":"", "row10c":"", "row10d":"","row10e":"", "row10f":""},
	  				 {"row11a":11, "row11b":"", "row11c":"", "row11d":"","row11e":"", "row11f":""},
	  				 {"row12a":12, "row12b":"", "row12c":"", "row12d":"","row12e":"", "row12f":""},
	  				 {"row13a":13, "row13b":"", "row13c":"", "row13d":"","row13e":"", "row13f":""},
	  				 {"row14a":14, "row14b":"", "row14c":"", "row14d":"","row14e":"", "row14f":""},
	  				 {"row15a":15, "row15b":"", "row15c":"", "row15d":"","row15e":"", "row15f":""},
	  				 {"row16a":16, "row16b":"", "row16c":"", "row16d":"","row16e":"", "row16f":""},		
	  				 {"row17a":17, "row17b":"", "row17c":"", "row17d":"","row17e":"", "row17f":""},		 	
	  				 {"row18a":18, "row18b":"", "row18c":"", "row18d":"","row18e":"", "row18f":""},			
	  				 {"row19a":19, "row19b":"", "row19c":"", "row19d":"","row19e":"", "row19f":""},	 		
	  				 {"row20a":20, "row20b":"", "row20c":"", "row20d":"","row20e":"", "row20f":""},			
	  				 {"row21a":21, "row21b":"", "row21c":"", "row21d":"","row21e":"", "row21f":""},			
	  				 {"row22a":22, "row22b":"", "row22c":"", "row22d":"","row22e":"", "row22f":""},			
	  				 {"row23a":23, "row23b":"", "row23c":"", "row23d":"","row23e":"", "row23f":""},	 		
	  				 {"row24a":24, "row24b":"", "row24c":"", "row24d":"","row24e":"", "row24f":""},			
	  				 {"row25a":25, "row25b":"", "row25c":"", "row25d":"","row25e":"", "row25f":""},			
	  				 {"row26a":26, "row26b":"", "row26c":"", "row26d":"","row26e":"", "row26f":""},			
	  				 {"row27a":27, "row27b":"", "row27c":"", "row27d":"","row27e":"", "row27f":""},
	  				 {"row28a":28, "row28b":"", "row28c":"", "row28d":"","row28e":"", "row28f":""},					   
	  				 {"row29a":29, "row29b":"", "row29c":"", "row29d":"","row29e":"", "row29f":""},					   
	  				 {"row30a":30, "row30b":"", "row30c":"", "row30d":"","row30e":"", "row30f":""}],
    "section_h3": [
                    {"rowNum": "1", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "2", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "3", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "4", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "5", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "6", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "7", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "8", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "9", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "10", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "11", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "12", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "13", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "14", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "15", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "16", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "17", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "18", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "19", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "20", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "21", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "22", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "23", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "24", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "25", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "26", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "27", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
                    {"rowNum": "28", "sec0": "5", "sec15": "5" , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
                    {"rowNum": "29", "sec0": "10", "sec15": "10" , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
                    {"rowNum": "30", "sec0": "15", "sec15": "15" , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"}
                    ]
    }

    db = firebase.database()
    db.child(collectionName).child(docNumber).set(data)

    print("executed add new method9 form")


add_new_method9_form(COLLECTION_NAME, DOC_NUMBER)

def number_of_docs_in_collection(collection_name):
    return 0

def update_section(collectionName, docNumber, section_data):

    return 0

get_collections(COLLECTION_NAME)

#section_a_data = {"m9-forms-collection/record-0001/section_a/": 
#   {    "company_name": "NY Pollution Center",
#        "street_address": "231 Kabelenga",
#        "city": "New York",
#        "state": "NY",
#        "zip": 32587,
#        "phone_key_contact": "710-456-3258",
#        "source_id_number": 215897
#    }
#}
#db.update(section_a_data)

h_data=[
{"rowNum": 1, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 2, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 3, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 4, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 5, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 6, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 7, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 8, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 9, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 10, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 11, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 12, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 13, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 14, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 15, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 16, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 17, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 18, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 19, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 20, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 21, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 22, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 23, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 24, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 25, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 26, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 27, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"},
{"rowNum": 28, "sec0": 5, "sec15": 5 , "sec30": 5, "sec45":5, "Notes": "From the rather self concious heights of"},
{"rowNum": 29, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 30, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"}
]



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add_section_a':
			company_name = request.form['company_name']
			street_address = request.form['street_address']
			city = request.form['city']
			state = request.form['state']
			zip_code = request.form['zip']
			phone_key_contact = request.form['phone_key_contact'] 
			source_id_number = request.form['source_id_number']

			print(u'{}'.format(company_name)) 
			print(u'{}{}{}{}{}{}{}'.format(company_name, street_address, city, state, zip_code, phone_key_contact, source_id_number))                                                                                                                                                                                                   

			PATH=COLLECTION_NAME+"/"+DOC_NUMBER+"/"+"section_a/" 			
			section_a_data={PATH :{"company_name": company_name, "street_address": street_address, "city": city, "state": state, "zip": zip_code, "phone_key_contact": phone_key_contact, "source_id_number": phone_key_contact}} 
			db.update(section_a_data)

			return render_template('index2.html', h_data=h_data)              
		elif request.form['submit'] == 'clear_section_a':     
			db.child("section_a").remove()
		#return render_template('index2.html')
		return render_template('index2.html', h_data=h_data)
	# return render_template('index2.html')
	return render_template('index2.html', h_data=h_data)

if __name__ == '__main__':
	app.run(debug=True)