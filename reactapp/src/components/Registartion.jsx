import { Form, FormGroup, Label, Col, Input, FormFeedback, Button } from "reactstrap"
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export function Registration() {
    const [user, setUser] = useState({})
    const [validUser, setValidUser] = useState({})

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
          password: user["password"],
          email: user["email"]
      }
      console.log(data)
  
      const result = await axios.post("http://127.0.0.1:8000/api/v1/users/", data, {headers: {'Content-Type': 'multipart/form-data'}})
          .then(() => {
            navigate("/login")
          })
          .catch((e) => {
            console.log(e.response.data["username"])
            console.log(e.response.data)
            setValidUser(e.response.data)
          })
    }
  
    return (
    <Form onSubmit={submitDataAdd}>
        <FormGroup row>
          <Label
            for="username"
            sm={2}
          >
            Username
          </Label>
          <Col sm={10}>
            <Input
              invalid={validUser["username"] !== undefined}
              id="username"
              name="username"
              type="name"
              onChange={onChange}
            />
            <FormFeedback>
              {validUser["username"]}
            </FormFeedback>
          </Col>
        </FormGroup>
        <FormGroup row>
          <Label
            for="email"
            sm={2}
          >
            Email
          </Label>
          <Col sm={10}>
            <Input
              invalid={validUser["email"] !== undefined}
              id="email"
              name="email"
              type="email"
              onChange={onChange}
            />
            <FormFeedback>
              {validUser["email"]}
            </FormFeedback>
          </Col>
        </FormGroup>
        <FormGroup row>
          <Label
            for="password"
            sm={2}
          >
            Password
          </Label>
          <Col sm={10}>
            <Input
              invalid={validUser["password"] !== undefined}
              id="password"
              name="password"
              type="password"
              onChange={onChange}
            />
            <FormFeedback>
              {validUser["password"]}
            </FormFeedback>
          </Col>
        </FormGroup>
        <FormGroup check row>
          <Col
            sm={{
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