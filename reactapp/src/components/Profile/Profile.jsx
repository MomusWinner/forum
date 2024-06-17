import axios from "axios";
import { useEffect, useState } from "react"
import { HOST, USER } from "../../api-path";
import { useNavigate } from "react-router-dom";
import { getToken } from "../utils"
import { Spinner } from "reactstrap";
import "./Profile.css";
import { ListThreads } from "../ListThreads/ListThreads";

export function Profile()
{
    const queryParams = new URLSearchParams(window.location.search)
    const userId = queryParams.get("userId")
    const [user, setUser] = useState()
    const navigate = useNavigate();

    useEffect(()=>{
        let token = getToken(navigate)
        const result = axios.get(HOST + USER + userId + "/", { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            setUser(resp.data);
            console.log(resp.data)
        })
        .catch((e) => console.log(e));
    }, [])


    return(
    <div>
        {user? 
        <div id="profile-container">
        <h1>Username: {user.username}</h1>
        <p>email: {user.email? user.email : "..."}</p>
        <h1>Threads</h1>
        <ListThreads threads={user.threads}/>
        </div>
        :
        <Spinner/>
        }
    </div>
    )
}