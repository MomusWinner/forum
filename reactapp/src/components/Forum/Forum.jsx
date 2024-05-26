import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";
import { Sections } from "../Sections/Sections";
import { ListThreads } from "../ListThreads/ListThreads";
import { getToken } from "../utils"
import "./Forum.css";

export function Forum()
{
    const [sectionId, setSectionId] = useState()
    const navigate = useNavigate();

    return(
        <div className="layout">
            <Sections token={getToken(navigate)} onChangeSection={setSectionId}/>
            <ListThreads token={getToken(navigate)} sectionId={sectionId}/></div>
    )
}