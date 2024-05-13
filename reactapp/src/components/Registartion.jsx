import { Form, FormGroup, Label, Col, Input, FormFeedback, Button } from "reactstrap"
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export function Registration() {
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
          password: user["password"],
          email: user["email"]
      }
      console.log(data)
  
      const result = await axios.post("http://127.0.0.1:8000/api/v1/users/", data, {headers: {'Content-Type': 'multipart/form-data'}})
          .then(() => {
            navigate("/login")
          })
          .catch((e) => console.log(e.data))
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
            for="exampleEmail"
            sm={2}
          >
            Email
          </Label>
          <Col sm={10}>
            <Input
              id="exampleEmail"
              name="email"
              placeholder="with a placeholder"
              type="email"
              onChange={onChange}
            />
          </Col>
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