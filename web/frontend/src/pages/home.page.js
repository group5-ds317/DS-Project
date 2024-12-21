import React, { useState, useEffect } from "react";
import MainLayout from "../layouts/main.layout";
import List from "../components/list.component";
import DetailedModel from "../components/detailedModal.component";
import { useAuth } from "../context/authentication.context";
import StudentAPI from "../apis/student";
import Swal from "sweetalert2"

export default function HomePage() {
    const { MSSV, currentTerm } = useAuth()
    const [recommendedCourse, setRecommendedCourse] = useState(null)
    const [attendedCourse, setAttendedCourse] = useState(null)
    const [unAttendedCourse, setUnAttendedCourse] = useState(null)
    const [isModalOpen, setIsModalOpen] = useState(false)
    const [detail, setDetail] = useState(null)

    useEffect(() => {
        Promise.all([handleLoadRecommendedCourse(), handleLoadAttendedCourse(), handleLoadUnAttendedCourse()])
    }, [])

    const handleLoadRecommendedCourse = () => {
        return StudentAPI.getRecommendedCourse(MSSV, currentTerm)
        .then(response => response.json())
        .then(data => {
            if (data?.success) {
                setRecommendedCourse(data?.data?.courses?.map(course => ({
                    courseId: course?.course_id,
                    courseName: course?.course_name,
                    summary: course?.summary,
                    credit: course?.credit,
                    major: course?.major,
                    courseType: course?.course_type,
                    groupCourseType: course?.group_course_type,
                    similarityScore: course?.similarity_score
                })))
                return 1
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Truy xuất danh sách môn học khuyến nghị thất bại",
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
                title: "Truy xuất danh sách môn học khuyến nghị thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
            return null
        })
    }

    const handleLoadAttendedCourse = () => {
        return StudentAPI.getAttendedCourse(MSSV, currentTerm)
        .then(response => response.json())
        .then(data => {
            if (data?.success) {
                setAttendedCourse(data?.data?.courses?.map(course => ({
                    courseId: course?.course_id,
                    courseName: course?.course_name,
                    summary: course?.summary,
                    credit: course?.credit,
                    major: course?.major,
                    courseType: course?.course_type,
                    groupCourseType: course?.group_course_type,
                })))
                return 1
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Truy xuất danh sách môn học đã đăng ký thất bại",
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
                title: "Truy xuất danh sách môn học đã đăng ký thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
            return null
        })
    }

    const handleLoadUnAttendedCourse = () => {
        return StudentAPI.getUnAttendedCourse(MSSV, currentTerm)
        .then(response => response.json())
        .then(data => {
            if (data?.success) {
                setUnAttendedCourse(data?.data?.courses?.map(course => ({
                    courseId: course?.course_id,
                    courseName: course?.course_name,
                    summary: course?.summary,
                    credit: course?.credit,
                    major: course?.major,
                    courseType: course?.course_type,
                    groupCourseType: course?.group_course_type,
                })))
                return 1
            } else {
                Swal.fire({
                    position: "center",
                    icon: "error",
                    title: "Truy xuất danh sách môn học chưa đăng ký thất bại",
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
                title: "Truy xuất danh sách môn học chưa đăng ký thất bại",
                text: error?.message,
                showConfirmButton: false,
                timer: 1500
            })
            return null
        })
    }

    const sections = ["Môn học hệ thống khuyến nghị", "Môn học đã đăng ký", "Môn học chưa đăng ký"]
    const columns = [
        [
            {
                title: "Mã môn học",
                dataIndex: "courseId",
                key: "courseId",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Tên môn học",
                dataIndex: "courseName",
                key: "courseName",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Số tín chỉ",
                dataIndex: "credit",
                key: "credit",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Loại môn học",
                dataIndex: "courseType",
                key: "courseType",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Độ tương đồng",
                dataIndex: "similarityScore",
                key: "similarityScore",
                align: "center",
                filtered: true,
                filterSearch: true,
                render: (value) => (value * 100).toFixed(0) + "%"
            },
            {
                title: "Chi tiết",
                dataIndex: "detail",
                key: "detail",
                align: "center",
                render: (_, record) => (
                    <a 
                        className="link-effect black-color"
                        onClick={() => {
                            setIsModalOpen(true)
                            setDetail({
                                "Mã môn học": record.courseId,
                                "Tên môn học": record.courseName,
                                "Độ tương đồng": (record.similarityScore * 100).toFixed(0) + "%",
                                "Tín chỉ": record.credit,
                                "Ngành môn học": record.major,
                                "Loại môn học": record.courseType,
                                "Nhóm loại môn học": record.groupCourseType,
                                "Tóm tắt môn học": record.summary
                            })
                        }}
                    >
                        Xem chi tiết
                    </a>
                )
            }
        ],
        [
            {
                title: "Mã môn học",
                dataIndex: "courseId",
                key: "courseId",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Tên môn học",
                dataIndex: "courseName",
                key: "courseName",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Số tín chỉ",
                dataIndex: "credit",
                key: "credit",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Loại môn học",
                dataIndex: "courseType",
                key: "courseType",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Chi tiết",
                dataIndex: "detail",
                key: "detail",
                align: "center",
                render: (_, record) => (
                    <a 
                        className="link-effect black-color"
                        onClick={() => {}}
                    >
                        Xem chi tiết
                    </a>
                )
            }
        ],
        [
            {
                title: "Mã môn học",
                dataIndex: "courseId",
                key: "courseId",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Tên môn học",
                dataIndex: "courseName",
                key: "courseName",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Số tín chỉ",
                dataIndex: "credit",
                key: "credit",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Loại môn học",
                dataIndex: "courseType",
                key: "courseType",
                align: "center",
                filtered: true,
                filterSearch: true
            },
            {
                title: "Chi tiết",
                dataIndex: "detail",
                key: "detail",
                align: "center",
                render: (_, record) => (
                    <a 
                        className="link-effect black-color"
                        onClick={() => {}}
                    >
                        Xem chi tiết
                    </a>
                )
            }
        ]
    ]

    return (
        <MainLayout>
            <List
                list={{
                    sections: sections,
                    columns: columns,
                    data: [
                        recommendedCourse,
                        attendedCourse,
                        unAttendedCourse
                    ]
                }} 
                listTitle={'Danh sách môn học'} 
                emptyMessage={"Không có môn học"}
            />
            <DetailedModel 
                isOpen={isModalOpen}
                onClose={() => setIsModalOpen(false)}
                title={"Thông tin chi tiết môn học"}
                data={detail}
            />
        </MainLayout>
    )
}