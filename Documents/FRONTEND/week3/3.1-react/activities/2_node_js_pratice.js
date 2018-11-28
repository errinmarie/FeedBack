/*
    This 90s music themed activity is intended to both get you used to using
    node.js, and give you more practice with JavaScript syntax.
*/


console.log('Challenge 1 --------------------------');
/*
    Right now, this will loop through every letter of the song lyrics. Rewrite
    the code so that the string is instead an array, such that it will print
    each phrase (separated with a comma).
    
    Hint 1: You will only need to modify the lyrics variable to accomplish
    this.

    Hint 2: const is the same as let, but you use it for variables you won't be
    re-assigning later on.
*/

const lyrics = ["Hey now", "you're an all-star", "get your game on", "go play"];
for (const lyric of lyrics) {
    console.log(lyric);
}


console.log('Challenge 2 --------------------------');
/*
    Write an if statement that checks both that ableToTouchThis is false, AND
    that the "time" variable is equal to "hammer". Some example code is
    provided and commented out, but the condition is missing
*/
const ableToTouchThis = false;
const time = 'hammer';


if (ableToTouchThis === false && time === 'hammer') {
    console.log("Can't touch this.");
    console.log("Stop! Hammer time.");
}




console.log('Challenge 3 --------------------------');
/*
    Modify the object called barbieGirl so that the if statement prints "Come
    on Barbie, let's go party!".

    Hint: You can do this by only modifying what barbieGirl is being assigned
    to.
*/
const barbieGirl = {
    world: 'barbie',
    life: 'plastic',
    canBrushHair: 'true',
 };

if (barbieGirl.world === 'barbie' &&
        barbieGirl.life === 'plastic' &&
        barbieGirl.canBrushHair) {
    console.log("Come on Barbie, let's go party!");
} else {
    console.log("Challenge 3 broken...");
}




console.log('Challenge 4 --------------------------');
/*
  The following is a while loop. Modify it so that it repeats 5 times.
*/
let timesHit = 0;
while (timesHit < 5) {
    console.log("Hit me baby one more time");
    timesHit = timesHit + 1
}


console.log('Challenge 5 --------------------------');
/*
  Context:
    Node uses the "CommonJS" JavaScript variant to import other code. This is a
    function called "require".
    NOTE: This might be switched in future versions to the "ESM" import syntax,
    so it will get closer to the JSX-variant syntax we will be using in React.
    See: https://nodejs.org/api/esm.html for more information.

  Instructions:
    1. Look up the node documentation for "os": https://nodejs.org/api/os.html

    2. Write the code to print the model of one of the CPUs on your computer
    (such as the first one).
*/
const os = require('os');



console.log('Challenge 6 --------------------------');
/*
  Context: A "callback" is what we call a function that is passed as an
  "argument" to another function, and is called when an operation finishes,
  such as fetching from an API. They are one of the more difficult aspects of
  JavaScript.

  Instructions: Add console.log to log out the "err" and the "data".
    1. Can you figure out what each of these arguments contains?
    2. Can you modify the code to cause "err" to not be null?

  HINT 1: Because callbacks are invoked only later, the output will be after
  everything else.

  HINT 2: fs.readFile is how we access data in the harddrive.
*/
const fs = require('fs');
function callback(err, data) {
    console.log("Baby got (call) back");
}
fs.readFile("2_node_js_practice.js", "utf-8", callback);


console.log('Challenge 7 --------------------------');
/*
  Instructions:

  1. Add a new property to the User class for "email".

  2. Make it so that Alanis's email to be "ironic@dontchathink.com", adding
  console logs as necessary to confirm it is working

  3. Call the logIn method, also adding console logs as necessary to confirm it
  is working
*/
class User {
    constructor(username) {
        this.username = username;
        this.isLoggedIn = false;
    }
    logIn() {
        this.isLoggedIn = true;
    }
}

const user = new User('alanis');
// console.log("Alanis's username is:", user.username);



console.log('Bonus Challenge --------------------------');
/*
Rewrite Challenge 6 using alternative function syntax: () => {}
See the node documentation on FS for clues, as all their examples use this:
https://nodejs.org/api/fs.html
*/


/*
Advanced Challenge --------------------------

Node comes with an HTTP server built-in. Use the following example code to see
if you can build a simple multi-page website using it.

Instructions: 
  1. Write several HTML pages to navigate between using links
  2. Make a button that will count and increment a variable

Hint 1: First step is get the example code running. It might be best to work on
this in a separate file since it is more complicated than the previous activity.

Hint 2: Use backtick "template literal" to apply templating to your HTML
snippets

*/

const http = require('http');

function serve(req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(`
        <h1>Welcome to my site</h1>
    `);
    res.end();
}

const server = http.createServer(serve);
// server.listen(8000); // uncommented this to get the server running

