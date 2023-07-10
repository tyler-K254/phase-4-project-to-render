import React from 'react';
import { NavLink } from 'react-router-dom';

// const linkStyles = {
//     display: "inline-block",
//     width: "50px",
//     padding: "12px",
//     margin: "0 6px 6px",
//     background: "blue",
//     textDecoration: "none",
//     color: "white",
//   };

function Navbar(){
    return (
        <>
        {/* <hr className='vertical-line'></hr> */}
        {/* <hr className='vertical-line2'></hr> */}
        <div className='navigation-bar'>
          
            <NavLink className='navLink' to ="/components/Home">Home |</NavLink>
            
            <NavLink className='navLink' to ="/components/Mainpage">Car Page |</NavLink>

            <NavLink className='navLink' to ="/components/Login">Login |</NavLink>

            <NavLink className='navLink' to ="/components/About">About</NavLink>
            
            
        </div>
        </>
    )
}

export default Navbar