
  console.log('test');

// Challenge 2: There is a typo preventing this function from running. Can you
// spot it?
  function addComment () {
  console.log('Adding a comment.');

  // Retrieve the textarea & the text the user entered, from the DOM
  let textArea = document.querySelector('#comment-textarea');
  console.log('Text area:', textArea);
  let commentText = textArea.value;
  console.log('Getting comment text', commentText);

  // Create a new div for the new message we will be making
  let newCommentDiv = document.createElement('div');

  // Challenge #3
  // Make the new comment div be in a color of your choice (such as "green" or
  // "tomato").
  // Hint #1: newCommentDiv.style.color = 'SOMETHING GOES HERE';
  // Hint #2: For more documentation on this, check this out:
  // https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style
  
  newCommentDiv.style.color = 'tomato';

  // Challenge #4
  // Get the value of the "Color" input, and make the foreground color of the
  // new comment be the color entered there instead of a hard-coded style as before.
  // Hint: You'll have to change the code you wrote for Challenge #3, to use
  // code similar to retrieving the value of textArea
  newCommentDiv.textContent = commentText;
  console.log(newCommentDiv);

  let commentSectionDiv = document.querySelector('.CommentSection');
  console.log('Comment section div:', commentSectionDiv);
  commentSectionDiv.append(newCommentDiv);


  // Challenge #5
  // Clear the textarea after you submit each comment.
  // Hint: nameOfVariableContainingElement.value = '';

}

/*
  Bonus Challenges:
  - Add a new input for background-color, just like you have one for color, to
    allow customization of the background color of each element.
  - Make it so that newlines in your textarea get converted into separate
    paragraphs (e.g. so that "enter"  works)
    Hint: The easiest way might involve splitting by "\n" and then combining
    with "<p>" tags, and using innerHTML of the commentDiv
  - Make both of the color inputs be a "multiple choice" select dropdown
    element (Harder than you might think!)
    Select Tag help here:
    https://www.w3schools.com/tags/tag_select.asp
*/
