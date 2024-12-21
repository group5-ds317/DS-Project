import React from 'react';
import '../assets/css/editModal.css';
import Button from './button.component';


export default function DetailedModel({ isOpen, onClose, title, data }) {
    return isOpen ? (
        <div className="modal-overlay">
            <div className="modal-container w-50">
                <p className='font-family-semibold primary-color'>{title}</p>
                <div className='d-flex flex-column align-items-start'>
                    {
                        Object.entries(data).map(([key, value]) => (
                            <div className='font-family-semibold text-wrap'>{key}: <span className='font-family-regular text-wrap'>{value}</span></div>
                        ))
                    }
                </div>
                <div className="modal-actions">
                    <Button onClick={onClose} type='warning'>Đóng</Button>
                </div>
            </div>
        </div>
    ) : null;
}