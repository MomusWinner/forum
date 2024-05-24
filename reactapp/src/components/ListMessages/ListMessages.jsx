import { MESSAGE } from "../../api-path";

export function ListMessages({token, threadId})
{
    useEffect(()=>{
        if(!token) return
        // if(sectionId === null || sectionId === undefined) sectionId = ""
        // else sectionId = "?sectionId=" + sectionId
        const result = axios.get(HOST + MESSAGE, { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            setThreads(resp.data);
        })
        .catch((e) => console.log(e));
    }, [threadId, token])

    return(
        
    )
}