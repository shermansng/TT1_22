import * as React from "react";
import {NavBar} from "../NavBar/index"
import FormControl from '@mui/material/FormControl';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import Button from '@mui/material/Button';
import getUserInfo from "../../api/userInfoGet"
import "./Account.css"

const Account = () => 
{    
    const initialUserData = {
      address: "",
      email: "",
      firstName: "",
      lastName: "",
      optIntoPhyStatements: null
    };    

    const [userData, getUserData] = React.useState(initialUserData)
    const [username, setUsername] = React.useState("Username");
    const [address, setAddress] = React.useState("Address")

    React.useEffect(() => {
      // declare the data fetching function
      const getUsers = async () => {
        const data = await getUserInfo(1);
        getUserData(data)
        console.log(data)
      }

      // call the function
      getUsers()
        // make sure to catch any error
        .catch(console.error);
    }, [])

    return (
      <div>
        <NavBar/>
        <div className="account_container">

          <h1>User Details</h1>
          {/*Display FirstName + LastName */}

          <div className="account_username">
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Username:</InputLabel>
              <Input id="component-simple" value={userData.email} onChange={(e) => {setUsername(e.target.value)}}/>
            </FormControl>
          </div>
          
          <div className="account_address">
            <FormControl variant="standard">
              <InputLabel htmlFor="component-simple">Address:</InputLabel>
              <Input id="component-simple" value={userData.address} onChange={(e) => {setAddress(e.target.value)}}/>
            </FormControl>
          </div>

          <Button variant="contained" size="small" color="secondary" className="account_button_save">Save</Button>
        </div>
      </div>
    );
};

export default Account;
