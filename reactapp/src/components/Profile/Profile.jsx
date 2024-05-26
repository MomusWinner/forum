import axios from "axios";
import { useEffect, useState } from "react"
import { HOST, USER } from "../../api-path";
import { useNavigate } from "react-router-dom";
import { getToken } from "../utils"
import { Spinner } from "reactstrap";

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
        <div>
        <h1>{user.username}</h1>
        <p>{user.email}</p>
        </div>
        :
        <Spinner/>
        }
    </div>
    )
}