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
config = {
  "apiKey": os.environ['FIREBASE_API_KEY'],
  "authDomain": os.environ['FIREBASE_AUTH_DOMAIN'],
  "databaseURL": os.environ['FIREBASE_DATABASE_URL'],
  "projectId": os.environ['FIREBASE_PROJECT_ID'],
  "storageBucket": os.environ['FIREBASE_STORAGE_BUCKET'],
  "messagingSenderId": os.environ['FIREBASE_MESSAGING_SENDER_ID'],
  "appId": os.environ['FIREBASE_APP_ID'],
  "measurementId": os.environ['FIREBASE_MEASUREMENT_ID']
}

# OPTION 1 - INITIALIZE FIREBASE SDK
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()

# OPTION 2 - INITIALIZE FIREBASE SDK
cred = credentials.Certificate("./firebase-private-key.json")
default_app = firebase_admin.initialize_app(cred)
# initialize instance of firestore
# db = firestore.client()

db = firestore.client()

doc_ref = db.collection(u'test')
doc_ref.add({u'name': u'test', u'added': u'just now'})



# Add a new document
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

# Then query for documents
users_ref = db.collection(u'users')

for doc in users_ref.stream():
    print(u'{} => {}'.format(doc.id, doc.to_dict()))



# db_collection=“{0}{1}”.format('epa_method_9_forms_', str(1)) # ‘epa_method_9_forms_’ + str(1)
# db_collection=‘epa_method_9_forms_’ + str(1)
# record_doc =“{0}{1}”.format('record_', 1) + str(1)
# Add a new EPA method 9 record to collection
doc_ref = db.collection(u'epa-method-9-forms').document(u'record-1')
# doc_ref = db.collection(u db_collection).document(u record_doc)
doc_ref.set({
    u'section_a':
    {
    u'company_name': u'Augusta Waste Processing',
    u'street_address': u'14500 Columbus Drive',
    u'city': u'Evans',
    u'state': u'GA',
    u'zip': u'30815',
    u'phone_key_contact': u'706-415-9856',
    u'source_id_number': 547
    },
    u'section_b1': 
    {
    u'process_equipment': u'Melter',
    u'process_equipment_operating_mode': u'Continuous',
    u'control_equipment': u'Wet Electrostatic Precipitator (WESP)',
    u'control_equipment_operating_mode': u'Continuous'
    }
})


# doc_ref = store.collection(u'names').limit(2)

#try:
#    docs = doc_ref.get()
#    for doc in docs:
#        print(u'Doc Data:{}'.format(doc.to_dict()))
#except google.cloud.exceptions.NotFound:
#    print(u'Missing data')


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
			#section_a_child_object = db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a')                                                                                                                                                                                      
			# db.collection(u'epa-method-9-forms').document(u'record-1').child('section_a').child("company_name").push(company_name)
			#section_a_child_object.child("company_name").push(company_name)
			#section_a_child_object.child("street_address").push(street_address)
			#section_a_child_object.child("city").push(city)
			#section_a_child_object.child("state").push(state)
			#section_a_child_object.child("zip").push(zip_code)
			#section_a_child_object.child("phone_key_contact").push(phone_key_contact)
			#section_a_child_object.child("source_id_number").push(source_id_number)
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

if __name__ == '__main__':
	app.run(debug=True)