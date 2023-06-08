from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager
import dropbox

# Set up Dropbox client
dbx = dropbox.Dropbox('sl.Bf7n-5aeo5OOMTw9sK_SBMM77l93xLCyi7PPMB6hDHC7AVyyxyousOPXoF-7ZcRfRJ5CauCIvN9D40n4UhVMrPT-iMnsdZBlN2zBc4wmhRsfrjGgxNIou0UrWGIqPUNXY_-V-a8')
app = Flask(__name__)




