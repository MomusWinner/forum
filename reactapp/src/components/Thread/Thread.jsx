import axios from "axios";
import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";
import { getToken } from "../utils"
import { ListMessages } from "../ListMessages/ListMessages";
import { HOST, THREAD } from "../../api-path";

export function Thread()
{
    const queryParams = new URLSearchParams(window.location.search)
    const threadId = queryParams.get("threadId")
    const [thread, setThread] = useState()
    const navigate = useNavigate();

    useEffect(()=>
    {
        let token = getToken(navigate)

        const result = axios.get(HOST + THREAD + threadId + "/", { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            setThread(resp.data);
            console.log(resp.data)
        })
        .catch((e) => console.log(e));
    }, [])

    return(
        <div>
        <h1>{thread ? thread.title : ""}</h1>
        <ListMessages token={getToken(navigate)} threadId={threadId}/>
        </div>
    )
}