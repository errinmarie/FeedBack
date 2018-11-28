/*
    Scenario: You landed a job as a front end engineer at a new start-up called
    Cognize. You aren't clear on what the company does, but you are given a
    series of tasks to improve the homepage.
*/

console.log('page loading');

/*
    Challenge #1: Loading this script
    1. Add a console.log to this script file to check if it's being loading.

      Hint: It isn't.

    2. Figure out why it isn't being loaded.

    3. Can you identify the problem? Fix it, and confirm that the console.log
    shows the script being loaded.

      Hint: The problem is it is not getting included via a script tag in the
      HTML.
*/


/*
    Challenge #2: Try Cognize Button
    1. This function is supposed to run and change the text when you click the
    Try Cognize button at the top of the page.
    2. Can you debug the error, and why it is not changing the text?

    Hint: It's not ".text", but something else.....
*/

function tryCognize() {
    let element = document.querySelector('h1');
    element.textContent = 'Bé Cognizé';
}


/*
    Challenge #3: "Accordion" effect

    - The Learn More button is supposed to toggle the visibility of the div
      with ID more-info. This is sometimes called an accordion effect.
      
*/

function toggleLearnMore() {
    console.log('toggling learn more');
    let accordion = document.querySelector('#more-info');
    accordion.classList.toggle('Accordion--collapsed');
    
}

/*
    1. Create a new function
    
    2. Use an onClick event to trigger this function when the Learn More button
    is pressed. Ensure it works using console.log.

    3. Inside this function, access from the page the element with the class of
    "Accordion" ("accordians" are types of visual elements that slide in and
    out to show or hide as needed)

    4. To cause the element to "collapse" or "expand", toggle the class
    "Accordion--collapsed" on the element. The CSS is already done for you, you
    just need to toggle the class.

    Hint #1: This one is tricky! Use previous code as a basis for making the
    onClick and such.

    Hint #2: Take it just one bit at a time. Use console.log to make sure each
    part of it works.

    Hint #3: Use something like this to toggle the existence of a class:
    someElementVariable.classList.toggle('name-of-class');

    More info here: https://alligator.io/js/classlist/


    Bonus: Can you figure out how it is doing the sliding animation?
*/


/*
    Challenge #4: Toggle arrow

    Similar to before, but make the text on the previous button alternate the
    arrow used in the text, either ↑ or ↓
*/


/*
    Bonus Challenge: Decipher Terrible Code

    A developer who is no longer with Cognizé wrote code to put logos on the
    page. Figure where this code is, and see if you can decipher the hideous
    code, and then rewrite it in a cleaner way. It's okay if it is not 100% the
    same behavior, as long as its mostly the same.

    (Good luck, you'll need it!)
*/


