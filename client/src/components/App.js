import { Routes, Route } from "react-router-dom";
import Home from "./Home";
import Navbar from './Navbar';
import Mainpage from './Mainpage';
import CarDetail from "./CarDetail"
import Login from "./Login";
import About from "./About";




function App() {
  return (
    <>
          <main>
          <Navbar />
            <Routes>
              {/* <Route path="/" element={<Login />}/> */}
              <Route path="/components/Login" element={<Login />}/>
              <Route path="/components/Home" element={<Home />}/>
              <Route path="/components/Mainpage" element={<Mainpage />}/>
              <Route path="/components/About" element={<About />}/>
              <Route path="/:id" element={<CarDetail /> }/>
              
            </Routes>
          </main>
        </>
  );
}

export default App;
