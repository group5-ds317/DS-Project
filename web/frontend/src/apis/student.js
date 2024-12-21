class StudentAPI {
    static login(mssv, password) {
        return fetch(
            `http://localhost:8000/login`, 
            {
                method: "POST",
                mode: "cors",
                headers: { 
                    "Content-type": "application/json; charset=UTF-8"
                },
                body: JSON.stringify({
                    mssv: mssv || "", // Tránh null
                    password: password || ""  // Tránh null
                })
            }
        )
    }

    static logout(mssv) {
        return fetch(
            `http://localhost:8000/logout`, 
            {
                method: "POST",
                mode: "cors",
                headers: { 
                    "Content-type": "application/json; charset=UTF-8"
                },
                body: JSON.stringify({
                    mssv: mssv
                })
            }
        )
    }

    static getStudent(mssv) {
        return fetch(
            `http://localhost:8000/get-student?mssv=${encodeURIComponent(mssv)}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }

    static getRecommendedCourse(mssv, termNumber) {
        return fetch(
            `http://localhost:8000/get-recommended-course?mssv=${encodeURIComponent(mssv)}&term_number=${termNumber}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }

    static getAttendedCourse(mssv, termNumber) {
        return fetch(
            `http://localhost:8000/get-attended-course?mssv=${encodeURIComponent(mssv)}&term_number=${termNumber}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }

    static getUnAttendedCourse(mssv, termNumber) {
        return fetch(
            `http://localhost:8000/get-unattended-course?mssv=${encodeURIComponent(mssv)}&term_number=${termNumber}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }
}

export default StudentAPI