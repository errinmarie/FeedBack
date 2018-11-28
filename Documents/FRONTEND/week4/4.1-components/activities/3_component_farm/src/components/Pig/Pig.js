import React, { Component } from 'react';
import './Pig.css';
import pigImage from './pigsprite.png';

class Pig extends Component <
  {},
  {
    count: number
  }
  > {
    state = {
    count: 0
  };
  
  render() {
    return (
      <div className="Pig">
        <img src={pigImage} alt="pig" />
        <button
        onClick={() => this.setState({ count: this.state.count + 1 })}
        >Feed Me
        </button>
      </div>
    );
  }
}

export default Pig;
