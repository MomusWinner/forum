import './App.css';
import 'bootstrap/dist/css/bootstrap.css';

import { Navbar, NavbarBrand } from 'reactstrap';
import { Routes, Route, Link } from "react-router-dom"
import { Registration } from "./components/Registartion.jsx"
import { Login } from './components/Login.jsx';
import { Home } from './components/Home.jsx';

function App() {
  return (
      <div>
        <Navbar>
          <NavbarBrand href="/">
            Home
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
        </Routes>
      </div>
  );
}

export default App;
