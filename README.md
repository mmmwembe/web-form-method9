# web-form-method9
# Michael Mwembeshi
# 1/26/2020
# 
# Objective: 
# Build a fully functioning CRUD web application for EPA Method 9 Form automation using:
#   (a) Firebase
#   (b) Python (pyrebase, Flask)
# The web app will include a real-time database (Firestore database) that integrates fully between the web app # and mobile app
# References:
#   1) https://blog.upperlinecode.com/flask-and-firebase-and-pyrebase-oh-my-f30548d68ea9
#   2) https://medium.com/@cbrannen/importing-data-into-firestore-using-python-dce2d6d3cd51
#   3) https://github.com/googleapis/google-cloud-python/tree/master/firestore
#   4) https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/firestore/cloud-client/snippets.py
#   5) https://github.com/thisbejim/Pyrebase
#   6) https://github.com/thisbejim/Pyrebase

Step 1: Install pyrebase (Python for Firebase module), flask and python-dotenv
```bash
    pip install pyrebase
    pip install flask
    pip install python-dotenv
    pip install firebase_admin
    pip install google-cloud-firestore
    pip install os-win  # for use of os.env on MS Windows
```

Step 2: Clone web-form-method9 repo from our github repo
```bash
    git clone https://github.com/mmmwembe/web-form-method9.git
```

Step 3: Install Firebase CLI
# To host your site with Firebase Hosting, you need the Firebase CLI (a command line tool).
# Run the following npm command to install the CLI or update to the latest CLI version
```bash
    npm install -g firebase-tools
```

Step 4: change directory into web-form-method9 directory
```bash
    cd web-form-method9
```

Step 5: Run app.py
```bash
    python app.py
```
e.g: Running on http://127.0.0.1:5000/
     https://localhost:5000/

Step 6: Go to URL displayed from step 5
