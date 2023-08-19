from config import REDIRECT_URL_LEAGUE,REDIRECT_URL_COUNTER,OAUTH_URL_LEAGUE,OAUTH_URL_COUNTER,CLIENT_SECRET
from flask import Flask,render_template, request,session
#from flask_mysqldb import MySQL
from zenora import APIClient
import data
import os

app = Flask(__name__)
app.secret_key = '1hello2'


app.config['MYSQL_HOST'] = 'containers-us-west-120.railway.app'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0en6pbybktiIE41UpRnu'
app.config['MYSQL_PORT'] = 6415
app.config['MYSQL_DB'] = 'railway'

token = data.getToken()
client = APIClient(token,client_secret=CLIENT_SECRET)


@app.before_request
def before_request():
    data.createTables()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/counterPage")
def counter():
    return render_template('counterPage.html', oauth_uri=OAUTH_URL_COUNTER)


@app.route("/leaguePage")
def league():
    return render_template('leaguePage.html', oauth_uri=OAUTH_URL_LEAGUE)


@app.route("/oauth/callback/league")
def callbackLeague():

    try:
        code = request.args['code']
        access_token = client.oauth.get_access_token(code, redirect_uri=REDIRECT_URL_LEAGUE).access_token
        bearer_client = APIClient(access_token, bearer=True)
        current_user = bearer_client.users.get_current_user().username
        session['current_user'] = current_user
        return render_template('league.html')

    except Exception as ex:
        return render_template('invalid.html')


@app.route("/oauth/callback/counter")
def callbackCounter():

    try:
        code = request.args['code']
        access_token = client.oauth.get_access_token(code, redirect_uri=REDIRECT_URL_COUNTER).access_token
        bearer_client = APIClient(access_token, bearer=True)
        current_user = bearer_client.users.get_current_user().username
        session['current_user'] = current_user
        return render_template('counter.html')

    except Exception as ex:
        return render_template('invalid.html')

@app.route('/registerLeague', methods=['POST', 'GET'])
def leagueRegister():

    if request.method == 'POST':
        leagueUser = request.form['leagueUser']
        walletAddress = request.form['walletAddress']
        leagueServer = request.form['leagueServer']
        discordUser = session.get('current_user')

        existing_user = data.getLeagueUser(discordUser)
        if existing_user:
            already_registered = True
            return render_template('league.html', already_registered=already_registered)

        data.insertLeagueUser(leagueUser,walletAddress,leagueServer,discordUser)
        registration_successful = True
        return render_template('league.html', registration_successful=registration_successful)

    return render_template('index.html', already_registered=False)


@app.route('/registerCounter', methods=['POST', 'GET'])
def counterRegister():

    if request.method == 'POST':
        counterUser = request.form['counterUser']
        walletAddress = request.form['walletAddress']
        counterServer = request.form['counterServer']
        discordUser = session.get('current_user')


        existing_user = data.getCounterUser(discordUser)

        if existing_user:
            already_registered = True
            return render_template('counter.html', already_registered=already_registered)

        data.insertCounterUser(discordUser,counterUser,walletAddress,counterServer)
        registration_successful = True
        return render_template('counter.html', registration_successful=registration_successful)

    return render_template('index.html', already_registered=False)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
