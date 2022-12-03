import axios from 'axios';
import {URL} from './apiConstant';
import session from './session';

const endpoint = `${URL}/user/login`;

/**
 * 
 * @param {*} username
 * @param {*} password
 * @returns id of the user if authenticated, else returns false;
 */
const authenticateUser = async (username, password) => {
    const payload = {
        username,
        password
    };

    try {
        let res = await axios.post(endpoint, payload);
        let data = res.data;
        if (data.status === 'success') {
            session.token = data.token;
            session.userid = data.id;
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
