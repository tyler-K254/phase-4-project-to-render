import { Link } from "react-router-dom";
import React from "react";

function CarCard({ car }) {
  const { id, name, image } = car;

  const handleDeleteClick = () => {
    fetch(`http://127.0.0.1:5555/cars/${id}`, {
      method: "DELETE"
    })
      .then(response => {
        if (response.ok) {
          // Handle successful deletion here (e.g., update state)
          window.location.reload(); // Refresh the page
        } else {
          throw new Error("Failed to delete car");
        }
      })
      .catch(error => console.log(error));
  };

  return (
    <li className="card">
      <Link to={`/${id}`}>
        <img src={image} alt={name} />
      </Link>
      <h4>{name}</h4>
      <button className="delete-button" onClick={handleDeleteClick}>
        Delete
      </button>
    </li>
  );
}

export default CarCard;