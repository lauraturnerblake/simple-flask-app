from flask import Flask, render_template, request
import logging

flask_app = Flask(__name__)

#CONFIGURING LOGGING
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('application_logs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

@flask_app.route('/')
def homepage():
    return render_template("Homepage.html")

@flask_app.route('/inspiration.html')
def inspiration():
    return render_template("inspiration.html")

@flask_app.route('/about_us.html')
def about_us():
    return render_template("about_us.html")

@flask_app.route('/jobs.html')
def jobs():
    return render_template("jobs.html")

@flask_app.route("/send", methods=["POST"])
def send_email_to_signer():
    print "ahsbdjha"
    send_simple_message(request.form["email"])
    return render_template("Homepage.html")



import requests

sender = "Creative Aspirations"
domain_name = "sandboxf68c8339faad487daa4b0ea47cd2dd94.mailgun.org"
api_key = ["ba5aa485af", "0b2cea6a33", "42-72dd13eea113", "a224840d-82fc61"]

def send_simple_message(destination):
    resultt =  requests.post(
        "https://api.mailgun.net/v3/{0}/messages".format(domain_name),
        auth=("api", api_key[0][::-1]+api_key[1][::-1]+api_key[2][::-1]+api_key[3][::-1]),
        data={
            "from": "{0} <mailgun@{1}>".format(sender, domain_name),
            "to": [destination],
            "subject": "Thank you for signing up",
            "text": "Thank you for signing up to Creative Aspirations. We look forward to keeping you updated with interesting opportunities and events!"
            }
        )
    print resultt.content




logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)
