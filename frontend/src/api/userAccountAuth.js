import axios from 'axios';
import {URL} from './apiConstant';

const endpoint = `${URL}/user/login`;

/**
 *
 * @param {*} username
 * @param {*} password
 * @returns id of the user if authenticated, else returns false;
 */
const authenticateUser = async (username, password) => {
    console.log(`Username: ${username}, password: ${password}`);
    const payload = {
        username,
        password
    };

    try {
        let res = await axios.post(endpoint, payload);
        let data = res.data.data;
        if (data.status === 'success') {
            sessionStorage.setItem("token", data.token);
            return data.id;
        } else if (data.status === 'fail') {
            console.log(data.message);
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default authenticateUser;
