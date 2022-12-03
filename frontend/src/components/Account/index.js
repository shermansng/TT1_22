import * as React from "react";
import {NavBar} from "../NavBar/index"
import FormControl from '@mui/material/FormControl';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import Button from '@mui/material/Button';
import getUserInfo from "../../api/userInfoGet"
import "./Account.css"
import userInfoUpdate from "api/userInfoUpdate";

const Account = () => 
{    
    const [userData, setUserData] = React.useState([])
    const [email, setEmail] = React.useState("")
    const [address, setAddress] = React.useState("")
    const id = parseInt(sessionStorage.getItem("id"));
    
    React.useEffect(() => {
      // declare the data fetching function
      const getUsers = async () => {
        let response = await getUserInfo(id);
        console.log(response);
        setUserData(response);
      }
      
      // call the function
      getUsers()
        // make sure to catch any error
        .catch(console.error);
    }, [])

    const HandleSubmit = (e) => {
      e.preventDefault();
      userInfoUpdate(id,email,address);
    }
    return (
      <div>
        <NavBar/>
        <div className="account_container">

          <h1>User Details</h1>
          {/*Display FirstName + LastName */}

          <div className="account_username">
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Email:</InputLabel>
              <Input id="component-simple" value={userData["email"]} onChange={(e) => {setEmail(e.target.value)}}/>
            </FormControl>
          </div>
          
          <div className="account_address">
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Address:</InputLabel>
              <Input id="component-simple" value={userData["address"]} onChange={(e) => {setAddress(e.target.value)}}/>
            </FormControl>
          </div>

          <Button variant="contained" size="small" color="secondary" className="account_button_save" onClick={HandleSubmit}>Save</Button>
        </div>
      </div>
    );
};

export default Account;
