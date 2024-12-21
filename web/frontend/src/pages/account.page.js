import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/authentication.context";
import { FaUserEdit } from "react-icons/fa";
import { BiRename } from "react-icons/bi";
import { FaTransgender } from "react-icons/fa";
import { FaUserLock } from "react-icons/fa";
import { LuUniversity } from "react-icons/lu";
import { MdCastForEducation } from "react-icons/md";
import { FaBookReader } from "react-icons/fa";
import { BiSolidCalendar } from "react-icons/bi";
import { BiSolidCalendarEdit } from "react-icons/bi";
import '../assets/css/account.page.css'
import Swal from 'sweetalert2'
import StudentAPI from "../apis/student";
import FacultyAPI from "../apis/faculty";
import MajorAPI from "../apis/major";
import TrainingSystemAPI from "../apis/trainingSystem";

import MainLayout from "../layouts/main.layout";
import InforAccount from "../components/infoAccount.component";
import Button from "../components/button.component";
import EditModal from "../components/editModal.component";

export default function AccountPage() {
    const navigate = useNavigate()
    const { MSSV, logout, currentTerm, updateCurrentTerm } = useAuth()

    const [isModalOpen, setModalOpen] = useState(false);
    const [currentField, setCurrentField] = useState({key: "", title: "",label:"", value: "",  type:"" });
    const [accountData, setAccountData] = useState(null);

    useEffect(() => {
        handleLoadStudent()
    }, [MSSV])

    const handleLoadStudent = () => {
        StudentAPI.getStudent(MSSV)
        .then(response => response.json())
        .then(data => {
            if (data?.success) {
                Promise.all([
                    fetchFaculty(data?.data?.faculty_id),
                    fetchMajor(data?.data?.major_id),
                    fetchTrainingSystem(data?.data?.training_system_id)
                ]).then(response => {
                    if(response) {
                        setAccountData({
                            MSSV: MSSV,
                            gender: data?.data?.gender == 0 ? "Nữ" : "Nam",
                            faculty: response[0],
                            major: response[1],
                            trainingSystem: response[2],
                            startYear: data?.data?.start_year,
                            currentTerm: currentTerm
                        })
                    }
                })
                
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Lấy thông tin sinh viên thất bại",
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
                title: "Lấy thông tin sinh viên thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
        })
    }

    const fetchMajor = (majorId) => {
        if (!majorId) return null

        return MajorAPI.getMajor(majorId)
        .then(response => response.json())
        .then(data => {
            if(data?.success) {
                return data?.data?.major
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Lấy thông tin ngành học thất bại",
                    text: data?.message,
                    showConfirmButton: false,
                    timer: 1500
                })
                return null
            }
        })
        .catch(error => {
            console.error(error)
            Swal.fire({
                position: "center",
                icon: "error",
                title: "Lấy thông tin ngành học thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
            return null
        })
    } 

    const fetchFaculty = (facultyId) => {
        if (!facultyId) return null

        return FacultyAPI.getFaculty(facultyId)
        .then(response => response.json())
        .then(data => {
            if(data?.success) {
                return data?.data?.faculty
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Lấy thông tin khoa thất bại",
                    text: data?.message,
                    showConfirmButton: false,
                    timer: 1500
                })
                return null
            }
        })
        .catch(error => {
            console.error(error)
            Swal.fire({
                position: "center",
                icon: "error",
                title: "Lấy thông tin khoa thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
            return null
        })
    } 

    const fetchTrainingSystem = (trainingSystemId) => {
        if (!trainingSystemId) return null

        return TrainingSystemAPI.getTrainingSystem(trainingSystemId)
        .then(response => response.json())
        .then(data => {
            if(data?.success) {
                return data?.data?.training_system
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Lấy thông tin hệ đào tạo thất bại",
                    text: data?.message,
                    showConfirmButton: false,
                    timer: 1500
                })
                return null
            }
        })
        .catch(error => {
            console.error(error)
            Swal.fire({
                position: "center",
                icon: "error",
                title: "Lấy thông tin hệ đào tạo thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
            return null
        })
    } 

    const handleEdit = (key, title, label, value, type) => {
        setCurrentField({ key, title, label, value, type });
        setModalOpen(true);
    };

    const handleSave = (newValue) => {
        setAccountData((prev) => ({ ...prev, [currentField.key]: newValue }));
        setModalOpen(false);
    };

    const handleUpdateAccount = () => {
        updateCurrentTerm(accountData?.currentTerm)
        Swal.fire({
            position: "center",
            icon: "success",
            title: "Cập nhật kỳ học hiện tại thành công",
            showConfirmButton: false,
            timer: 1500
        })
        .then(() => {
            navigate("/")
        })
    }

    const handleLogout = () => {
        StudentAPI.logout(MSSV)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                setAccountData(null)
                Swal.fire({
                    position: "center",
                    icon: "success",
                    title: "Đăng xuất thành công",
                    showConfirmButton: false,
                    timer: 1500
                }).finally(() => {
                    logout()
                })
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Đăng xuất thất bại",
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
                title: "Đăng xuất thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
        })
    }

    return (
        <>
            <MainLayout>
                <div className="infor-account mt-5">
                    <InforAccount
                        icon={FaUserEdit}
                        label="Mã số sinh viên"
                        title="Mã số sinh viên"
                        value={accountData?.MSSV}
                        type="text"
                    />
                    <InforAccount
                        icon={FaTransgender}
                        label="Giới tính"
                        title="Giới tính"
                        value={accountData?.gender}
                        type="text"
                    />
                    <InforAccount
                        icon={LuUniversity}
                        label="Khoa đào tạo"
                        title="Khoa đào tạo"
                        value={accountData?.faculty}
                        type="text"
                    />
                    <InforAccount
                        icon={FaBookReader}
                        label="Ngành học"
                        title="Ngành học"
                        value={accountData?.major}
                        type="text"
                    />
                    <InforAccount
                        icon={MdCastForEducation}
                        label="Chương trình đào tạo"
                        title="Chương trình đào tạo"
                        value={accountData?.trainingSystem}
                        type="text"
                    />
                    <InforAccount
                        icon={BiSolidCalendar}
                        label="Năm học bắt đầu"
                        title="Năm học bắt đầu"
                        value={accountData?.startYear}
                        type="text"
                    />
                    <InforAccount
                        icon={BiSolidCalendarEdit}
                        title="Chọn Kỳ học hiện tại"
                        label="Kỳ học hiện tại"
                        type="text"
                        value={accountData?.currentTerm}
                        onEdit={() => handleEdit("currentTerm", "Chọn kỳ học hiện tại","Kỳ học hiện tại", accountData?.currentTerm, "currentTerm")}
                    />
                    {/* <InforAccount
                        icon={FaUserLock}
                        title="Đổi mật khẩu"
                        label="Mật khẩu"
                        type="password"
                        value={"......"}
                        onEdit={() => handleEdit("password", "Đổi mật khẩu","Mật khẩu", accountData?.password, "password")}
                    /> */}
                </div>
                <span
                    className="combo-button"
                >
                    <Button type="warning" size="large" onClick={handleLogout}>
                        Đăng xuất
                    </Button>
                    <Button type="primary" size="large" onClick={handleUpdateAccount}>
                        Cập nhật
                    </Button>
                </span>
            </MainLayout>
            <EditModal
                isOpen={isModalOpen}
                onClose={() => setModalOpen(false)}
                title={currentField.title} 
                label={currentField.label} 
                value={currentField.value} 
                type={currentField.type}  
                onSave={handleSave}
            />
        </>
    );
}
