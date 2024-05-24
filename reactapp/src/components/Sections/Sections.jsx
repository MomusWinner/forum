import axios from "axios";
import { SECTION, HOST } from "../../api-path";
import { useEffect, useState } from "react";
import { Spinner, ListGroup, ListGroupItem } from "reactstrap";
import "./Sections.css"

export function Sections({ token, onChangeSection }) {
    const [sections, setSections] = useState();
    const [error, setError] = useState(false);

    useEffect(() => {
        if(!token) return
        const result = axios.get(HOST + SECTION, { headers: { "Authorization": 'Token ' + token } })
            .then((resp) => {
                setSections(resp.data);
            })
            .catch((e) => setError(true));
    }, [token]);

    function getSections()
    {
        return(
            sections ?
            <ListGroup>
                {sections.map(section => (
                    <ListGroupItem key={section.id} onClick={() => onChangeSection(section.id)}>{section.name}</ListGroupItem>
                ))}
            </ListGroup>
            :
            <Spinner>
            Loading...
            </Spinner>
        )
    }

    return (
        <div className="section-list">
        {error ? <p>No info</p>: getSections()}
        </div>
    );
}
