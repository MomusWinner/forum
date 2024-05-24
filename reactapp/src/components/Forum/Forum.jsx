import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";
import { Sections } from "../Sections/Sections";
import { ListThreads } from "../ListThreads/ListThreads";
import { getToken } from "../utils"
import "./Forum.css";

export function Forum()
{
    const [token, setToken] = useState()
    const [sectionId, setSectionId] = useState()
    const navigate = useNavigate();

    useEffect(()=>
    {
        getToken(setToken, navigate)
    }, [])

    return(
        <div className="layout">
            <Sections token={token} onChangeSection={setSectionId}/>
            <ListThreads token={token} sectionId={sectionId}/></div>
    )
}