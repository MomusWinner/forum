export function getToken(navigate)
{
    let newToken = localStorage.getItem('token')
    console.log(typeof(newToken) + newToken)
    if(newToken)  
        return newToken
    navigate('/login')
}