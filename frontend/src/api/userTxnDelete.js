import axios from 'axios';
import {URL, getHeader} from './apiConstant';

const ep = `${URL}/transactions/delete`;

const deleteTransaction = async (transactionID) => {
    let payload = {
        transactionID
    }
    try {
        // let res = axios.delete(ep, payload);
        let res = axios.post(ep, payload, {
            headers: getHeader()
        });
        return true;
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default deleteTransaction;
