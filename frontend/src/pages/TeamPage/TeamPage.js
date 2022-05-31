import React from "react";
import { useNavigate } from "react-router-dom";


const TeamPage = () => {
    const navigate = useNavigate();
    
    return (
        <div>
            <li>
                <button onClick={() => navigate("/draft")}>Draft new team</button>
            </li>
            <li>
                <button>Simulate random draft</button>
            </li>
            <div className="container">
                <h1>Team Name Skaters</h1>
            </div>
            <div className="container">
                <h2>Team Name Goalies</h2>
            </div>
        </div>
    );
    

}

export default TeamPage;