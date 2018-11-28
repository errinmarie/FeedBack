import React, { Component } from 'react';
import './App.css';

import Button from './components/Button/Button.js';
import Dropdown from './components/Dropdown/Dropdown.js';
import Modal from './components/Modal/Modal.js';

class App extends Component {
  state = {
    counter: 0,
  }

  onButtonClick = () => {
    this.setState({
      counter: this.state.counter + 1,
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Component Library</h1>
        </header>
        <div className="App-library">
          {/*
            Challenge #1: Use the Button component to display a button that
            says "Click to increment" and increments the counter using onButtonClick
          */}

          <h1>Button example:</h1>
          <h4>{this.state.counter}</h4>
          <Button
            buttonText="Hello button world"
            gotClicked={this.onButtonClick}
            />

          {/*
            Challenge #2: Create a separate counter example like above, b
            says "Count" and increments the counter using onButtonClick
          */}
          <p>Second counter: {this.state.counter2}</p>
          <Button
            buttonText="Count"
            gotClicked={this.onButtonClick}
          />
          <Modal
            visible={this.state.modalShowing}
            title="Modal example"
            onDismiss={this.hideModal}>
          </Modal>




          <h1>Modal example</h1>
          <Button
              gotClicked={this.showModal}
              buttonText="Show modal"
            />

          <p>Modal ipsum dolor sit amet,
          consectetur adipiscing elit. Sed at
          metus id tellus vestibulum.</p>


          {/* Challenge #3: Use the Modal component */}



          {/* Challenge #4 & #5: Use the Dropdown component */}
          <h1>Dropdown example</h1>
        </div>
      </div>
    );
  }
}

export default App;
