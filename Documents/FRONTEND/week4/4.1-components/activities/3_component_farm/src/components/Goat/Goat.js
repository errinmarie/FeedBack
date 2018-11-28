import React, { Component } from 'react';
import './Goat.css';
import goatImage from './goat.png';

class Goat extends Component {
  render() {
    return (
      <div className="Goat">
        <img src={goatImage} alt="goat" />
        <button>Feed me</button>
      </div>
    );
  }
}

export default Goat;
