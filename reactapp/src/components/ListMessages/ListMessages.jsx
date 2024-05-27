import { Table } from "reactstrap";
import parse from 'html-react-parser';
import { User } from "../User/User";
import { formatDate } from "../utils";

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
                        <td>{parse(message.message_body)}</td>
                        <td>{formatDate(message.created)}</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </>
    )
}

