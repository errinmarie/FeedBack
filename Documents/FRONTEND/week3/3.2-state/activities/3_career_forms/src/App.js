import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    name: '',
    dob: '',
    position: 'Pizza Delivery',
    interests: {
      funTimes: false,
      gruelingLabor: true,
      officePolitics: true,
    },
  }

  onNameChange = (ev) => {
    console.log('getting a new value!', value);
    let value = ev.target.value;
    this.setState({
      name: value,
    });
  }
  
  onDOBChange = (ev) => {
    console.log('adding DOB!', value);
    let value = ev.target.value;
    this.setState({
      dob: value,
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src="https://i.imgur.com/91fScLx.png" />
          <h1 className="App-title">Career Assignment Office</h1>

          <h2>Hi, {this.state.name}.</h2>
        </header>
        <div className="Form">

          <h2>Name: {this.state.name}</h2>
          <input
              placeholder="Enter your name"
              value={this.state.name}
              onChange={this.onNameChange}
            />

          <h2>Date of birth: {this.state.dob}</h2>
          <input
              placeholder="Date of birth"
              value={this.state.dob}
              onChange={this.onDOBChange}
            />

          <h2>Most recent position:</h2>
          <p>{this.state.position}</p>
          <textarea
              placeholder="Most recent position"
            />

          <h2>Degrees earned:</h2>

          {/* TODO Add in input for "degrees earned" */}

          <h2>Interests:</h2>

          <label>
            <input
                type="checkbox"
                checked={this.state.interests.funTimes}
              />
            Fun times
          </label>

          <label>
            <input
                type="checkbox"
                checked={this.state.interests.gruelingLabor}
              />
            Grueling labor
          </label>

          <label>
            <input
                type="checkbox"
                checked={this.state.interests.officePolitics}
              />
            Office politics
          </label>



          <h2>Salary calculator</h2>
          <label>
            <input /> x 12 + <input /> (bonus) = {100} bucks
          </label>

          <h2>Prove you are not a robot:</h2>
          <p>We cannot plant career chips in robots. Apologies to
          Bender, Flexo, Boxy, and Calculon units.</p>

          <label style={{background: "green"}}>
            3 + 7 = <input />
          </label>

          <label style={{background: "red"}}>
            6 / 2 = <input />
          </label>

        </div>
      </div>
    );
  }
}

export default App;
