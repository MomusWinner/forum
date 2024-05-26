import axios from "axios";
import { Button, ModalBody, Modal, ModalFooter, ModalHeader, Input, Label } from "reactstrap";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { HOST, THREAD } from "../../api-path";
import { getToken } from "../utils"


export function CreateThreadModal({onCreate})
{
    const { className } = "";

    const [modal, setModal] = useState(false);
    const [title, setTitle] = useState()
    const navigate = useNavigate();


    const toggle = () => setModal(!modal);

    function createThread(){
        let token = getToken(navigate)
        if(title)
        {
            axios.post(HOST+THREAD, {title: title},  {headers: { "Authorization": 'Token ' + token } })   
            onCreate()
            toggle()
        }

    }

    return (
        <div>
            <Button onClick={toggle}>
            Create new thread
            </Button>
            <Modal
            isOpen={modal}
            modalTransition={{ timeout: 700 }}
            backdropTransition={{ timeout: 1300 }}
            toggle={toggle}
            className={className}>
                <ModalHeader toggle={toggle}>Create thread</ModalHeader>
                <ModalBody>
                    <Label for="title" sm={2}>
                        Title
                    </Label>
                    <Input id="title" onChange={(e) => setTitle(e.target.value)}></Input>
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" onClick={createThread}>
                    Create
                    </Button>
                    <Button color="secondary" onClick={toggle}>
                    Cancel
                    </Button>
                </ModalFooter>
            </Modal>
        </div>
      );
    
}