import axios from 'axios';
import {URL, getHeader} from './apiConstant'

const ep = `${URL}/user/updateInfo`;

const updateUserInfo = async (id, email, address) => {
    const payload = {
        id,
        email,
        address,
    }
    try {
        let res = await axios.post(ep, payload, {
            headers: getHeader()
        });
        let data = res.data;
        if (data.code === 200) {
            return true;
        } else {
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
};

export default updateUserInfo;
