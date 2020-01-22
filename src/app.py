import os
from pyoidc_redis_session_backend import RedisSessionBackend
from flask import Flask, flash, session, redirect, render_template, url_for, request
from flask_session import Session
from config import OIDC_SERVER_URL, OIDC_CLIENT_ID, OIDC_CLIENT_SECRET, SESSION_SECRET_KEY, SESSION_TYPE, SESSION_REDIS_HOST, SESSION_REDIS_PORT, SERVER_ADDRESS
from oic.oic.consumer import Consumer
from oic.utils.authn.client import ClientSecretBasic, ClientSecretPost

from oic.utils.sdb import DictSessionBackend
from oic.utils.http_util import Redirect
import redis
from oic.exception import AccessDenied

app = Flask(__name__)
app.config["SECRET_KEY"] = SESSION_SECRET_KEY
redisClient = redis.Redis(SESSION_REDIS_HOST, SESSION_REDIS_PORT)

if(SESSION_TYPE == "redis"):
    print("Using Redis as session storage")
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redisClient
else:
    print("Using filesystem as session storage")
    app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

backend = RedisSessionBackend(redisClient)

consumer = Consumer(backend, {
    "authz_page": "/auth/callback",
    "response_type": "code",
},
    client_config={
    "client_id": OIDC_CLIENT_ID,
    "client_authn_method": {
        'client_secret_post': ClientSecretPost,
        'client_secret_basic': ClientSecretBasic
    }
})
consumer.provider_config(OIDC_SERVER_URL)
consumer.set_client_secret(OIDC_CLIENT_SECRET)


@app.route("/auth", methods=["GET"])
def auth():
    state, url = consumer.begin(
        scope="openid email", response_type="code", use_nonce=True, path=SERVER_ADDRESS)
    session["state"] = state
    return Redirect(url)


@app.route("/auth/callback", methods=["GET"])
def auth_callback():
    try:
        aresp, atr, idt = consumer.parse_authz(
            query=request.query_string.decode("utf-8"))
        assert aresp["state"] == session["state"]
        consumer.complete(state=aresp["state"])
        flash("You have been logged in", "success")
    except AssertionError:
        flash("Error", "error")
    return redirect(url_for("index"))

@app.route("/auth/logout", methods=["GET"])
def logout():
    try:
        consumer.end_session()
        session.pop("state")
        flash("You have been logged out")
    except:
        flash("Error logging out", "error")
    return redirect(url_for("index"))


@app.route("/", methods=["GET"])
def index():
    try:
        data = consumer.get_user_info(state=session["state"])
        return render_template("index.html", loggedIn=True, data=data)
    except AccessDenied:
        session.pop("state")
        return render_template("index.html", loggedIn=False)
    except KeyError:
        return render_template("index.html", loggedIn=False)
    


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="Page not found"), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)