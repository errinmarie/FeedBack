import React, { Component } from 'react';
import './Inventory.css';

import Stew from '../Stew/Stew.js';
import Fish from '../Fish/Fish.js';
import Wheat from '../Wheat/Wheat.js';

class Inventory extends Component {
  render() {
    return (
      <div className="Inventory">
        <h1>Inventory</h1>
        <Stew />
        <Fish />
        <Wheat />
      </div>
    );
  }
}

export default Inventory;
