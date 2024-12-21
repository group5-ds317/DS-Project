import React, { useState } from "react";
import { Table } from "antd";
import Button from "./button.component";
import '../assets/css/list.css';

export default function List({ list, listTitle, emptyMessage }) {
    const [sectionIndex, setSectionIndex] = useState(0)

    const emptyList = (emptyMessage) => (
        <div className="empty-list-container">
            <p className="font-family-regular empty-list-message">{emptyMessage}</p>
        </div>
    )

    const listNavbar = (sections) => (
        <div className="list-navbar-container font-family-semibold">
            {
                sections.map((section, index) => (
                    <div
                        key={'section-' + index} 
                        className={`list-section ${sectionIndex === index ? 'primary-color' : 'primary-disabled-color'}`}
                        onClick={() => {
                            setSectionIndex(index);
                        }}
                    >
                        {section}
                    </div>
                ))
            }
        </div>
    )

    return (
        <>
            <div className="list-container">
                <div className="list-title font-family-semibold">
                    {listTitle}
                </div>
                {
                    (list === undefined || list.length === 0) ? 
                    emptyList(emptyMessage) :
                    <>
                        {listNavbar(list.sections)}
                        <Table 
                            key={sectionIndex}
                            className="list"
                            sticky={true}
                            columns={list.columns[sectionIndex]}
                            dataSource={list.data[sectionIndex]}
                            locale={{
                                emptyText: 'Danh sách trống',
                            }}
                        />
                    </> 
                }
            </div>
        </>
    )
}
