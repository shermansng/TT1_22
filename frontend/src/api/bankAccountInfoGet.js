import axios from 'axios';
import {URL, getHeader} from './apiConstant'

const ep = `${URL}/user/bankaccounts`

const getBankAccountInfo = async (userid) => {
    const payload = {
        userid
    }
    try {
        let res = await axios.post(ep, payload, {
            headers: getHeader()
        });
        let data = res.data;
        if (data.code === 200) {
            return data.data;
        } else {
            return false;
        }
    } catch (err) {
        console.log(err)
        return false;
    }
};

export default getBankAccountInfo;
