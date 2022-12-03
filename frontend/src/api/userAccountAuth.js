import axios from 'axios';
import {URL} from './apiConstant';
import session from './session';

const endpoint = `${URL}/user/login`;

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
            session.user.firstname = data.firstName;
            session.user.lastname = data.lastName;
            return true
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
