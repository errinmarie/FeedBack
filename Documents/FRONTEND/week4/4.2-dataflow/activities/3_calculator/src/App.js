import React, { Component } from 'react';
import './App.css';

import Calculator from './components/Calculator/Calculator.js';

class App extends Component {
  state = {
    number: '',
  }

  /*
    TODO: Will need to add new methods to implement clicking on numbers and
    other events.
  */

  render() {
    return (
      <div className="App">
        {/* TODO: Will need to replace the event here,
          to add the number to the state... */}
        <Calculator
          testevent={(number) => console.log('testing', number)}
          number={this.state.number} />
      </div>
    );
  }
}

export default App;
