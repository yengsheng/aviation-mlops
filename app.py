from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, SelectField
import requests
import json
# from ml_service.util.env_variables import Env
# from azureml.core import Workspace
# from azureml.core.webservice import AciWebservice

app = Flask(__name__)
app.config['SECRET_KEY'] = 'someRandomKey'

# e = Env()
# ws = Workspace.get(
#     name=e.workspace_name,
#     subscription_id=e.subscription_id,
#     resource_group=e.resource_group
# )

# service_name = "aviation-service3"
# # aml_workspace = Workspace.from_config()

# service = AciWebservice(ws, service_name)
# scoring_uri = service.scoring_uri
# print(scoring_uri)

scoring_uri = "http://0ca3b4cf-5100-4a96-a794-d328dc403b55.southeastasia.azurecontainer.io/score"

def api_call(features):
    global scoring_uri
    # Two sets of data to score, so we get two results back
    data = {"data":
            [
                features
            ]
            }
    # Convert to JSON string
    input_data = json.dumps(data)

    # Set the content type
    headers = {'Content-Type': 'application/json'}

    # Make the request and display the response
    resp = requests.post(scoring_uri, input_data, headers=headers)
    print(resp)
    return(resp.text)

class AviationForm(FlaskForm):
    #InvestigationType = TextField('Investigation Type')
    InvestigationType = SelectField('Investigation Type', choices=[(2, 'Accident'), (1, 'Incident')])
    #Country = TextField('Country')
    Country = SelectField('Country', choices=[(1, 'United States'), (0, 'Outside United States')])
    #InjurySeverity = TextField('Injury Severity')
    InjurySeverity = SelectField('Injury Severity', choices=[(4, 'Fatal'), (3, 'Siruouse'), (2, 'Non-Fatal'), (1, 'Minor'), (0, 'Unavailable')])
    #AmateurBuilt = TextField('Amateur Built')
    AmateurBuilt = SelectField('Amateur Built', choices=[(1, 'Yes'), (0, 'No')])
    #NumberofEngines = DecimalField('Number of Engines')
    NumberofEngines = TextField('Number of Engines')
    FatalInjuries = TextField('Total Fatal Injuries')
    SeriousInjuries = TextField('Total Serious Injuries')
    MinorInjuries = TextField('Total Minor Injuries')
    Uninjured = TextField('Total Uninjured')
    submit = SubmitField('Submit for Prediction')

# @app.route("/", methods = ['GET', 'POST'])
# def landing():
#     global scoring_uri
#     form = APIForm()
#     if form.validate_on_submit():
#         scoring_uri = form.APILink.data
#         return redirect(url_for("index"))
#     return render_template("landing.html" , form=form)
    

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = AviationForm()
    if form.validate_on_submit():
        session['InvestigationType'] = form.InvestigationType.data
        session['Country'] = form.Country.data
        session['InjurySeverity'] = form.InjurySeverity.data
        session['AmateurBuilt'] = form.AmateurBuilt.data
        session['NumberofEngines'] = form.NumberofEngines.data
        session['FatalInjuries'] = form.FatalInjuries.data
        session['SeriousInjuries'] = form.SeriousInjuries.data
        session['MinorInjuries'] = form.MinorInjuries.data
        session['Uninjured'] = form.Uninjured.data
        return redirect(url_for("prediction"))
    return render_template("home.html" , form=form)

@app.route('/prediction')
def prediction():
    global destroyed_or_no
    result = api_call([session['InvestigationType'],
                        session['Country'],
                        session['InjurySeverity'],
                        session['AmateurBuilt'],
                        session['NumberofEngines'],
                        session['FatalInjuries'],
                        session['SeriousInjuries'],
                        session['MinorInjuries'],
                        session['Uninjured']]).strip("\\[]\"")
    print(type(result))
    return render_template('prediction.html', results=result)

if __name__ == '__main__':
    app.run()