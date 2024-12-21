import React, { useState } from 'react';
import '../assets/css/editModal.css';
import TextInputLabel from './textInput&Label.component';
import Button from './button.component';


export default function EditModal({ isOpen, onClose, title, label, value, onSave, type }) {
    // Luôn khởi tạo trạng thái từ giá trị prop `value`
    const [inputValue, setInputValue] = useState(() => value);

    // Render modal nếu đang mở
    return isOpen ? (
        <div className="modal-overlay">
            <div className="modal-container">
                <p className='font-family-semibold primary-color'>{title}</p>
                <TextInputLabel
                    label={label}
                    defaultValue={value} // Gán giá trị từ state
                    type={type}
                    onChange={(e) => setInputValue(e.target.value)} // Cập nhật state khi người dùng nhập
                />
                <div className="modal-actions">
                    <Button onClick={onClose} type='warning'>Hủy</Button>
                    <Button onClick={() => onSave(inputValue)} type='success'>Lưu</Button>
                </div>
            </div>
        </div>
    ) : null;
}
