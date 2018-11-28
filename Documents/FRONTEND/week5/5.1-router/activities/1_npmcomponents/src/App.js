import React, { Component } from 'react';
import DatePicker from 'react-date-picker';
import Select from 'react-select';
import logo from './logo.svg';
import './App.css';

const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' }
];

class App extends Component {
  state = {
    date: new Date(),
    selectedOption: null,
  }
  

onChange = date => this.setState({ date })
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
 
        <DatePicker
          onChange={this.onChange}
          value={this.state.date}
        />
           
      </div>  
    );
  }
}

export default App;
