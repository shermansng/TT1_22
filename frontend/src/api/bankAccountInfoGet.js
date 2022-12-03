import axios from 'axios';
import {URL} from './apiConstant';

const ep = `${URL}/user/bankaccounts`

const getBankAccountInfo = async (id) => {
    const payload = {
        id
    }
    try {
        let res = await axios.post(ep, payload);
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
