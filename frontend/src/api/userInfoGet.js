import axios from 'axios';
import {getHeader} from './apiConstant'
import session from './session';

const endpoint = `${URL}/user/info`

/**
 *
 * @param {*} id
 * @returns User info object, else false
 */
const getUserInfo = async (id) => {
    const payload = {
        id,
    }
    try {
        let axiosres = await axios.post(endpoint, payload, {
            headers: getHeader()
        });
        let res = axiosres.data;
        let data = res.data;
        console.log(data);
        if (data.code === 200) {
            return data.data;
        } else {
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default getUserInfo;
