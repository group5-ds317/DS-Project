class CourseTypeAPI {
    static getCourseType(courseTypeId) {
        return fetch(
            `http://localhost:8000/get-course-type?course_type_id=${courseTypeId}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }
}

export default CourseTypeAPI