import axios from 'axios';
import {URL} from './apiConstant';

const ep = `${URL}/transactions/delete`;

const deleteTransaction = async (transactionID) => {
    let payload = {
        transactionID
    }
    try {
        // let res = axios.delete(ep, payload);

    } catch (err) {
        console.log(err);
        return false;
    }
}

export default deleteTransaction;
