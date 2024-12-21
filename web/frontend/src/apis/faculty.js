class FacultyAPI {
    static getFaculty(facultyId) {
        return fetch(
            `http://localhost:8000/get-faculty?faculty_id=${facultyId}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }
}

export default FacultyAPI