class MajorAPI {
    static getMajor(majorId) {
        return fetch(
            `http://localhost:8000/get-major?major_id=${majorId}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }
}

export default MajorAPI