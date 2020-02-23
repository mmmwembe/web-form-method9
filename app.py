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
db = firestore.client()



store = firestore.client()
doc_ref = store.collection(u'names').limit(2)

try:
    docs = doc_ref.get()
    for doc in docs:
        print(u'Doc Data:{}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)