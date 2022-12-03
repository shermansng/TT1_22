import axios from 'axios';
import {URL, getHeader} from './apiConstant'

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
        // let data = res.data;
        if (res.code === 200) {
            return res.data;
        } else {
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default getUserInfo;
