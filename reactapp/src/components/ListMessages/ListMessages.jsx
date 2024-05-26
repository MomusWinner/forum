import axios from "axios";
import { MESSAGE } from "../../api-path";
import { HOST, THREAD } from "../../api-path";
import { useEffect, useState } from "react";
import { Table } from "reactstrap";
import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import parse from 'html-react-parser';

export function ListMessages({token, messages})
{

    return(
        <>
        <Table >
            <thead>
            <tr>
                <th>User</th>
                <th style={{width: "70%"}}>Message</th>
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
                                parse(message.message_body)
                                // <CKEditor
                                //     editor={ ClassicEditor }
                                //     data={message.message_body}
                                //     disableWatchdog={true}
                                //     onReady={ editor => {
                                //         // You can store the "editor" and use when it is needed.
                                //         console.log( 'Editor is ready to use!', editor );
                                //     } }
                                //     onChange={ ( event ) => {
                                //         console.log( event );
                                //     } }
                                //     onBlur={ ( event, editor ) => {
                                //         console.log( 'Blur.', editor );
                                //     } }
                                //     onFocus={ ( event, editor ) => {
                                //         console.log( 'Focus.', editor );
                                //     } }
                                //     />
                        }</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </>
    )
}

