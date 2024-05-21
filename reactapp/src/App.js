import './App.css';
import 'bootstrap/dist/css/bootstrap.css';

import { Navbar, NavbarBrand } from 'reactstrap';
import { Routes, Route, Link } from "react-router-dom"
import { Registration } from "./components/Registartion.jsx"
import { Login } from './components/Login.jsx';
import { Home } from './components/Home.jsx';
import { Forum } from './components/Forum/Forum.jsx';

function App() {
  return (
      <div>
        <Navbar>
          <NavbarBrand href="/">
            Home
          </NavbarBrand>
          <NavbarBrand href="/forum">
            Forum
          </NavbarBrand>
          <NavbarBrand href="/registration">
            Reagistration
          </NavbarBrand>
          <NavbarBrand href="/login">
            login
          </NavbarBrand>
        </Navbar>

        <Routes>
         <Route path="/" element={<Home />} />
          <Route path="/registration" element={<Registration />} />
          <Route path="/login" element={<Login />} />
          <Route path="/forum" element={<Forum />} />
        </Routes>
      </div>
  );
}

export default App;
