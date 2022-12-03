import Login from "./components/Login";
import React from "react";
import { Routes, Route } from "react-router-dom";
import About from "./components/About";
import Dashboard from "./components/Dashboard";
import Home from "./components/Home";
import {NavBar} from "./components/NavBar";
import NoMatch from "./components/NoMatch";

function App() {
  return (
    <div>
      <Routes>
          <Route path="/" element={<Login/>} />
          {/* <Route path="/" element={<NavBar />} /> */}
          <Route path="/home" element={<Home />} />
          <Route path="/transaction" element={<Dashboard />} />
          <Route path="/account" element={<About />} />
          <Route path="/nomatch" element={<NoMatch />} />
        </Routes>
    </div>
  );
}

export default App;
