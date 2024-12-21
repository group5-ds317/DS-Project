class GroupCourseTypeAPI {
    static getGroupCourseType(groupCourseTypeId) {
        return fetch(
            `http://localhost:8000/get-group-course-type?group_course_type_id=${groupCourseTypeId}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }
}

export default GroupCourseTypeAPI