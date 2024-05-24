import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";
import { Sections } from "../Sections/Sections";
import { getToken } from "../utils"

export function Thread()
{
    const [token, setToken] = useState()
    const navigate = useNavigate();

    useEffect(()=>
    {
        getToken(setToken, navigate)
    }, [])

    return(
        <div className="layout">
            <Sections token={token}/>
            {/* <ListThreads token={token} sectionId={sectionId}/> */}
        </div>
    )
}