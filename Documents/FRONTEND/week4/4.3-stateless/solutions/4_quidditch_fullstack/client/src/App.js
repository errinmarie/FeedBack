import React, { Component } from 'react';
import './App.css';

import Nav from './components/Nav/Nav.js';
import Character from './components/Character/Character.js';

// Define our App
class App extends Component {
  state = {

    // Define "pool" of available characters
    availableChasers: [],
    availableBeaters: [],
    availableKeepers: [],
    availableSeekers: [],

    // Define which ones we'll be using for this team
    chosenChasers: [],
    chosenBeaters: [],

    // There is only one keeper and one seeker per team
    chosenKeeper: null,
    chosenSeeker: null,
  }

  componentDidMount() {
    this.refreshData()
  }

  refreshData = () => {
    fetch('/api/get/available/')
      .then(response => response.json())
      .then(data => {
        console.log('this is data', data);
        this.setState({
          availableChasers: data.chasers,
          availableBeaters: data.beaters,
          availableKeepers: data.keepers,
          availableSeekers: data.seekers,
        });

        fetch('/api/get/chosen/')
          .then(response => response.json())
          .then(data => {
            console.log('this is data', data);
            this.setState({
              chosenChasers: data.chasers,
              chosenBeaters: data.beaters,
              chosenKeeper: data.keepers[0] || null,
              chosenSeeker: data.seekers[0] || null,
            });
          });
      });
  }

  chooseCharacter = (availableArray, index) => {
    const chosen = availableArray[index];
    const name = chosen.name;
    fetch('/api/choose/' + name + '/', {method: 'POST'})
      .then(response => response.json())
      .then(data => {
        this.refreshData();
      });
  }

  onChooseKeeper = (index) => {
    this.chooseCharacter(this.state.availableKeepers, index);
  }

  onChooseSeeker = (index) => {
    this.chooseCharacter(this.state.availableSeekers, index);
  }

  onChooseChaser = (index) => {
    this.chooseCharacter(this.state.availableChasers, index);
  }

  onChooseBeater = (index) => {
    this.chooseCharacter(this.state.availableBeaters, index);
  }

  render() {
    return (
      <div className="App">
        <Nav />
        <div className="TeamManager">
          <div className="TeamManager-position">
            <h2>Starting Keeper</h2>
            <Character info={this.state.chosenKeeper} />
          </div>

          <div className="TeamManager-position">
            <h2>Roster (Keepers)</h2>
            {
              this.state.availableKeepers.map((character, index) => (
                <Character
                  key={character.name}
                  info={character}
                  onButtonClick={() => this.onChooseKeeper(index)} />
              ))
            }
          </div>

          <div className="TeamManager-position">
            <h2>Starting Seeker</h2>
            <Character info={this.state.chosenSeeker} />
          </div>

          <div className="TeamManager-position">
            <h2>Roster (Seekers)</h2>
            {
              this.state.availableSeekers.map((character, index) => (
                <Character
                  key={character.name}
                  info={character}
                  onButtonClick={() => this.onChooseSeeker(index)} />
              ))
            }
          </div>

          <div className="TeamManager-position">
            <h2>Starting Chasers</h2>
            {
              this.state.chosenChasers.map((character, index) => (
                <Character key={character.name} info={character} />
              ))
            }

          </div>

          <div className="TeamManager-position">
            <h2>Roster (Chasers)</h2>
            {
              this.state.availableChasers.map((character, index) => (
                <Character
                  key={character.name}
                  info={character}
                  onButtonClick={() => this.onChooseChaser(index)} />
              ))
            }
          </div>

          <div className="TeamManager-position">
            <h2>Starting Beaters</h2>
            {
              this.state.chosenBeaters.map((character, index) => (
                <Character key={character.name} info={character} />
              ))
            }

          </div>

          <div className="TeamManager-position">
            <h2>Roster (Beaters)</h2>
            {
              this.state.availableBeaters.map((character, index) => (
                <Character
                  key={character.name}
                  info={character}
                  onButtonClick={() => this.onChooseBeater(index)} />
              ))
            }
          </div>
        </div>
      </div>
    );
  }
}

export default App;
