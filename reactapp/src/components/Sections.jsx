import axios from "axios";
import { SECTION, HOST } from "../api-path";
import { useEffect, useState } from "react";
import { ListGroup, ListGroupItem } from "reactstrap";

export function Sections({ token }) {
    const [sections, setSections] = useState();

    useEffect(() => {
        const result = axios.get(HOST + SECTION, { headers: { "Authorization": 'Token ' + token } })
            .then((resp) => {
                console.log(resp.data);
                setSections(resp.data);
            })
            .catch((e) => console.log(e));
    }, []);

    return (
        <>
            {sections ?
                <ListGroup>
                    {sections.map(section => (
                        <ListGroupItem>{section.name}</ListGroupItem>
                    ))}
                </ListGroup>
                :
                <div>Загрузка</div>}
        </>
    );
}
