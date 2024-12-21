import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Swal from 'sweetalert2';
import '../assets/css/login.page.css';

import { useAuth } from "../context/authentication.context";
import StudentAPI from "../apis/student";

import InputFormNormal from "../components/inputFormNormal.component";
import InputFormPassWord from "../components/inputFormPassword.component";
import imgLoginPage from "../assets/img/login.png";
import Button from "../components/button.component";

export default function LoginPage() {
    const navigate = useNavigate();
    const { login } = useAuth()
    const [MSSV, setMSSV] = useState('');
    const [password, setPassword] = useState('');
    const [MSSVError, setMSSVError] = useState(false);
    const [passwordError, setPasswordError] = useState(false);

    const handleLogin = () => {
        StudentAPI.login(MSSV, password)
        .then(response => response.json())
        .then(data => {
            if (data?.success) {
                Swal.fire({
                    position: "center",
                    icon: "success",
                    title: "Đăng nhập thành công",
                    showConfirmButton: false,
                    timer: 1500
                })
                .then(() => {
                    login(data?.data?.mssv)
                    navigate("/account")
                })
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Đăng nhập thất bại",
                    text: data?.message,
                    showConfirmButton: false,
                    timer: 1500
                })
            }
        })
        .catch(error => {
            console.error(error)
            Swal.fire({
                position: "center",
                icon: "error",
                title: "Đăng nhập thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
        })
    };
    
    return (
        <div className='login-page-container'>
            <div className="login-left">
                <img src={imgLoginPage} alt='Login Illustration' className='login-image' />
            </div>
                
            <div className="login-right">
                <p className="title_login font-family-semibold">Đăng nhập</p>
                
                <InputFormNormal 
                    placeholder="Mã số sinh viên"
                    value={MSSV} 
                    onChange={(e) => {
                        const inputValue = e.target.value;
                        setMSSV(inputValue);

                        if (inputValue.trim()) {
                            setMSSVError(false);
                        }
                    }}
                    error={MSSVError} 
                    errorMessage="Vui lòng nhập mã số sinh viên."
                />            
                <InputFormPassWord
                    label=" "
                    value={password}
                    onChange={(e) => {
                        setPassword(e.target.value);
                        setPasswordError(false);
                    }}
                    error={passwordError}
                    errorMessage="Vui lòng nhập mật khẩu."
                /> 
                <div className="login-button-space"></div>
                <Button 
                    type="primary" 
                    size="large" 
                    status="active" 
                    onClick={handleLogin}
                >
                    Đăng nhập
                </Button>
            </div>
        </div>
    );
}
