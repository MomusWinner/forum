import { Spinner, ListGroup, ListGroupItem } from "reactstrap";

export function Section({section})
{
    return(
        <ListGroupItem key={section.id}>{<a href={"/forum?sectionId=" + section.id}>{section.name}</a>}</ListGroupItem>
    )
}