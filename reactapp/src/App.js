import logo from './logo.svg';
import './App.css';
import { useState } from "react"
import {Form, FormGroup, Label, Col, Input, FormFeedback, Button} from "reactstrap"
import { Routes, Route, Link } from "react-router-dom"
import axios from "axios";

function App() {
  return (
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/Reagistration">Reagistration</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/reset">Reset</Link>
            </li>
            <li>
              <Link to="/dashboard">Dashboard</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/Reagistration" element={<Reagistration />} />
          <Route path="/login" element={<Login />} />
          <Route path="/reset" element={<PasswordReset />} />
        </Routes>
      </div>
  );
}


function Reagistration() {
  const [user, setUser] = useState({})

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
            console.log("sfsdaf")
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
      </FormGroup></Form>
  );
}

function Login() {
  return <h2>Login</h2>;
}

function PasswordReset() {
  return <h2>Password Reset</h2>;
}

function Dashboard() {
  return <h2>Dashboard</h2>;
}

export default App;
