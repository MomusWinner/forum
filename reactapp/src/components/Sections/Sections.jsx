import axios from "axios";
import { SECTION, HOST } from "../../api-path";
import { useEffect, useState } from "react";
import { Spinner, ListGroup, ListGroupItem } from "reactstrap";
import { Section } from "../Section/Section"
import "./Sections.css"

export function Sections({ token, onSetSection }) {
    const [sections, setSections] = useState();

    useEffect(() => {
        const result = axios.get(HOST + SECTION, { headers: { "Authorization": 'Token ' + token } })
            .then((resp) => {
                setSections(resp.data);
            })
            .catch((e) => console.log(e));
    }, []);

    return (
        <div className="section-list">
            {sections ?
                <ListGroup>
                    {sections.map(section => (
                        <Section section={section}/>
                    ))}
                </ListGroup>
                :
                <Spinner>
                Loading...
                </Spinner>}
        </div>
    );
}
