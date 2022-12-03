import axios from 'axios';
import session from './session';

const logout = async (username) => {
    let token = session.token;
    let payload = {
        username,
        token
    }
    try {
        // let res = await axios.
    } catch (err) {
        console.log(err);
        return false;
    }
};

export default logout;;
