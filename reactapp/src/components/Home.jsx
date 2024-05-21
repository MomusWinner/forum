import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";
import { Sections } from "./Sections";

export function Home()
{
    const [token, setToken] = useState()
    const navigate = useNavigate();

    useEffect(()=>
    {
        let newToken = localStorage.getItem('token')
        console.log(typeof(newToken) + " " + newToken)
        if(newToken === undefined)
        {   
            console.log('artartrar') 
            navigate('/login')
        }
        else{
            setToken(newToken)
        }
    }, [])

    return(
        <>
        {token?
        <Sections token={token}/>:
        ""
        }
        </>
    )
}