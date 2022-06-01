import React from "react";
import useAuth from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";
import useCustomForm from "../../hooks/useCustomForm";
import axios from "axios";

let initialValue = {
    name: ""
};

const CreateLeaguePage = () => {
    const [user, token] = useAuth();
    const navigate = useNavigate();
    const [formData, handleInputChange, handleSubmit] = useCustomForm(initialValue, postNewLeague)

    async function postNewLeague(){
        try {
            let response = await axios.post("http://127.0.0.1:8000/api/leagues/", formData, {
                headers: {
                    Authorization: 'Bearer ' + token
                }
            })
            navigate("/createTeamManager")
        } catch (error) {

        }
    }

    return (
        <div className="container">
            <form className="form" onSubmit={handleSubmit}>
                <label>
                    Name:{" "}
                    <input
                       type="text"
                       name="name"
                       value={formData.name}
                       onChange={handleInputChange}
                    />
                </label>
                <button>Create League</button>
            </form>
        </div>
    )


}

export default CreateLeaguePage;