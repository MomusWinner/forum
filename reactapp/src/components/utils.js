export function getToken(setToken, navigate)
{
    let newToken = localStorage.getItem('token')
    console.log(typeof(newToken) + newToken)
    if(newToken)  
        setToken(newToken)
    else
        navigate('/login')
}