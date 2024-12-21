import React, { useState } from "react";
import '../assets/css/inputFormPassword.css';
import { FaRegEye } from "react-icons/fa";
import { FaRegEyeSlash } from "react-icons/fa";

export default function InputFormPassWord({
    label = 'Mật khẩu',
    placeholder = 'Nhập mật khẩu của bạn',
    defaultValue = '',
    type = '', 
    width = '361px',
    error = false,
    errorMessage = 'Mật khẩu không hợp lệ',
    onChange = () => {}
}) {
    const [isPasswordVisible, setIsPasswordVisible] = useState(false);

    const togglePasswordVisibility = () => setIsPasswordVisible(!isPasswordVisible);

    const inputType = type || (isPasswordVisible ? "text" : "password");

    return (
        <div className="input-form-password-wraper" style={{ width }}>
            {label && <label className="input-form-password-label font-family-semibold">{label}</label>}
            <div className="input-form-password-container" style={{ width }}>
                <input
                    type={inputType}
                    defaultValue={defaultValue}
                    placeholder={placeholder}
                    onChange={onChange}
                    className="input-form-password font-family-regular"
                />
                {type === "" && (
                    <span
                        className="toggle-password-icon"
                        onClick={togglePasswordVisibility}
                    >
                        {isPasswordVisible ? <FaRegEye /> : <FaRegEyeSlash />}
                    </span>
                )}
            </div>
            {error && <p className="error-message font-family-light">{errorMessage}</p>}
        </div>
    );
}
