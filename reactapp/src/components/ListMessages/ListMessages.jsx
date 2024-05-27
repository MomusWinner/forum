import { Table } from "reactstrap";
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
                        <td>{message.user}</td>
                        <td>{
                                parse(message.message_body)
                        }</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </>
    )
}

