export const URL = 'http://ec2-13-215-211-254.ap-southeast-1.compute.amazonaws.com';

export const getHeader = () => {
    return {
        "Authorization": `Bearer ${sessionStorage.getItem("token")}`
    }
}
