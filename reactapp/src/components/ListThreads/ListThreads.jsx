import { Spinner, Table } from "reactstrap";
import "./ListThreads.css"
import { User } from "../User/User";
import { formatDate } from "../utils";

export function ListThreads({threads})
{
    return(
        <div>
        <Table >
            <thead>
            <tr>
                <th>Title</th>
                <th>User</th>
                <th>Created</th>
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
                        <td><a href={"/thread?threadId=" + thread.id}>{thread.title}</a></td>
                        <td><User userId={thread.user_id}/></td>
                        <td>{formatDate(thread.created)}</td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </div>
    )
}