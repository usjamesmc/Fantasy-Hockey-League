import React from "react";
import useAuth from "../../hooks/useAuth";
import { useNavigate } from "react-router-dom";
import useCustomForm from "../../hooks/useCustomForm";
import axios from "axios";

let initialValue = {
    league: "",
    firstName: "",
    lastName: "",
    email: ""

};

const CreateTeamManagerPage = () => {
    const [user, token] = useAuth();
    const navigate = useNavigate();
    const [formData, handleInputChange, handleSubmit] = useCustomForm(initialValue, postNewTeamManager)

    async function postNewTeamManager(){
        try {
            let response = await axios.post("http://127.0.0.1:8000/api/team_managers/", formData, {
                headers: {
                    Authorization: 'Bearer ' + token
                }
            })
            navigate("/draft")
        } catch (error) {

        }
    }
    return (
        <div className="container">
            <form className="form" onSubmit={handleSubmit}>
                <label>
                    League:{" "}
                    <input
                       type="text"
                       name="league"
                       value={formData.league}
                       onChange={handleInputChange}
                    />
                </label>
                <label>
                    First Name:{" "}
                    <input
                       type="text"
                       name="first_name"
                       value={formData.first_name}
                       onChange={handleInputChange}
                    />
                </label>
                <label>
                    Last Name:{" "}
                    <input
                       type="text"
                       name="last_name"
                       value={formData.last_name}
                       onChange={handleInputChange}
                    />
                </label>
                <label>
                    Email:{" "}
                    <input
                       type="text"
                       name="email"
                       value={formData.email}
                       onChange={handleInputChange}
                    />
                </label>
                <button>Create Team Manager</button>
            </form>
        </div>
    )


}

export default CreateTeamManagerPage;