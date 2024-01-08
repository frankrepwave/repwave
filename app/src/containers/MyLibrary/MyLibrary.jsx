import React from 'react'
import Navbar from "../../components/Navbar/Navbar";
import './MyLibrary.css';
import LogsTable from "../../components/LogsTable/LogsTable";



export default function MyLibrary() {
  return (
  <div className='library-container'>
    <Navbar />
    <LogsTable />
  </div>
  )
}
