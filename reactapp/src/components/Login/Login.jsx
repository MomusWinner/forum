import { Form, FormGroup, Label, Col, Input, FormFeedback, Button } from "reactstrap"
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { API_LOGIN, HOST }  from "../../api-path.js"
import "./Login.css";

export function Login() {
    const [user, setUser] = useState({})
    const [validLogin, setValidLogin] = useState()
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
  
      const result = await axios.post(HOST + API_LOGIN, data, {headers: {'Content-Type': 'multipart/form-data'}})
          .then((resp) => {
            console.log(resp.data["auth_token"])
            localStorage.setItem('token', resp.data["auth_token"])
            setValidLogin(undefined)
            navigate("/")
          })
          .catch((e) => setValidLogin("Name or password is incorrect."))
    }
  
    return (
    <>
    <p hidden={!validLogin} className='login-message'>{validLogin}</p>
    <Form onSubmit={submitDataAdd} id="login-form">
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
            <Button name="submit">
              Login
            </Button>
          </Col>
        </FormGroup>
    </Form>
    </>
    );
  }