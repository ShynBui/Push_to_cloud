import math
import datetime
from flask import render_template, request, redirect, session, jsonify, url_for
from saleapp import app, admin, untils, dbx
from flask_login import login_user, logout_user, login_required, current_user
import cloudinary.uploader
import dropbox

@app.route("/", methods=['post', 'get'])
def home():
    print(dbx.users_get_current_account())
    return render_template('index.html')


@app.route('/upload', methods=['get', 'post'])
def upload():
    print("2")
    file = request.files.get('file')

    link = dbx.files_upload(file.read(), '/' + file.filename)

    shared_link = dbx.sharing_create_shared_link_with_settings('/' + file.filename,
                                                               settings=dropbox.sharing.SharedLinkSettings(requested_visibility=dropbox.sharing.RequestedVisibility.public)).url
    print(shared_link)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
