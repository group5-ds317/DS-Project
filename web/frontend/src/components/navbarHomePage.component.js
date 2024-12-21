import React from 'react';
import { useNavigate } from "react-router-dom";
import '../assets/css/navbarHomePage.css';

import Button from './button.component';
import logoIcon from '../assets/img/logo.svg'

import { useAuth } from '../context/authentication.context';

const NavbarHomePage = () => {
    const navigate = useNavigate()
    const { MSSV } = useAuth()

    return (
        <div className='navbar-homepage-container foreground-color'>
            <img src={logoIcon} className='logo-icon' onClick={() => navigate("/")}/>
            <div className='navbar-homepage-header'>
                {
                    MSSV ?
                    <Button 
                        type='secondary' 
                        size='large' 
                    >
                        Hi, sinh viên UIT
                    </Button> :
                    <Button 
                        type='secondary' 
                        size='large' 
                        onClick={() => navigate("/login")}
                    >
                        Đăng nhập
                    </Button>
                }
            </div>
        </div>
    );
  };
  
export default NavbarHomePage;