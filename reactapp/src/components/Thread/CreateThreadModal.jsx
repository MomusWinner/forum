import axios from "axios";
import { Button, ModalBody, Modal, ModalFooter, ModalHeader, Input, Label } from "reactstrap";
import Select from 'react-select' 
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { HOST, SECTION, THREAD } from "../../api-path";
import { getToken } from "../utils"

import makeAnimated from 'react-select/animated';

const animatedComponents = makeAnimated();

export function CreateThreadModal({onCreate})
{
    const [modal, setModal] = useState(false)
    const [sectionsOption, setsectionsOption] = useState()

    const [title, setTitle] = useState()
    const [sections, setSections] = useState()
    const toggle = () => setModal(!modal);
    const navigate = useNavigate();
    
    useEffect(()=>{
        let token = getToken(navigate)
        axios.get(HOST + SECTION, {headers: { "Authorization": 'Token ' + token } } )
        .then((resp)=>{
            var sections = []
            for(let i=0; i<resp.data.length; i++)
            {
                let section = new Object()
                section.label = resp.data[i].name
                section.value = resp.data[i].id
                sections.push(section)
            }
            setsectionsOption(sections)
        })
        .catch((e)=>{
            console.log(e.data)
        })
    }, [])

    function createThread(){
        let token = getToken(navigate)
        let sectionsId = []
        if(sections)
            sections.forEach((section)=>sectionsId.push(section.value))
        axios.post(HOST+THREAD, {title: title, sections: sectionsId}, {headers: { "Authorization": 'Token ' + token } })
        .then((resp)=>{
            onCreate()
            toggle()
        })
        .catch((e) =>
        {
            toggle()
        })
    }

    return (
        <div>
            <Button id="create-thread-button" onClick={toggle}>
            Create new thread
            </Button>
            <Modal
            isOpen={modal}
            modalTransition={{ timeout: 300 }}
            backdropTransition={{ timeout: 700 }}
            toggle={toggle}>
                <ModalHeader toggle={toggle}>Create thread</ModalHeader>
                <ModalBody>
                    <Label for="title" sm={2}>
                        Title
                    </Label>
                    <Input id="title" onChange={(e) => setTitle(e.target.value)}></Input>
                    <Label for="sections" sm={2}>
                        Sections
                    </Label>
                    <Select
                        id="sections"
                        closeMenuOnSelect={false}
                        components={animatedComponents}
                        isMulti
                        options={sectionsOption}
                        onChange={setSections}
                    />
                </ModalBody>
                <ModalFooter>
                    <Button id="create-thread-modal-button" color="primary" onClick={createThread}>
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