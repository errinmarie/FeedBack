# Lord of the Rings componentization

This is an activity in refactoring, by splitting larger App.js files into
separate components. The end result will look the same, but have neater, DRYer
code.

Getting started:
Either copy the node_modules directory from a previous activity into this
directory (if installation takes too long) OR do "npm install" within this
directory, and then get server started by running:

    npm run start

Challenge #1: console.log, and observe likely component
----------------------

- Add a console.log near the top of the file, above the class App line, to
  ensure you are editing the right file.

- Look closely at the code. Discuss with those nearby you the following
  questions:
    - Do you see repetition? What is the repeated unit?
    - What properties change for each repitition? E.g. what would the "props"
      be?


Challenge #2: Create CharacterCard component
----------------------

1. Create a directory called "components" in "src" to hold all your new
components

2. Create a directory called CharacterCard within "src/components", and a file
called CharacterCard.js
    - Refer to previous activities as a reference for the structure of the file
      for this, such as last class's Farm Component activity

3. Copy over the HTML code from Frodo (or another character) to this new
component




Challenge #2: Add props & use in App.js
----------------------

Using the React feature of "props", add in necessary props to make
CharacterCard be reusable by App.js for each of the 4 characters, and then add
references to CharacterCard within App.js.

Hint 1: To use a prop handed down from the parent, use code like this *within* the
child component's JSX (in this case, within CharacterCard):

    <h1>{this.props.name}</h1>
    <p><strong>Bio:</strong> {this.props.bio}</p>

    {/* Etc... */}

Hint 2: To use a component in App.js, you must import it first, something like:

    import CharacterCard from './components/CharacterCard/CharacterCard.js';

Hint 3: This is how Frodo should be specified in App.js, using the new
CharacterCard component:

    <CharacterCard
        image={frodo}
        name="Frodo Baggins"
        bio={`Frodo comes from the Shire. He inherits the One
            Ring from his cousin (referred to as his uncle) Bilbo
            Baggins and undertakes the quest to destroy it in the
            fires of Mount Doom.`}
        birthYear="2968 Third Age"
        species="Hobbit"
        ring="The One Ring"
        title="Deputy Mayor of Michel Delving, Bearer of the One Ring"
    />





Challenge #3: Move CharacterCard CSS to your new component directory
----------------------

1. Create a new CharacterCard.css file next to your CharacterCard.js file

2. Import it in your CharacterCard.js file with code similar to:
    import './CharacterCard.css'

3. Copy over all the CharacterCard related CSS from your App.css file to your
new file




Challenge #4: Refactor CharacterCardGroup
----------------------

- Follow steps 1-4 to create a new component called  CharacterCardGroup. It
  should be comparatively much simpler than CharacterCard.

- Hint 1: Use "children props" so that you can put the CharacterCards "within"
  the CharacterCardGroup. Within CharacterCardGroup JSX, you can access the
  children like this:

    <div>
        {this.props.children}
    </div>

- Hint 2: In App.js, it will end up looking like this

    <CharacterCardGroup>
        <CharacterCard image={frodo} name="Frodo Baggins" />
        <CharacterCard image={arwen} name="Arwen" /> 
        <CharacterCard image={gandalf} name="Gandalf" />
        <CharacterCard image={legolas} name="Legolas" />
    </CharacterCardGroup>




----------------------

Bonus Challenge: Refactor

Solution found in "AppBonusSolution.js"

* Move the data of the characters into an array of objects

* Use .map to loop through this data, including the Character components as
  necessary

Hint: To "transform" all the properties of an object into props of a component
use the following syntax:

    <ComponentName {...obj} />


