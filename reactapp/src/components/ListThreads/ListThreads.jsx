import axios from "axios";
import { HOST, THREAD } from "../../api-path";
import { useEffect, useState } from "react";
import { Spinner, Table } from "reactstrap";
import "./ListThreads.css"

export function ListThreads({token, sectionId})
{
    const [threads, setThreads] = useState()

    useEffect(()=>{
        if(sectionId === null) sectionId = ""
        else sectionId += "/"
        console.log(sectionId)
        const result = axios.get(HOST + THREAD + sectionId, { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            setThreads(resp.data);
        })
        .catch((e) => console.log(e));
    }, [])

    return(
        // <>
        //     {sections ?
        //         <ListGroup>
        //             {sections.map(section => (
        //                 <ListGroupItem>{section.name}</ListGroupItem>
        //             ))}
        //         </ListGroup>
        //         :
        //         <Spinner>
        //         Loading...
        //         </Spinner>}
        // </>
        <div className="thead-table">
        <Table >
            <thead>
            <tr>
                <th>Title</th>
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
                    <tr key={thread.url}>
                        <td>{thread.title}</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </div>
    )
}