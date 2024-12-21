import React from 'react';
import '../assets/css/avatarAccount.css';
import Avatar from './avatar.component';

export default function AvatarAccount({ studentName = 'A', MSSV }) {

    return (
        <span className='avatar-account-container font-family-regular'>
            <Avatar 
                studentName={studentName}
                MSSV={MSSV}
            />
        </span>
    );
}