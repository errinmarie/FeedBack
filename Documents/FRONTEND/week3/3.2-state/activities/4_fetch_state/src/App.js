import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    username: '',
    results: [],
  }

  onUsernameChange = (ev) => {
    let value = ev.target.value;
    this.setState({
      username: value,
    });
  }

  onSubmit = () => {
      // TODO fill me in
      // HINT: https://api.github.com/users/michaelpb/repos
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src="https://i.imgur.com/IGjUDRd.png" />
          <h1 className="App-title">GitHub Profile Search</h1>
        </header>
        <div className="Form">

          <input
              placeholder="Enter your GitHub username"
              value={this.state.username}
              onChange={this.onUsernameChange}
            />
          <h2>URL: github.com/{this.state.username || '...'}/</h2>
          <button onClick={() => this.onSubmit()}>Submit</button>


          <p>{this.state.results.length === 0 ? 'No results.' : ''}</p>

          {
            this.state.results.map(item => (
              <div>
                <hr />
                <h2>{item.name}</h2>
                <p>{item.description}</p>

              </div>
            ))
          }

          {/*
            <img src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/0.16.1/images/loader-large.gif" />
          */}
        </div>
      </div>
    );
  }
}

export default App;
