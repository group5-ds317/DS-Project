import React from 'react'
import '../assets/css/button.css'

const handleClickDefault = () => {}
const handleMouseEnterDefault = () => {}
const handleMouseLeaveDefault = () => {}

export default function Button({ 
    type='primary', 
    size='small', 
    status='active', 
    onClick=handleClickDefault, 
    onMouseEnter=handleMouseEnterDefault,
    onMouseLeave=handleMouseLeaveDefault,
    children 
}) {
    let classNameList = [
        'button',
        'font-family-semibold'
    ]

    switch(type) {
        case 'primary':
            classNameList.push("primary-button")
            break
        case 'secondary':
            classNameList.push("secondary-button")
            break
        case 'warning':
            classNameList.push("warning-button")
            break
        case 'success':
            classNameList.push("success-button")
            break
        case 'premium':
            classNameList.push("premium-button")
            break
        default:
            classNameList.push("primary-button")
            break
    }

    switch(size) {
        case 'small':
            classNameList.push("small-button")
            break
        case 'large':
            classNameList.push("large-button")
            break
        case 'extra-large':
            classNameList.push("extra-large-button")
            break
        default:
            classNameList.push("small-button")
            break
    }

    switch(status) {
        case 'active':
            break
        case 'disabled':
            classNameList.push("disabled-button")
            break
        default:
            break
    }



    return (
        <>
            <div 
                className={classNameList.join(" ")} 
                onClick={onClick}
                onMouseEnter={onMouseEnter}
                onMouseLeave={onMouseLeave}
            >
                {children}
            </div>
        </>
    )
}