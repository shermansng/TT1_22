import axios from 'axios';

const endpoint = `${URL}/user/info`

/**
 * returns the user information object in the form:
 * {
 *     address,
 *     email,
 *     firstName,
 *     lastName,
 *     optIntoPhyStatements,
 * }
 */
const getUserInfo = async (id, email, address) => {
    const payload = {
        id,
        email,
        address,
    }
    try {
        let axiosres = await axios.post(endpoint, payload);
        let res = axiosres.data;
        if (res.code === 200) {
            return res.data;
        } else if (res.code === 404) {
            console.log(res.data.message);
            return false;
        }
    } catch (err) {
        console.log(err);
        return false;
    }
}

export default getUserInfo;
