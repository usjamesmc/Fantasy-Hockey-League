import React from "react";
import { useNavigate } from "react-router-dom";

const LeaguePage = () => {
  const navigate = useNavigate();
    

    return (
      <div>
        <div className="container">
          <h1>League Page!</h1>
        </div>
         <li>
         <button onClick={() => navigate("/draft")}>Draft new team</button>
         </li>
         <li>
         <button>Simulate random draft</button>
         </li>
      </div>
    );
    

}

export default LeaguePage;