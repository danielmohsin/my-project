import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [randomInt, setRandomInt] = useState(null);

  useEffect(() => {
    // Fetch current time
    fetch('http://127.0.0.1:5001/api/time')
      .then(res => res.json())
      .then(data => {
        setCurrentTime(data.unix_time);
      })
      .catch(error => {
        console.error('Error fetching time:', error);
      });

    // Fetch random integer
    fetch('http://127.0.0.1:5001/api/random')
      .then(res => res.json())
      .then(data => {
        setRandomInt(data.random_int);
      })
      .catch(error => {
        console.error('Error fetching random integer:', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>The current time is {currentTime}.</p>
        {randomInt !== null ? (
          <p>The random integer is: {randomInt}</p>
        ) : (
          <p>Loading random integer...</p>
        )}
      </header>
    </div>
  );
}

export default App;

