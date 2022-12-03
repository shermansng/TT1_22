export const URL = 'http://ec2-13-215-211-254.ap-southeast-1.compute.amazonaws.com';

export const getHeader = (token) => {
    return {
        "Authorization": `Bearer ${token}`
    }
}
