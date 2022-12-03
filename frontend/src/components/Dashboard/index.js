import React from "react";
import { useState } from "react";
import {NavBar} from "../NavBar/index"

const Dashboard = () => {
  // const [user, setUser] = useState({
  //   login: "",
  //   password: "",
  // });
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  return (
    <div>
      <NavBar/>
      <h1>Dashboard</h1>
      Username:
      <input
        type="text"
        value={username}
        onChange={(e) => {
          setUsername(e.target.value);
        }}
      />
      <br />
      Password:
      <input
        type="text"
        value={password}
        onChange={(e) => {
          setPassword(e.target.value);
        }}
      />
      <button>Login</button>
      <button
        onClick={() => {
          setUsername("");
          setPassword("");
        }}
      >
        Reset
      </button>
    </div>
  );
};

export default Dashboard;
