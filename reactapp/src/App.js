import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import { Navbar, NavbarBrand } from 'reactstrap';
import { Routes, Route } from "react-router-dom"
import { Registration } from "./components/Registartion.jsx"
import { Login } from './components/Login.jsx';
import { Home } from './components/Home.jsx';
import { Forum } from './components/Forum/Forum.jsx';
import { Thread } from './components/Thread/Thread.jsx';
import { useNavigate } from "react-router-dom";
import { Profile } from './components/Profile/Profile.jsx';

function App() {
  const navigate = useNavigate();

  function handleLogout()
  {
    localStorage.setItem('token', "")
    navigate("/login")
  }

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
          <NavbarBrand onClick={handleLogout}>
            logout
          </NavbarBrand>
        </Navbar>

        <Routes>
         <Route path="/" element={<Home/>} />
          <Route path="/registration" element={<Registration/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="/forum" element={<Forum/>} />
          <Route path="/thread" element={<Thread/>} />
          <Route path="/profile" element={<Profile/>}/>
        </Routes>
      </div>
  );
}

export default App;
