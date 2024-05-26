import axios from "axios";
import { MESSAGE } from "../../api-path";
import { HOST, THREAD } from "../../api-path";
import { useEffect, useState } from "react";
import { Spinner, Table } from "reactstrap";

import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';


export function ListMessages({token, threadId})
{
    const [messages, setMessages] = useState()

    useEffect(()=>{
        if(!token) return
        // if(sectionId === null || sectionId === undefined) sectionId = ""
        // else sectionId = "?sectionId=" + sectionId
        const result = axios.get(HOST + MESSAGE, { headers: { "Authorization": 'Token ' + token } })
        .then((resp) => {
            setMessages(resp.data);
        })
        .catch((e) => console.log(e));
    }, [threadId, token])

    return(
        <>
        <Table >
            <thead>
            <tr>
                <th>User</th>
                <th>Message</th>
            </tr>
            </thead>
            <tbody>
            {!messages || messages.length <= 0 ? (
                <tr>
                    <td colSpan="6" align="center">
                        <b>Пока ничего нет</b>
                    </td>
                </tr>
            ) : messages.map(message => (
                    <tr key={message.id}>
                        <td>{message.user_id}</td>
                        <td>{
                                    <CKEditor
                                    editor={ ClassicEditor }
                                    data={message.message_body}
                                    onReady={ editor => {
                                        // You can store the "editor" and use when it is needed.
                                        console.log( 'Editor is ready to use!', editor );
                                    } }
                                    onChange={ ( event ) => {
                                        console.log( event );
                                    } }
                                    onBlur={ ( event, editor ) => {
                                        console.log( 'Blur.', editor );
                                    } }
                                    onFocus={ ( event, editor ) => {
                                        console.log( 'Focus.', editor );
                                    } }
                                    />
                        }</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </>
    )
}

