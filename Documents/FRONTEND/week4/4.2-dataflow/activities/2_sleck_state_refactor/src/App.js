import React, { Component } from 'react';
import './App.css';

import Button from './components/Button/Button.js';
import Nav from './components/Nav/Nav.js';
import ChannelSelector from './components/ChannelSelector/ChannelSelector.js';
import ChatArea from './components/ChatArea/ChatArea.js';
import NewMessage from './components/NewMessage/NewMessage.js';

class App extends Component {
  state = {
    messages: [
      'Hi how are you',
      'how are you',
      'pls respond',
      'pls',
    ],

    message: '',
  }

  onChangeMessage = (ev) => {
    this.setState({
      message: ev.target.value,
    });
  }

  sendMessage = () => {
    const messages = this.state.messages.slice(); // duplicate messags
    messages.push(this.state.message); // push to messages
    this.setState({ // set the state with new array
      message: '',
      messages: messages
    });
  }

  render() {
    return (
      <div className="App">
        <Nav />
        <ChannelSelector />
        <ChatArea messages={this.state.messages} />

        {/*
          Challenge #1:
            The goal is to connect the onChangeMessage and onClickSend props in
            the NewMessage component to correspond to the App.js
            onChangeMessage method and the sendMessage method respectively, so
            that the events "go up" from the child to the parent component.
          Hint 1: Add a couple of "new props" in NewMessage below. 
          Hint 2: One line will look like this:
            onChangeMessage={this.onChangeMessage}
        */}
        <NewMessage
          value={this.state.message}
          onChangeMessage={this.onChangeMessage}
          onClickSend={this.sendMessage}
          />
      </div>
    );
  }
}

export default App;
