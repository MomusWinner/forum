import axios from "axios";
import { useEffect, useState, useCallback } from "react"
import { useNavigate } from "react-router-dom";
import { Sections } from "../Sections/Sections";
import { ListThreads } from "../ListThreads/ListThreads";
import { getToken } from "../utils"
import { CreateThreadModal } from "../Thread/CreateThreadModal";
import { HOST, THREAD } from "../../api-path";
import "./Forum.css";

export function Forum()
{
    const [sectionId, setSectionId] = useState()
    const [threads, setThreads] = useState()
    const navigate = useNavigate();

    useEffect(()=>{
        getThreads()
    }, [sectionId])

    useEffect(()=>{getThreads()},[])

    function getThreads()
    {
        let token = getToken(navigate)
        if(!token) return
        let query = ""
        if(sectionId !== null && sectionId !== undefined)
        query = "?sectionId=" + sectionId
        const result = axios.get(HOST + THREAD + query, { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            console.log("generate")
            setThreads(resp.data);
        })
        .catch((e) => console.log(e));
    }


    return(
        <div className="layout">
            <Sections token={getToken(navigate)} onChangeSection={setSectionId}/>
            <div id="threads-list" style={{flex: 1}}>
                <CreateThreadModal onCreate={getThreads}/>
                <ListThreads threads={threads}/>
            </div>
        </div>
    )
}