import axios from 'axios';
import {URL, getHeader} from './apiConstant'

const ep = `${URL}/user/updateInfo`;

const updateUserInfo = async (id, email, password) => {
    const payload = {
        id,
        email,
        password,
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
