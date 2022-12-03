import axios from 'axios';
import {URL} from './apiConstant';

const endpoint = `${URL}/user/login`;

const authenticateUser = (username, password, successCallback) => {
    const payload = {
        username,
        password
    }
    axios.post(endpoint, payload)
    // .then(res => successCallback(res))
    .then(response => console.log(response))
    .catch(err => console.log(err));
}

export default authenticateUser;
