import React, { Component } from 'react';
import './CharacterCard.css';

class CharacterCard extends Component {
  render() {

    return (
        <div className="CharacterCard">
            <img src={this.props.image} alt={this.props.name} />
            <h1>{this.props.name}</h1>
            <p><strong>Bio:</strong> {this.props.bio}</p>
            <p><strong>Birth Year:</strong> {this.props.birthYear}</p>
            <p><strong>Species:</strong> {this.props.species}</p>
            {
              this.props.ring ? (
                <p><strong>Ring of Power:</strong> {this.props.ring}</p>
              ) : (
                null
              )
            }
            <p><strong>Title:</strong> {this.props.title}</p>
        </div>
    );
  }
}

export default CharacterCard;
