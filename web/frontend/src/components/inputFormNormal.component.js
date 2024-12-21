import React from "react";
import '../assets/css/inputFormNormal.css';
import InputFormPassWord from "./inputFormPassword.component";

export default function InputFormNormal({
    label = '',
    placeholder = '',
    error = false,
    errorMessage='',
    onChange = () => {}
}) {


    return (
       
        <div className="input-form-normal-wraper">
            <div className="input-form-normal-container">
                <InputFormPassWord 
                label={label}
                placeholder={placeholder}
                type="text"
                error={error}
                errorMessage={errorMessage}
                onChange={onChange}
                />
            </div>
        </div>
        
        
    );
}
