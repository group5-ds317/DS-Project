import { Checkbox, ConfigProvider } from 'antd';
import React, { useState, useEffect } from 'react';

function CheckBox({ checked: propChecked, onChange }) {
    const [checked, setChecked] = useState(propChecked || false);  // Quản lý checked nội bộ, nếu không có prop thì mặc định là false

    // Khi prop checked thay đổi, cập nhật trạng thái checked
    useEffect(() => {
        if (propChecked !== undefined) {
            setChecked(propChecked);
        }
    }, [propChecked]);

    const handleChange = (e) => {
        const newChecked = e.target.checked;

        if (onChange) {
            // Nếu có hàm onChange được truyền vào, gọi hàm đó
            onChange(newChecked);
        } else {
            // Nếu không có onChange, tự động cập nhật trạng thái checked của mình
            setChecked(newChecked);
        }
    };

    return (
        <ConfigProvider
            theme={{
                token: {
                    colorBorder: '#000',
                    colorPrimary: '#06AB66',
                    colorPrimaryBorder: '#06AB66',
                    colorPrimaryHover: '#06AB66',
                },
            }}
        >
            <div className='check-box'>
                <Checkbox
                    className="custom-checkbox"
                    checked={checked}  // Dùng trạng thái checked
                    onChange={handleChange}  // Xử lý khi thay đổi trạng thái
                />
            </div>
        </ConfigProvider>
    );
}

export default CheckBox;