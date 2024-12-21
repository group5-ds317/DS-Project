import { Checkbox, ConfigProvider } from 'antd';
import React, { useState } from 'react';

function CheckBoxWithText({ text }) {
    const [checked, setChecked] = useState(false);

    const handleChange = (checked) => {
        setChecked(checked);
    };

    return (
        <ConfigProvider
            theme={{
                token: {
                    colorBorder: '#000',
                    colorText: '#000',
                    colorPrimary: '#06AB66',
                    colorPrimaryBorder: '#06AB66',
                    colorPrimaryHover: '#06AB66',
                },
            }}
        >
            <div className='check-box-with-text'>
                <Checkbox 
                    className={`custom-check-box-with-text font-family-regular`}
                    onChange={handleChange}
                >
                    <span>{text}</span>
                </Checkbox>
            </div>
        </ConfigProvider>
    );
}

export default CheckBoxWithText;
