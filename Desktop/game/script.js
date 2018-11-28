//No questions asked yet

let count = 0;

//asking questions

let answer1 = prompt("What is Ashley's nickname?");
if (answer1.toUpperCase() === 'ASH') {
  count += 1;
  document.write('Correct answer!');
} else {
  document.write('Ooh, bummer.');
}

document.write('Next question: ');

let answer2 = prompt("What is Isabelle's nickname?");
if (answer2.toUpperCase() === 'IZZY') {
  count += 1;
  document.write('Correct answer!');
} else {
  document.write('Ooh, bummer.');
}
