class TrainingSystemAPI {
    static getTrainingSystem(TrainingSystemId) {
        return fetch(
            `http://localhost:8000/get-training-system?training_system_id=${TrainingSystemId}`, 
            {
                method: "GET",
                mode: "cors"
            }
        )
    }
}

export default TrainingSystemAPI