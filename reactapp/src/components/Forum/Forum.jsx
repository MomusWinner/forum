import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";
import { Sections } from "../Sections/Sections";
import { ListThreads } from "../ListThreads/ListThreads";
import "./Forum.css";

export function Forum()
{
    const [token, setToken] = useState()
    const [sectionId, setSectionId] = useState()
    const navigate = useNavigate();

    useEffect(()=>
    {
        const queryParams = new URLSearchParams(window.location.search)
        setSectionId(queryParams.get("sectionId"))

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
        <div className="layout">
            <Sections token={token}/>
            <ListThreads token={token} sectionId={sectionId}/>
        </div>
        :
        ""
        }
        </>
    )
}