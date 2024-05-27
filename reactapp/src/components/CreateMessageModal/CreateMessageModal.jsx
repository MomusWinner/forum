import axios from "axios";
import { Button, ModalBody, Modal, ModalFooter, ModalHeader, Input, Label } from "reactstrap";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { HOST, MESSAGE } from "../../api-path";
import { getToken } from "../utils"
import { CKEditor } from '@ckeditor/ckeditor5-react';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

export function CreateMessageModal({onCreate, threadId})
{
    const [modal, setModal] = useState(false)
    const [messageBody, setMessageBody] = useState()

    const toggle = () => setModal(!modal);
    const navigate = useNavigate();

    function createMessage(){
        let token = getToken(navigate)
        axios.post(HOST+MESSAGE, {message_body: messageBody, thread: threadId}, {headers: { "Authorization": 'Token ' + token } })
        .then((resp)=>{
            onCreate()
            toggle()
        })
        .catch((e) =>
        {
            console.log(e.data)
            toggle()
        })
    }

    return (
        <div>
            <Button onClick={toggle}>
            Create new message
            </Button>
            <Modal
            isOpen={modal}
            modalTransition={{ timeout: 300 }}
            backdropTransition={{ timeout: 700 }}
            toggle={toggle}>
                <ModalHeader toggle={toggle}>Create thread</ModalHeader>
                <ModalBody>
                    <CKEditor
                    editor={ ClassicEditor }
                    disableWatchdog={true}
                    onReady={ editor => {
                        console.log( 'Editor is ready to use!', editor.getData() );
                    } }
                    onChange={(event, editor) => setMessageBody(editor.getData())}
                    />
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" onClick={createMessage}>
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