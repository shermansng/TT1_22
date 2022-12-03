import { Button } from "@mui/material";
import React from "react";
import { Link, useNavigate } from "react-router-dom";
import "./NavBar.css"
import session from '../../api/session';

function NavBar() {

  const navigate = useNavigate();
  const sessionProperties = Object.getOwnPropertyNames(session);
  const logout = () =>{
    //clear session object
    sessionProperties.forEach(property => {
      delete session[property];
    });
    console.log(session)
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

export {NavBar};
