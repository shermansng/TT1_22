import axios from 'axios';
import {URL, getHeader} from './apiConstant';

const ep = `${URL}/transactions/insert`;

const insertTransaction = async (txnObj) => {
    try {
        let res = await axios(ep, txnObj);
        if (res) {
            return true;
        } else {
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default insertTransaction;
