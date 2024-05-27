import axios from "axios";
import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";
import { getToken } from "../utils"
import { ListMessages } from "../ListMessages/ListMessages";
import { HOST, THREAD } from "../../api-path";
import { Spinner } from "reactstrap";
import { CreateMessageModal } from "../CreateMessageModal/CreateMessageModal";

export function Thread()
{
    const queryParams = new URLSearchParams(window.location.search)
    const threadId = queryParams.get("threadId")
    const [thread, setThread] = useState()
    const navigate = useNavigate();

    useEffect(()=>
    {
        getMessages()
    }, [])

    function getMessages()
    {
        let token = getToken(navigate)
        const result = axios.get(HOST + THREAD + threadId + "/", { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            setThread(resp.data);
            console.log(resp.data)
        })
        .catch((e) => console.log(e));
    }

    return(
        <div>
        {thread?
        <>
        <h1>{thread ? thread.title : ""}</h1>
        <CreateMessageModal threadId={threadId} onCreate={getMessages}/>
        <ListMessages token={getToken(navigate)} messages={thread.messages}/>
        </>
        :
        <Spinner/>
        }
        </div>
    )
}