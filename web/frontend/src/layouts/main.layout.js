import React from 'react';
import Sidebar from '../components/sidebar.component';
import NavbarHomePage from '../components/navbarHomePage.component';
export default function MainLayout({ children }) {
    return (
        <>
            <NavbarHomePage />
            <div className='main-container d-flex'>
                <Sidebar />
                <div className='secondary-container pb-5'>
                  {children}
                </div>
            </div>
        </>
    );
}
