import React from 'react';
import '../assets/css/avatar.css';

function Avatar({ studentName="A", MSSV }) {
   
    return (
        <div className="avatar-container font-family-regular">
            <div className="avatar">
                <span>{studentName.charAt(0).toUpperCase()}</span>
            </div>
            <div className="account-info">
                <div className="account-studentName font-family-semibold">{studentName + " - " + MSSV || "StudentName"}</div>
            </div>
        </div>
    );
}

export default Avatar;
