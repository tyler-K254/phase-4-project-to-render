import { useState } from "react";

function NewCarForm({ onAddCar }) {
  const [name, setName] = useState("");
  const [model, setModel] = useState("");
  const [image, setImage] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    fetch("http://127.0.0.1:5555/cars", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        model: model,
        image: image,
      }),
    })
      .then((r) => r.json())
      .then((newCar) => {
        onAddCar(newCar);
        setName("");
        setModel("");
        setImage("");
      })
      .catch((error) => {
        console.error("Error adding car:", error);
      });
  }

  return (
    <div className="new-car-form">
      <h2>New Car</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Car name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="text"
          name="model"
          placeholder="Model"
          value={model}
          onChange={(e) => setModel(e.target.value)}
          required
        />
        <input
          type="text"
          name="image"
          placeholder="Image URL"
          value={image}
          onChange={(e) => setImage(e.target.value)}
          required
        />
        <button type="submit">Add Car</button>
      </form>
    </div>
  );
}

export default NewCarForm;
