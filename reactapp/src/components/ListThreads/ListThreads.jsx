import axios from "axios";
import { HOST, THREAD } from "../../api-path";
import { useEffect, useState } from "react";
import { Spinner, Table } from "reactstrap";
import "./ListThreads.css"

export function ListThreads({token, sectionId})
{
    const [threads, setThreads] = useState()

    useEffect(()=>{
        if(!token) return
        if(sectionId === null || sectionId === undefined) sectionId = ""
        else sectionId = "?sectionId=" + sectionId
        const result = axios.get(HOST + THREAD + sectionId, { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            setThreads(resp.data);
        })
        .catch((e) => console.log(e));
    }, [sectionId, token])

    return(
        <div className="thead-table">
        <Table >
            <thead>
            <tr>
                <th>Title</th>
                <th>User</th>
            </tr>
            </thead>
            <tbody>
            {!threads || threads.length <= 0 ? (
                <tr>
                    <td colSpan="6" align="center">
                        <b>Пока ничего нет</b>
                    </td>
                </tr>
            ) : threads.map(thread => (
                    <tr key={thread.id}>
                        <td>{thread.title}</td>
                        <td>{thread.user_id}</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </div>
    )
}