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
RECORD_PREFIX="record"
RECORD_NUMBER=1

def get_collections(collection_type):
    db = firebase.database()
    collections_ref = db.collection("{}".format(collection_type))
    docs = collections_ref.stream()

    for doc in docs:
        print("{}=>{}".format(doc.id, doc.to_dict()))

# print("collection_01 :", COLLECTION_01)
# get_collections(COLLECTION_01)

def add_new_method9_form():
# https://github.com/thisbejim/Pyrebase
# To view data- go to Firebase > Database (Realtime Database) > Data
# https://form-automation-method9.firebaseio.com/
# 
    data={
	  "section_0": {"doc_id":"", "doc_status": "","date_created":"", "date_completed":"", "author":"", "reviewer":"", "approver":"", "date_approved":""},
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
      "section_h2": {"row01a":"", "row01b":"", "row01c":"", "row01d":"","row01e":"",
	  				 "row02a":"", "row02b":"", "row02c":"", "row02d":"","row02e":"",
	  				 "row03a":"", "row03b":"", "row03c":"", "row03d":"","row03e":"",
	  				 "row04a":"", "row04b":"", "row04c":"", "row04d":"","row04e":"",
	  				 "row05a":"", "row05b":"", "row05c":"", "row05d":"","row05e":"",
	  				 "row6a":"", "row6b":"", "row6c":"", "row6d":"","row6e":"",
	  				 "row07a":"", "row07b":"", "row07c":"", "row07d":"","row07e":"",
	  				 "row08a":"", "row08b":"", "row08c":"", "row08d":"","row08e":"",
	  				 "row09a":"", "row09b":"", "row09c":"", "row09d":"","row09e":"",
	  				 "row10a":"", "row10b":"", "row10c":"", "row10d":"","row10e":"",
	  				 "row11a":"", "row11b":"", "row11c":"", "row11d":"","row11e":"",
	  				 "row12a":"", "row12b":"", "row12c":"", "row12d":"","row12e":"",
	  				 "row13a":"", "row13b":"", "row13c":"", "row13d":"","row13e":"",
	  				 "row14a":"", "row14b":"", "row14c":"", "row14d":"","row14e":"",
	  				 "row15a":"", "row15b":"", "row15c":"", "row15d":"","row15e":"",
	  				 "row16a":"", "row16b":"", "row16c":"", "row16d":"","row16e":"",		
	  				 "row17a":"", "row17b":"", "row17c":"", "row17d":"","row17e":"",			
	  				 "row18a":"", "row18b":"", "row18c":"", "row18d":"","row18e":"",			
	  				 "row19a":"", "row19b":"", "row19c":"", "row19d":"","row19e":"",			
	  				 "row20a":"", "row20b":"", "row20c":"", "row20d":"","row20e":"",			
	  				 "row21a":"", "row21b":"", "row21c":"", "row21d":"","row21e":"",			
	  				 "row22a":"", "row22b":"", "row22c":"", "row22d":"","row22e":"",			
	  				 "row23a":"", "row23b":"", "row23c":"", "row23d":"","row23e":"",			
	  				 "row24a":"", "row24b":"", "row24c":"", "row24d":"","row24e":"",			
	  				 "row25a":"", "row25b":"", "row25c":"", "row25d":"","row25e":"",			
	  				 "row26a":"", "row26b":"", "row26c":"", "row26d":"","row26e":"",			
	  				 "row27a":"", "row27b":"", "row27c":"", "row27d":"","row27e":"",
	  				 "row28a":"", "row28b":"", "row28c":"", "row28d":"","row28e":"",					   
	  				 "row29a":"", "row29b":"", "row29c":"", "row29d":"","row29e":"",					   
	  				 "row30a":"", "row30b":"", "row30c":"", "row30d":"","row30e":""}	  	  	  	  	  	  
    }

    db = firebase.database()
    db.child("epa-method-9-records").child("record-0002").set(data)

    print("executed add new method9 form")


add_new_method9_form()


section_a_data = {"m9-forms-collection/record-0001/section_a/": 
   {    "company_name": "NY Pollution Center",
        "street_address": "231 Kabelenga",
        "city": "New York",
        "state": "NY",
        "zip": 32587,
        "phone_key_contact": "710-456-3258",
        "source_id_number": 215897
    }
}
db.update(section_a_data)



h_data=[{"rowNum": 1, "sec0": 5, "sec15": 10 , "sec30": 25, "sec45":20, "Notes": "From the rather self concious heights of"},
{"rowNum": 2, "sec0": 10, "sec15": 10 , "sec30": 10, "sec45":10, "Notes": "All the same. Cool, sunny and cool"},
{"rowNum": 3, "sec0": 15, "sec15": 15 , "sec30": 15, "sec45":15, "Notes": "Monday - cold and who knows"}
]


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':
			company_name = request.form['company_name']
			street_address = request.form['street_address']
			city = request.form['city']
			state = request.form['state']
			zip_code = request.form['zip']
			phone_key_contact = request.form['phone_key_contact'] 
			source_id_number = request.form['source_id_number']

			print(u'{}'.format(company_name)) 
			print(u'{}{}{}{}{}{}{}'.format(company_name, street_address, city, state, zip_code, phone_key_contact, source_id_number))                                                                                                                                                                                                   
			#db.child("todo").push(name)
			#todo = db.child("todo").get()
			#to = todo.val()
			# return render_template('index.html', t=to.values())
			return render_template('index2.html')            
		elif request.form['submit'] == 'clear':
			db.child("section_a").remove()
		return render_template('index2.html')
	return render_template('index2.html')
@app.route('/modal', methods=['GET', 'POST'])
def get_btn_value():
	if request.method == 'POST' and (request.form['btn_x']!='close'):
		btn_value = request.form['btn_x']
		print("opacity ", btn_value)
	return render_template('modal.html')

if __name__ == '__main__':
	app.run(debug=True)