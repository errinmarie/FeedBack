import React, { Component } from 'react';
import './CharacterCardGroup.css';

class CharacterCardGroup extends Component {
  render() {
    return (
      <div className="CharacterCardGroup">
        {this.props.children}
      </div>
    );
  }
}

export default CharacterCardGroup;
