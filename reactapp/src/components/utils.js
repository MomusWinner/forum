export function getToken(navigate)
{
    let newToken = localStorage.getItem('token')
    console.log(typeof(newToken) + newToken)
    if(newToken)  
        return newToken
    navigate('/login')
}

export function formatDate(string){
    var options = {
        year: 'numeric', 
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric' };
    return new Date(string).toLocaleDateString([],options);
}