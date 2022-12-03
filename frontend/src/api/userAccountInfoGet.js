import axios from 'axios';

const endpoint = `${URL}/user/info`

const getUserAccountInfo = async (id, email, address) => {
    const payload = {
        id,
        email,
        address,
    }
    try {
        let axiosres = await axios.post(endpoint, payload);
        let res = axiosres.data;
        
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default getUserAccountInfo;
