/*

Ask a series of questions
Keep track of the number of questions answered correctly
Display the number of questions correctly answered
Display the number of questions the player got wrong

You got 2 questions right:
You got these questions correct:
You got these questions wrong:

DONE - Use a 2-dimensional array to hold the questions & answers
DONE - Create a 2-dimensional array with at least 3 questions in it

DONE - Use a loop to cycle through each question:
Ask it, and compare the response from the player to the answer in the array
(Use the prompt method to ask the question)

Use a conditional statement to see if the player's answer matches the real answer

When the loop is done, print out the correct answers to the screen
*/


var questions = [
  ["What color are Ashley's eyes?", 'blue'],
  ['Does Errin wear glasses?', 'yes'],
  ['Where does John work?', 'interstate battery'],
  ['What did Isabelle pull out of the lake?', 'scooters']
]

var correctAnswers = 0;
var question;
var answer;
var response;
var correct = [];
var wrong = [];

for (var i = 0; i < questions.length; i+= 1) {
  question = questions[i][0]; 
  answer = questions[i][1];
  response = prompt(question);
  if (response === answer) {
    correctAnswers += 1;
    correct.push(question);
  } else {
    wrong.push(question);
  }
}

html = "You got " + correctAnswers + " question(s) right.";
print(html);
html += '<h2>You got these questions correct:</h2>';
html += buildList(correct);
html += '<h2>You got these questions wrong:</h2>';
html += buildList(wrong);
print(html);

function print(message) {
  var outputDiv = document.getElementById('output');
  outputDiv.innerHTML = message;
}

function buildList(arr) {
  var listHTML = '<ol>';
    for (var i = 0; i < arr.length; i += 1) {
      listHTML += '<li>' + arr[i] + '</li>';
    }
    listHTML += '</ol>';
    return listHTML;
}











