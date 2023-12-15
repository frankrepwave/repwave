import os

from flask import Flask, render_template, request
from markupsafe import escape
from src.ai import process_meeting_summary
from src.model.MeetingTemplate import MeetingTemplate

app = Flask(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates'
)


@app.route("/")
def index():
    """Homepage"""
    return render_template('index.html')

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

@app.get("/api/generate_meeting_summary")
def generate_meeting_summary():
    """Generate Meeting Summary"""

    meeting_template = MeetingTemplate()
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
        filepath="",
        meeting_template=meeting_template,
        additional_information=additional_information
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))