import React, { useState, useEffect } from 'react';
import './LogsTable.css'; 
import profilePic from '../../assets/images/edwinImg.jpg'
import editIcon from '../../assets/images/editIcon.svg'; 
import trash from '../../assets/images/deleteIcon.svg'; 
import documentIcon from '../../assets/images/documentIcon.svg';
import AISummary from '../AISummary/AISummary';

export default function LogsTable() {
    //const [teamLogs, setTeamLogs] = useState([]);
    const [showSummary, setShowSummary] = useState(false);


    /* useEffect(() => {
      fetch('/api/team-logs')// Replace '/api/team-logs' with the actual endpoint
        .then(response => response.json())
        .then(data => setTeamLogs(data))//replace this give the JSON structure from the backend 
        .catch(error => console.error('Error fetching team logs:', error));
    }, []); */


    const handleDocumentIconClick = () => {
      setShowSummary(true);
    };

    const handleClose = () => {
      setShowSummary(false);
    };

    return (
    <>
        <div className="logs-table-container">
            <h2 className='logs-title'>Your Team</h2>
          <table className="logs-table">
            <thead>
              <tr>
                <th>Name (select for export)</th>
                <th>Status</th>
                <th>Date of meeting</th>{/* new Date(review.created_at).toLocaleString() */}
                <th>Workflow Used</th>
                <th>Themes/Highlights</th>
                <th>AI Summary</th>
                <th>Actions</th> 
              </tr>
            </thead>
            <tbody>
            <tr>
                  <td className='name-td'>
                    <input type="checkbox" className=""></input>
                    <img src={profilePic} alt="Profile" className="profile-pic" />
                    Edwin
                  </td>
                  <td>
                    Ready
                  </td>
                  <td>Jan 14 2002</td>{/* new Date(review.created_at).toLocaleString() */}
                  <td>Standard 1on1</td>
                  <td>Product, Training</td>
                  <td>
                    <button className="ai-summary-button" onClick={handleDocumentIconClick}>
                      <img src={documentIcon} alt="AI Summary" />
                    </button>
                  </td>
                  <td>
                    <button className="delete-button">
                      <img src={trash} alt="Delete" />
                    </button>
                    <button className="edit-button">
                      <img src={editIcon} alt="Edit" />
                    </button>
                  </td>
                </tr>

                <tr>
                  <td className='name-td'>
                    <input type="checkbox" name=""></input>
                    <img src={profilePic} alt="Profile" className="profile-pic" />
                    Edwin
                  </td>
                  <td>
                    Ready
                  </td>
                  <td>Jan 14 2002</td>
                  <td>Deal Focus Workflow</td>
                  <td>PM, Product, Risk...</td>
                  <td>
                    <button className="ai-summary-button">
                      <img src={documentIcon} alt="AI Summary" />
                    </button>
                  </td>
                  <td>
                    <button className="delete-button">
                      <img src={trash} alt="Delete" />
                    </button>
                    <button className="edit-button">
                      <img src={editIcon} alt="Edit" />
                    </button>
                  </td>
                </tr>

                <tr>
                  <td className='name-td'>
                    <input type="checkbox" className=""></input>
                    <img src={profilePic} alt="Profile" className="profile-pic" />
                    Edwin
                  </td>
                  <td>
                    Ready
                  </td>
                  <td>Jan 14 2002</td>{/* new Date(review.created_at).toLocaleString() */}
                  <td>Standard 1on1</td>
                  <td>Product, Training</td>
                  <td>
                    <button className="ai-summary-button" onClick={handleDocumentIconClick}>
                      <img src={documentIcon} alt="AI Summary" />
                    </button>
                  </td>
                  <td>
                    <button className="delete-button">
                      <img src={trash} alt="Delete" />
                    </button>
                    <button className="edit-button">
                      <img src={editIcon} alt="Edit" />
                    </button>
                  </td>
                </tr>



                <tr>
                  <td className='name-td'>
                    <input type="checkbox" name=""></input>
                    <img src={profilePic} alt="Profile" className="profile-pic" />
                    Edwin
                  </td>
                  <td>
                    Ready
                  </td>
                  <td>Jan 14 2002</td>
                  <td>Deal Focus Workflow</td>
                  <td>PM, Product, Risk...</td>
                  <td>
                    <button className="ai-summary-button">
                      <img src={documentIcon} alt="AI Summary" />
                    </button>
                  </td>
                  <td>
                    <button className="delete-button">
                      <img src={trash} alt="Delete" />
                    </button>
                    <button className="edit-button">
                      <img src={editIcon} alt="Edit" />
                    </button>
                  </td>
                </tr>

              
            </tbody>
          </table>
          {/* teamLogs.map((log, index) => (
                <tr key={index}>
                  <td>
                    <img src={log.profilePic} alt="Profile" className="profile-pic" />
                    {log.name}
                  </td>
                  <td>
                    <img src={statusIcon} alt="Status" className="status-icon" />
                    {log.status}
                  </td>
                  <td>{log.dateOfMeeting}</td>
                  <td>{log.workflowUsed}</td>
                  <td>{log.themes.join(', ')}</td>
                  <td>
                    <button className="ai-summary-button">
                      <img src={documentIcon} alt="AI Summary" />
                    </button>
                  </td>
                  <td>
                    <button className="delete-button">
                      <img src={trash} alt="Delete" />
                    </button>
                    <button className="edit-button">
                      <img src={editIcon} alt="Edit" />
                    </button>
                  </td>
                </tr>
              )) */}
              
        </div>
        {showSummary && <AISummary show={showSummary} onClose={handleClose} />}
        </>
        
      );
}
