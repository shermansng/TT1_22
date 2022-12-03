import Login from "./components/Login";
import React from "react";
import { Routes, Route } from "react-router-dom";
import Account from "./components/Account"
import Dashboard from "./components/Dashboard";
import Home from "./components/Home";
import {NavBar} from "./components/NavBar";
import NoMatch from "./components/NoMatch";
import TransactionPage from "./components/TransactionPage";
 
function App() {
  return (
    <div>
      <Routes>
          <Route path="/" element={<Login/>} />
          {/* <Route path="/" element={<NavBar />} /> */}
          <Route path="/home" element={<Home />} />
          <Route path="/account" element={<Account />} />
          <Route path="/nomatch" element={<NoMatch />} />
          <Route path="/transaction" element = {<TransactionPage />} />
        </Routes>
    </div>
  );
}

export default App;
