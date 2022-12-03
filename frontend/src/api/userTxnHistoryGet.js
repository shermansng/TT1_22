import axios from 'axios';
import { URL } from './apiConstant';

const endpoint = `${URL}/transactions/byAccount`;

const getTransactions = async (accountId) => {
    console.log(`AccountID: ${accountId}`);
    const payload = {
        "accountID":accountId
    };
    console.log(payload)
    try {
        let res = await axios.post(endpoint, payload);
        let data = res.data;
        console.log(data)
        if (data.status === 'success') {
            return data.id;
        } else if (data.status === 'fail') {
            console.log(data.message);
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default getTransactions;
