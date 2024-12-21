import React, { useState, useEffect } from 'react'
import '../assets/css/sidebar.css'

import homeIcon from '../assets/img/home.svg'
import homeBlueIcon from '../assets/img/home-blue.svg'
import accountIcon from '../assets/img/account.svg'
import accountBlueIcon from '../assets/img/account-blue.svg'

const clickToNavigate = (type) => {

    switch (type) {
        case 'home':
            window.location.assign('/')
            break;
        case 'account':
            window.location.assign('/account')
            break;
        default:
            window.location.assign('/')
            break;
    }
}

const sidebarItem = (name, type='home', mode='default', onMouseEnter, onMouseLeave) => {

    let icon = null
    switch (type) {
        case 'home':
            icon = mode !== 'default' ? homeBlueIcon : homeIcon
            break;
        case 'account':
            icon = mode !== 'default' ? accountBlueIcon : accountIcon
            break;
        default:
            icon = mode !== 'default' ? homeBlueIcon : homeIcon
            break;
    }

    return (
        <>
            <div 
                className='sidebar-item d-flex flex-row align-items-center' 
                onClick={() => clickToNavigate(type)} 
                onMouseEnter={() => onMouseEnter(type)} 
                onMouseLeave={() => onMouseLeave(type)}
            >
                <div className='sidebar-item-icon'>
                    <img src={icon} alt='sidebar-item-con' />
                </div>
                <div className={`sidebar-item-name font-family-regular ${mode !== 'default' ? 'primary-color' : ''}`}>{name}</div>
            </div>
        </>
    )
}

export default function Sidebar() {
    const [selected, setSelected] = useState({
        'home': false,
        'account': false
    })

    const [hover, setHover] = useState({
        'home': false,
        'account': false,
    })

    useEffect(() => {
        switch(window.location.pathname) {
            case '/':
                setSelected({
                    'home': true,
                    'exam': false,
                    'history': false,
                    'account': false,
                    'settings': false,
                    'forum': false
                })
                break;
            case '/account':
                setSelected({
                    'home': false,
                    'exam': false,
                    'history': false,
                    'account': true,
                    'settings': false,
                    'forum': false
                })
                break;
        }
    }, [window.location.pathname])

    const handleMouseEnter = (type) => {
        setHover((prevHover) => ({
            ...prevHover,
            [type]: true,
        }))
    }

    const handleMouseLeave = (type) => {
        setHover((prevHover) => ({
            ...prevHover,
            [type]: false,
        }))
    }

    return (
        <>
            <div className='sidebar col-2 foreground-color'>
                <div className='sidebar-item-list d-flex flex-column align-items-center'>
                    {sidebarItem('Trang chủ', 'home', selected['home'] || hover['home'] ? 'selected' : 'default', handleMouseEnter, handleMouseLeave)}
                    {sidebarItem('Sinh viên', 'account', selected['account'] || hover['account'] ? 'selected' : 'default', handleMouseEnter, handleMouseLeave)}
                </div>
            </div>
        </>
    )
}