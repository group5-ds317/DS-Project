import React from "react";
import '../assets/css/textInput&Label.css';
import TextInput from "./textInput.component";

export default function TextInputLabel({
    label = '',
    placeholder = '',
    defaultValue = '',
    type = 'text',
    width = '345px',
    onChange=()=>{}
}) {

    return (
        <div className="text-input-label-container" style={{ width }}>

            {label && <label className="label font-family-semibold">{label}</label>}

            <div className="text-input-label" >
                <TextInput
                    type={type}
                    width={{ width }}
                    placeholder={placeholder}
                    defaultValue={defaultValue}
                    onChange={onChange}
                />
            </div>
        </div>
    );
}


