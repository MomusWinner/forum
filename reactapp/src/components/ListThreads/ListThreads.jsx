import axios from "axios";
import { HOST, THREAD } from "../../api-path";
import { useEffect, useState } from "react";
import { Spinner, Table } from "reactstrap";
import "./ListThreads.css"

export function ListThreads({threads})
{

    return(
        <div>
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
                        <td><a href={"/thread?threadId=" + thread.id}>{thread.title}</a></td>
                        <td><a href={"/profile?userId=" + thread.user_id}>{thread.user_id}</a></td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
        </div>
    )
}