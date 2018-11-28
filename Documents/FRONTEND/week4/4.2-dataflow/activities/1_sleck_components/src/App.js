import React, { Component } from 'react';
import './App.css';

import Button from './components/Button/Button.js';

import Nav from './components/Nav/Nav.js';

import avatar from './components/ChatArea/placeholder.svg';
import starEmpty from './components/ChatArea/star_empty.svg';

class App extends Component {
  state = {
    channels: [
      'parking-lot',
      'random',
      'jokes',
    ],
    selectedChannel: 'parking-lot',
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

        <div className="ChannelSelector">
          <div className="ChannelSelector-channelHeader">All Channels</div>
          {
            this.state.channels.map((channelName, index) => (
              this.state.selectedChannel === channelName ? (
                <div key={index} className="ChannelSelector-channel ChannelSelector-channel--selected"># {channelName}</div>
              ) : (
                <div key={index} className="ChannelSelector-channel"># {channelName}</div>
              )
            ))
          }
        </div>

        <div className="ChatArea">
          {
            this.state.messages.map((text, index) => (
              <div key={index} className="ChatArea-message">
                <img className="ChatArea-avatar" src={avatar} alt="avatar" />
                <div className="ChatArea-messageText">
                  <p>{text}</p>
                </div>
                <img className="ChatArea-star" src={starEmpty} alt="avatar" />
              </div>
            ))
          }
        </div>

        <div className="NewMessage">
          <input value={this.state.message} onChange={this.onChangeMessage} placeholder="Type your message" />
          <Button onClick={this.sendMessage}>Send</Button>
        </div>
      </div>
    );
  }
}

export default App;
