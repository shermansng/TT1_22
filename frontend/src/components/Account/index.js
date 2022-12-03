import * as React from "react";
import {NavBar} from "../NavBar/index"
import FormControl from '@mui/material/FormControl';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';

function Account()
{
    // GET, POST, DELETE of address and email    
    
    // GET
    const [searchEmail, getEmail] = React.useState("Email")
    
    // POST
    const [username, setUsername] = React.useState("Username");
    const [address, setAddress] = React.useState("Address")

    return (
      <div>
        <NavBar/>
        <div id="Body">
          <h1>Account</h1>
          
          {/*Display FirstName + LastName */}
          <FormControl variant="standard">
            <InputLabel htmlFor="component-simple">Username</InputLabel>
            <Input id="component-simple" value={username} onChange={(e) => {setUsername(e.target.value)}}/>
          </FormControl>
          <FormControl variant="standard">
            <InputLabel htmlFor="component-simple">Address</InputLabel>
            <Input id="component-simple" value={address} onChange={(e) => {setAddress(e.target.value)}}/>
          </FormControl>
        </div>
      </div>
    );
};

export default Account;
