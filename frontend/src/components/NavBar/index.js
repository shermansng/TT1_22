import { Button } from "@mui/material";
import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./NavBar.css"
import sessionLogout from "../../api/userLogout";

function Logout() {
    const navigate = useNavigate();
    sessionLogout();
    sessionStorage.removeItem("token");
    navigate('/');
}

function NavBar() {

  const navigate = useNavigate();
  const logout = () =>{
    sessionLogout()
    sessionStorage.removeItem("token")
    navigate("/")
  }
  return (
    <div className="navbar">
      <img src="DBS-logo-dark.png" alt="DBS Logo" className="navbar_logo"></img>
      <Link to="/home" className="navbar_pages">Home</Link>
      <Link to="/transaction" className="navbar_pages">Transaction History</Link>
      <Link to="/account" className="navbar_pages">Account</Link>
      <Button variant="contained" onClick={logout} sx={{float:"right", backgroundColor:"red", margin:"10px", fontSize:"10px"}}>Logout</Button>
    </div>
  );
}

export {NavBar, Logout};
