# -*- coding: UTF-8 -*-
from flask import Flask
from flask import Flask, render_template, request, session, redirect, url_for, flash, abort;
import nmap, sqlite3
import inputHandler
import os
#import helper.db.createDB
import helper.generateLink
from helper import readPropFiles
import docker


# die Session muss noch gespeichert werden. ToDo: Sessions sind hier wichtig, es ist aktuell ein single User System

# Hier muss anhand der Liste selectedScan entschieden werden, welche Webseite an den Beantrager ausgeliefert wird
# Es muss eine Reihenfolge mit weiteren Fragen, anhand der Liste erstellt werden.
# Wichtig ist, dass man nur soviel Infos abfragt, die benötigt werden

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

#Hier existiert noch kein kontent. Muss noch erstellt und überarbeitet werden
@app.route('/dev/<app>')
def dev(app):
    return render_template('DevelopmentSec.html', app=app)
# aktueller PoC Pfad. d.h. der erste Pfad,d er wirklich produktiv gesetzt werd
@app.route('/ops')
def ops():
    return render_template('OperationsSec.html')
# Hier ist nur ein einfaches Formular hinterlegt ohne Fuktionalität. Bei submit ist eine Seite hinterlegt, die keine posts erlaubt
@app.route('/infra')
def infra():
    return render_template('InfrastructureSec.html')
# Hier sollen Red Teams, Pentests etc. beauftragt werden können. ebenfalls nur das Formular wie bei Infra hinterlegt
@app.route('/individual')
def individual():
    return render_template('individualRequest.html')

@app.route('/result', methods=['POST'])
def result():
    #ToDo: E-mail Notification für ISO einfügen

    #test Start docker

    return render_template('results.html', result="scanning")

@app.route('/handleOpsSelection', methods=['POST'])
def handleOpsSelection():
    # Wir benötigen noch den Namen des Beantragers, Assets und den Namen des ISO. Darüber kann festgestellt werden ob
    # der Beantrager den Scan für das betroffene Asset beantragen darf.
    # in der nächsten Ausbaustufe soll Mittels Rollen und Nutzerkonten festgelegt werden, wer was für welchen Nutzer einstellen darf
    # Hier soll dann auch ein schedule System eingeführt werden, für alle, die eine zyklische Überprüfung wünschen

    selectedScans = inputHandler.selectOps(request.form)
    info = inputHandler.appInfo(request.form)
    print(info)

    return render_template('/detailSelection/selectDetailsOps/selectDetailsOps.html', app=info.get("app"),
                          url=info.get("url"),
                          req_mail=info.get("req_mail"),
                          env=info.get("environment"),
                          reason=info.get("reason"),
                          owner=info.get("owner"),
                          add_info=info.get("add_info"),
                          desc=info.get("desc"),
                          scanTypes=selectedScans)

@app.route('/startScans', methods=['POST'])
def startSans():
    return 'ToDo'
    # ToDo hier müssen die Scans gestartet werden und die ergebnisse nach und nach angezeigt werden bzw. ein Link zu den
    # Ergebnissen an den Owner geschickt werden

#Dieser Endpunkt dient dem Aufgeben eines Scan Starts.
@app.route('/scanStart/<scanId>')
def scanStart(scanId):
    return render_template('DevelopmentSec.html', scanId=scanId)

@app.route('/darkJoe')
@app.route('/darkjoe')
@app.route('/dj')
def darkJoe():
    return render_template('index.html')

##################################################
#       Login test Seiten
##################################################
#
# helper.db sind die Datenbankzugriffe und anlege Scripte für login
# die __init__ muss noch ünerarbeitet werden und bei dem howto
# https://pythonspot.com/login-authentication-with-flask/
# in zeile "python tabledef.py" weiter machen
#
#


@app.route('/logon')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')

    else:
        return 'Hello Boss! <a href="/logout">Logout</a>'


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True

    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0')
    #readPropFiles.readPropFiles()
    helper.db.createDB
    helper.generateLink.genLink("abaa")