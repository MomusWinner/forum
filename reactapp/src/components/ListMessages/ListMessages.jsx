import { Table } from "reactstrap";
import parse from 'html-react-parser';
import { User } from "../User/User";
import { formatDate } from "../utils";
import MDEditor from '@uiw/react-md-editor';

export function ListMessages({messages})
{
    return(
        <>
        <Table >
            <thead>
            <tr>
                <th>User</th>
                <th style={{width: "70%"}}>Message</th>
                <th>Created</th>
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
                        <td>{<User userId={message.user}/>}</td>
                        <td>{<div data-color-mode="light"><MDEditor.Markdown source={message.message_body}/></div>}</td>
                        <td>{formatDate(message.created)}</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </>
    )
}

