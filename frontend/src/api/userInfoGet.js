import axios from 'axios';

const getUserInfo = (id ) => {
    axios.get('https://jsonplaceholder.typicode.com/users')
    .then(msg => console.log(msg)).catch(err => console.log(err));
}

export default getFakeUsers;
