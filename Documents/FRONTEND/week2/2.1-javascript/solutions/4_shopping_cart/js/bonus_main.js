let items = [
  {
    title: "Lettuce",
    description: "Lettuce deliver the finest leaves to you.",
    item: "Leaf of Lettuce",
  },
  {
    title: "Tomato",
    description: "Some same tomato, some say tomahto, we say buy them from us.",
    item: "Tomato",
  },
  {
    title: "Oats",
    description: "Oats and goats and boats and totes.",
    item: "Oat Grain",
  },
];

let totals = {
  Lettuce: 0,
  Oats: 0,
  Tomato: 0,
};

function renderItems() {

  // Grab the shopping div from the page
  let shoppingDiv = document.querySelector('#shopping-items');
  shoppingDiv.innerHTML = ''; // Clear existing contents

  // Loop through the items in our list, creating new elements for each item
  for (let item of items) {

    // Make h1 & p tag for the header and description of each item for sale
    let header = document.createElement('h1');
    header.textContent = item.title;
    shoppingDiv.appendChild(header); // Add header to the div
    let para = document.createElement('p');
    para.textContent = item.description;
    shoppingDiv.appendChild(para); // Add paragraph to the div

    // Make the button
    let button = document.createElement('button');
    button.textContent = 'Buy 1 ' + item.item;

    let title = item.title; // access the title, put it in a variable

    // Add an "onClick" event to the button 
    button.onclick = () => {
      totals[title] += 1;
      renderShoppingCart();
    };
    shoppingDiv.appendChild(button);
  }
}


function renderShoppingCart() {

  // Grab the shopping div from the page
  let shoppingCart = document.querySelector('#shopping-cart');
  shoppingCart.innerHTML = ''; // Clear existing contents

  // Loop through the items in our list, creating new elements for each item
  for (let item of items) {
    let para = document.createElement('p');

    // Grab the value from the object "totals", put it in a separate variable
    let value = totals[item.title];

    // Make h1 & p tag for the header and description of each item for sale
    para.textContent = item.title + ': ' + value;
    shoppingCart.appendChild(para); // Add paragraph to the div
  }
}


function showTotal() {
  // Grab the body from the page
  let body = document.querySelector('body');
  body.innerHTML = '<h1>Order Receipt</h1> <hr />';

  // Loop through the items in our list, creating new elements for each item
  for (let item of items) {
    let header = document.createElement('h2');

    // Grab the value from the object "totals", put it in a separate variable
    let value = totals[item.title];

    // Make h1 & p tag for the header and description of each item for sale
    header.textContent = 'Total ' + item.title + ': ' + value;
    body.appendChild(header); // Add paragraph to the div
  }


  // Make the button
  let button = document.createElement('button');
  button.textContent = 'Next Customer';
  body.appendChild(button);

  // Add an "onClick" event to the button 
  button.onclick = () => {
    location.reload();
  };
}

renderShoppingCart();
renderItems();
