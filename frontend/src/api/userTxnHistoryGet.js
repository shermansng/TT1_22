import axios from 'axios';
import { URL, getHeader } from './apiConstant';

const endpoint = `${URL}/transactions/byAccount`;

const getTransactions = async (accountId) => {
    console.log(`AccountID: ${accountId}`);
    const payload = {
        "accountID":accountId
    };
    console.log(payload)
    try {
        let res = await axios.post(endpoint, payload, {
            headers: getHeader()
        });
        let data = res.data;
        console.log(data)
        if (data.code === 200) {
            return data.data;
        } else if (data.code === 400) {
            console.log(data.data);
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default getTransactions;
