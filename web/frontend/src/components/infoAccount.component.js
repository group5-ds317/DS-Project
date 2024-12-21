import React from 'react';
import '../assets/css/infoAccount.css';

export default function InforAccount({ 
    title = '', 
    value = '',
    colorIcon = '',
    icon: IconComponent,
    type = 'text',
    onEdit = null
}) {
    // Xử lý hiển thị giá trị
    const displayValue = type === 'password' ? '•'.repeat(value.length) : value || 'Chưa có thông tin';

    return (
        <span className='infor-account-container font-family-regular'>
            <span className='title-container font-family-semibold'>
                {IconComponent && <IconComponent className="icon" color={{ colorIcon }} />}
                <p>{title}</p>
            </span>
            <span className='value-container'>{displayValue}</span>
            {
                onEdit ?
                <span className='link-container'>
                    <a
                        href="#"
                        onClick={(e) => {
                            e.preventDefault(); // Ngăn hành vi mặc định
                            onEdit(); // Gọi callback khi nhấn
                        }}
                    >
                        {value ? 'Chỉnh sửa' : 'Thêm'}
                    </a>
                </span> :
                null
            }
        </span>
    );
}
