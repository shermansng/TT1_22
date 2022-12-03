import axios from 'axios';
import {URL, getHeader} from './apiConstant';

const endpoint = `${URL}/user/logout`

const logout = async () => {
    let payload = {}
    try {
        // let res = await axios.
        let res = await axios.post(endpoint, payload, {
            headers: getHeader()
        });
        console.log(res);
        return true;
    } catch (err) {
        console.log(err);
        return false;
    }
};

export default logout;;
