import React from "react";
import { Link, Outlet } from "react-router-dom";
import "./NavBar.css"

function NavBar() {
  return (
    <div className="navbar">
      <img src="DBS-logo-dark.png" alt="DBS Logo" className="navbar_logo"></img>
      <Link to="/home" className="navbar_pages">Home</Link>
      <Link to="/transaction" className="navbar_pages">Transaction History</Link>
      <Link to="/account" className="navbar_pages">Account</Link>
    </div>
  );
}

export {NavBar};
