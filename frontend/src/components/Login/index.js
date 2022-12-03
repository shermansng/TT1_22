import React, {useState, useEffect, useRef} from 'react';
import { Link, useNavigate } from 'react-router-dom'
import './Login.css';
import { Button, TextField } from '@mui/material';
import authUser from '../../api/userAccountAuth';
import userInfoGet from '../../api/userInfoGet';

const Login = () => {

    const [username ,setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const login = async () => {
        let id = await authUser(username, password);
        if (id) {
            console.log("Login success");
            navigate("/home")
            sessionStorage.setItem("id",id)
        } else {
            console.log("Login failed");
            // login failure
        }
    }

    return (
        <div className="login">
            <div className="login__container">
                <input
                    type="text"
                    className="login__textBox"
                    value={username}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Username"
                />
                <input
                    type="password"
                    className="login__textBox"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                />
                <Button variant="contained"
                        onClick = {login} >
                Login
                </Button>
            </div>
        </div>
    )
}

//     const [registerEmail, setRegisterEmail] = useState("");
//     const [registerPassword, setRegisterPassword] = useState("");
//     const [loginEmail, setLoginEmail] = useState("");
//     const [loginPassword, setLoginPassword] = useState("");
//     const [user, setUser] = useState({})

//     //use "useEffect" with [] so that onAuthStateChange is only called once when mounted
//     // React.useEffect(() => {onAuthStateChanged(auth, (currentUser) => {setUser(currentUser)})},[])

//     //register function (using async await)
//     const register = async () => {
//         try {
//         const user = await createUserWithEmailAndPassword(auth, registerEmail, registerPassword);
//         console.log(user);
//         } catch (error) {
//         console.log(error.message);
//         }
//     };

//     //login function (using async await)
//     const login = async () => {
//         console.log("login")
//         try {
//         const user = await loginWithEmailAndPassword(auth, loginEmail, loginPassword);
//         console.log(user);
//         } catch (error) {
//         console.log(error.message);
//         }
//     };

//     return (
//     <div className='login'>
//         <form action="">
//             <h1>Sign in</h1>
//             <input
//                 // onChange={(event)=>{setRegisterEmail(event.target.value)}}
//                 onChange={(event)=>{setLoginEmail(event.target.value)}}
//                 type="email"
//             />
//             <input
//                 // onChange={(event)=>{setRegisterPassword(event.target.value)}}
//                 onChange={(event)=>{setLoginPassword(event.target.value)}}
//                 type="password"
//             />
//             <button onClick={login}>Sign in</button>
//             <h6> Not yet registered? <span onClick={register} className="login_link"> Sign up </span></h6>
//         </form>
//     </div>
//   )
// }

export default Login
