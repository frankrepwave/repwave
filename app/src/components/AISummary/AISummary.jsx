import React, { useState, useEffect } from 'react';
import './AISummary.css'; 
import AIChatBox from '../AIChatBox/AIChatBox';

const AISummary = ({ show, onClose }) => {
    if (!show) {
    return null;
  }
  const containerClasses = show ? "ai-summary open" : "ai-summary";


  return (
    <>
    <div className="ai-summary-overlay" onClick={onClose}></div>
    <div className={containerClasses}>
        <div className='header'>
            <h2>Header</h2>
        <button onClick={onClose} className="close-btn">Close</button>
        </div>
        <div className='AI-container'>
            <div className='meeting-summary'>
            <p>Detailed Summary with Dates and Mutual Agreed Action Items:
                Rep's Accountabilities for the Next Week:
                Disney and Salters Account Focus:
                Disney: Prepare for QBR, strategize on renewal and upselling (Renewal due in July).
                Salters: Address the contract out clause issue and prepare for January QBR. The contract is invoiced in March with an expected increase to $58K.
                Enhanced Outreach:
                Target: 50 contacts in morning and evening sessions. Aim to reach 100 daily contacts starting immediately.
                QBR Preparation Improvement:
                Utilize Salesforce for efficient QBR preparation, learning from teammate Erica as soon as possible.
                Strategic Review of Upcoming Renewals:
                Review accounts with renewals in the next six months, starting this week.
                Rep's Action Items:
                Accurate Account Detail Confirmation:
                Confirm Disney and Salters' renewal dates and devise specific strategies by the end of the week.
                QBR Preparation Enhancement:
                Aim to create more impactful QBRs, starting with the next scheduled QBR.
                Outreach Productivity:
                Reach a daily target of 100 contacts to enhance pipeline development, beginning immediately.
                Leadership Development:
                Increase participation in team meetings and lead discussions, starting from the next team meeting.
                Manager's Action Items:
                Strategic Support:
                Provide insights for refining strategies for Disney and Salters by the end of the week.
                Assistance in QBR Preparations:
                Help with efficient QBR preparation, scheduling a session to go over Salesforce functionalities within the next two days.
                Monitoring Outreach Efforts:
                Keep track of the rep's outreach progress, providing feedback in the next one-on-one meeting.
                Facilitating Leadership Opportunities:
                Create opportunities for the rep to showcase leadership abilities, starting from the next team meeting.
                Deal Discussion Summary and Forecast:
                Disney: Renewal in July, potential value at $75K. Strategies for renewal and upselling need clarity in the next QBR.
                Salters: Renewal in March, estimated increase to $58K. January QBR planned to discuss contract rewrite.
                General Call Summary:
                The meeting predominantly focused on renewal strategies for key accounts and improving outreach activities. Discussions on personal development and leadership were also prominent. The rep was advised to enhance proactive strategies and efficiency in QBR preparations.
                General Manager Feedback:
                Emphasized the need for better account detail understanding, proactive renewal strategies, and increased outreach activities. Encouraged the rep to take leadership roles and manage personal development effectively.
                Mutual Agreed Plan with Timeline Expectations:
                By End of This Week:
                Rep to confirm renewal dates for Disney and Salters and begin formulating specific strategies.
                Manager to provide strategic insights for both accounts.
                Rep to increase outreach efforts to 100 contacts per day.
                Next Team Meeting:
                Rep to participate more actively and lead a discussion segment.
                Next QBR with Disney:
                Rep to present a refined and impactful QBR, with the manager's guidance in preparation.
                Within Two Days:
                Manager to assist rep in learning Salesforce functionalities for QBR preparation.
                Next One-on-One Meeting:
                Review progress on outreach efforts and discuss further strategies for key accounts.
                January QBR for Salters:
                Prepare for discussion on contract rewrite and address the out clause issue.
                Ongoing:
                Rep to continue working on leadership development and personal growth within the team.
                This detailed summary and mutual action plan provide a comprehensive overview of the meeting's outcomes and set clear expectations with specific timelines for both the rep and the manager.
                </p>
            </div>
            <AIChatBox />
        </div>
        <div className='footer'>
            <p>Footer</p>
        </div>
    </div>
    </>
  );
};

export default AISummary;
