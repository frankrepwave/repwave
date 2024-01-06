import json
import os

from flask import Flask, render_template, request, send_from_directory
from markupsafe import escape

import src.dao as DAO
from src.ai import process_meeting_summary
from src.model.MeetingTemplate import MeetingTemplate

app = Flask(__name__,
    static_folder='app/build',
    template_folder='templates'
)

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route("/page/my-library")
def my_library():
    """My Library"""
    return render_template('my_library.html')

@app.route("/page/my-reps")
def my_reps():
    """My Reps"""
    return render_template('my_reps.html')

@app.route("/page/deal-room")
def deal_room():
    """Deal Room"""
    return render_template('deal_room.html')

@app.route("/page/legacy")
def legacy():
    """Legacy Page"""
    return render_template('legacy.html')

@app.get("/api/helloworld")
def hello():
    return "hellow world"

@app.get("/api/get_all_users_for_manager")
def get_all_users_for_manager():
    company_id = request.args.get('company_id')
    manager_user_id = request.args.get('user_id')
    all_users = DAO.get_all_users_for_manager(company_id=company_id, manager_user_id=manager_user_id)
    return all_users

@app.get("/api/generate_meeting_summary")
def generate_meeting_summary():
    """Generate Meeting Summary"""
    
    print(request.args.get('templateParam'))
    if request.args.get('templateParam') == 'StandardTemplate':
        template_file = "static/meeting_templates/TestMeetingTemplate.json"
    else:
        template_file = ""
    with open(template_file, 'r') as f:
        json_data = json.load(f)
        org_name = json_data['org_name']
        outcomes = json_data['outcomes']
        glossary = json_data['glossary']
        meeting_template = MeetingTemplate(org_name, outcomes, glossary)
        # additional_information = """
        # Nayla is the Sales Director at an HR research advisory firm that provides leaders with practical information and applicable skills through comprehensive training resources and leadership development programs. 
        # Client pay a membership to access advisors and the McLean research portal/content. 
        # Nayla is Manager. 
        # Edwin is the account manager with sales targets on new accounts, growth on current accounts managed, and servicing current accounts.
        # Agenda for the meeting (30-45 minutes):
        # Forecast review - walk me through your gap for December?
        # How are your accounts looking for Q3 and Q4?
        # Risks?
        # Quota discussion.
        # Want to talk about MCV and revenue for the month.
        # Rep should focus on deals they have and talk through strategy instead of the above details.
        # Everything above should be 10-15 minutes.
        # Talk about how last week went.
        # """
        additional_information = request.form.get("additional_information")
        return process_meeting_summary(
            transcript_filepath="test_data/transcript.txt",
            meeting_template=meeting_template,
            additional_information=additional_information
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run(use_reloader=True, port=5000, threaded=True)