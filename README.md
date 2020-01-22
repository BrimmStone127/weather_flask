# Weather Flask Server
This is a straightforward flask RESTful server.

## Running locally via Flask development server
NOTE: Flask development server is intended for developing/debugging it should not be used in production environments directly exposed to web traffic.
This guide is written using OSX and a unix terminal. You will need python3 installed to run the server https://www.python.org/downloads/

1: Move into the server directory
```
cd /server
```
2. Either copy and paste this command or create a new python virtual environment and perform the pip commands
```
python3 -m venv venv  # creates ./venv
. venv/bin/activate  # enable using this venv
pip install --upgrade pip  # avoid nagging upgrade msgs
pip install -r requirements.txt  # installs flask et al
flask run
# Now visit http://localhost:5000
```


3. This should startup and run the server on localhost:5000
