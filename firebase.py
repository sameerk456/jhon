import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyChNUk_bvNP34KhOoEESp1M37UIWx3kEnI",
  "authDomain": "jhon-d40cb.firebaseapp.com",
  "projectId": "jhon-d40cb",
  "storageBucket": "jhon-d40cb.appspot.com",
  "messagingSenderId": "541836789809",
  "appId": "1:541836789809:web:6bb1aa2fcad8c8ee8ded10",
  "measurementId": "G-RZJ2G941LD",
  "databaseURL":"https://jhon-d40cb-default-rtdb.firebaseio.com/"
};
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
#push data
data={"name":"anupama","age":23,"address":["xyz","abcd"]}
db.push(data)
