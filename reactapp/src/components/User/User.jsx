import axios from "axios";
import { useEffect, useState } from "react"
import { HOST, USER } from "../../api-path";
import { useNavigate } from "react-router-dom";
import { getToken } from "../utils"
import { Spinner } from "reactstrap";

export function User({userId})
{
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
            <p><a href={"/profile?userId=" + user.id}>{user.username}</a></p>
            </div>
            :
            <Spinner/>
            }
        </div>
        )
}