import React, { Component } from 'react';
import 'CharacterCard.css'

class CharacterCard extends Component {
  render() {
    return (
      <div className="CharacterCard">
                          <img src={frodo} alt="Frodo" />

                          <h1>Frodo Baggins</h1>

                          <p><strong>Bio:</strong> Frodo comes from the Shire.
                          He inherits the One Ring from his cousin (referred to
                          as his uncle) Bilbo Baggins and undertakes the quest
                          to destroy it in the fires of Mount Doom.</p>

                          <p><strong>Birth Year:</strong> 2968 Third Age</p>

                          <p><strong>Species:</strong> Hobbit</p>

                          <p><strong>Ring of Power:</strong> The One Ring</p>

                          <p><strong>Title:</strong> Deputy Mayor of Michel
                          Delving, Bearer of the One Ring, Elf-friend</p>
      </div>
    );
  }
}






                    

