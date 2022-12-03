import * as React from "react";
import {NavBar} from "../NavBar/index"
import FormControl from '@mui/material/FormControl';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import Button from '@mui/material/Button';
import "./Account.css"

const Account = () => 
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
        <div className="account_container">
          <h1>User Details</h1>
          
          {/*Display FirstName + LastName */}
          <div className="account_username">
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Username:</InputLabel>
              <Input id="component-simple" value={username} onChange={(e) => {setUsername(e.target.value)}}/>
            </FormControl>
          </div>
          
          <div className="account_address">
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Address:</InputLabel>
              <Input id="component-simple" value={address} onChange={(e) => {setAddress(e.target.value)}}/>
            </FormControl>
          </div>

          <Button variant="contained" size="small" color="secondary" className="account_button_save">Save</Button>
        </div>
      </div>
    );
};

export default Account;
