// General Imports
import { Routes, Route } from "react-router-dom";
import "./App.css";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";
import LeaguePage from "./pages/LeaguePage/LeaguePage";
import TeamPage from "./pages/TeamPage/TeamPage";
import TradePage from "./pages/TradePage/TradePage";
import DraftPage from "./pages/DraftPage/DraftPage";
import CreateLeaguePage from "./pages/CreateLeaguePage/CreateLeague";
import CreateTeamManagerPage from "./pages/CreateTeamManagerPage/CreateTeamManagerPage";
// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/league" element={<PrivateRoute><LeaguePage /></PrivateRoute>} />
        <Route path="/team" element={<PrivateRoute><TeamPage /></PrivateRoute>} />
        <Route path="/trade" element={<PrivateRoute><TradePage /></PrivateRoute>} />
        <Route path="/home" element={<PrivateRoute><HomePage /></PrivateRoute>} />
        <Route path="/draft" element={<PrivateRoute><DraftPage /></PrivateRoute>} />
        <Route path="/createLeague" element={<PrivateRoute><CreateLeaguePage /></PrivateRoute>} />
        <Route path="/createTeamManager" element={<PrivateRoute><CreateTeamManagerPage /></PrivateRoute>} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
