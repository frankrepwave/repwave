import React from 'react'
import './Navbar.css';
import profile from '../../assets/images/profile.svg';
import team from '../../assets/images/team.svg';
import suitcase from '../../assets/images/suitcase.svg';
import library from '../../assets/images/library.svg';
import templates from '../../assets/images/templates.svg';



export default function Navbar() {
  /* const navItems = [
    { name: 'Team and Themes', iconClassName: 'team-icon', icon: team },
    { name: 'Deal Room', iconClassName: 'suitcase-icon', icon: suitcase },
    { name: 'My Library', iconClassName: 'library-icon', icon: library },
    { name: 'Templates/Workflows', iconClassName: 'templates-icon, icon: templates' }
  ]; */

  return (
    <nav className="navbar">
      <div className="profile-section">
        <img src ={profile} className="profile-icon"/>
        <span className="profile-name">Edwin Saraccini</span>
      </div>
      <ul className="nav-list">
        <li className="nav-item">
          <img src={team} className="team-icon" alt="Team"/>
          <span>Team and Themes</span>
        </li>
        <li className="nav-item">
          <img src={suitcase} className="suitcase-icon" alt="Deal Room"/>
          <span>Deal Room</span>
        </li>
        <li className="nav-item">
          <img src={library} className="library-icon" alt="Library"/>
          <span>My Library</span>
        </li>
        <li className="nav-item">
          <img src={templates} className="templates-icon" alt="Templates"/>
          <span>Templates/Workflows</span>
        </li>
      </ul>
    </nav>
  );
}