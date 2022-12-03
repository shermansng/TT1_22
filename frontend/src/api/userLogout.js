import axios from 'axios';
import session from './session';

const logout = async (username) => {
    let token = session.token;
    let payload = {
        username,
        token
    }
};

export default logout;;
