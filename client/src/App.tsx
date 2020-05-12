import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [name, setName] = useState('World');

  const handleClick = async () => {
    const response = await fetch('/api/hello');
    const data = await response.json();
    setName(data);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Hello {name}</p>
        <button onClick={handleClick}>Update name</button>
      </header>
    </div>
  );
}

export default App;
