import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = {
    message: '',
  }
  
  onMessageChange = (ev) => {
    let value = ev.target.value;
    this.setState({
      message: value,
    });
  }
  
  render() {
    return (
      <div className="App">
        <h1 className="App-title">Type a message</h1>
        <input
            placeholder="Type your message"
            value={this.state.message}
            onChange={this.onMessageChange}
          />
        <h1 className="App-title">
          Your message: <br />
        </h1>
      </div>
    );
  }
}

export default App;
