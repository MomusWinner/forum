import { Form, FormGroup, Label, Col, Input, FormFeedback, Button } from "reactstrap"
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { API_LOGIN }  from "../api-path.js"


export function Login() {
    const [user, setUser] = useState({})
    const navigate = useNavigate();

    const onChange = (e) => {
      const newUser = user
      newUser[e.target.name] = e.target.value
      setUser(newUser)
    }
  
    const submitDataAdd = async (e) => {
      e.preventDefault();
      const data = {
          username: user["username"],
          password: user["password"]
      }
      console.log(API_LOGIN)
  
    
      const result = await axios.post(API_LOGIN, data, {headers: {'Content-Type': 'multipart/form-data'}})
          .then(() => {
            localStorage.setItem('token', data["auth_token"])
            localStorage.getItem('token')
            navigate("/")
          })
          .catch((e) => console.log('[Error] ' + e.data))
    }
  
    return (
    <Form onSubmit={submitDataAdd}>
        <FormGroup row>
          <Label
            for="exampleUsername"
            sm={2}
          >
            Username
          </Label>
          <Col sm={10}>
            <Input
              id="exampleUsername"
              name="username"
              placeholder="with a placeholder"
              type="name"
              onChange={onChange}
            />
          </Col>
          <FormFeedback>
            You will not be able to see this
          </FormFeedback>
        </FormGroup>
        <FormGroup row>
          <Label
            for="examplePassword"
            sm={2}
          >
            Password
          </Label>
          <Col sm={10}>
            <Input
              id="examplePassword"
              name="password"
              placeholder="password placeholder"
              type="password"
              onChange={onChange}
            />
          </Col>
        </FormGroup>
        <FormGroup
          check
          row
        >
          <Col
            sm={{
              offset: 2,
              size: 10
            }}
          >
            <Button>
              Submit
            </Button>
          </Col>
        </FormGroup>
    </Form>
    );
  }