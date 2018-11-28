let lettuceCount = 0;

function lettuce() {
  lettuceCount += 1;

  let lettuceCountSpan = document.querySelector('#lettuce-count');
  lettuceCountSpan.textContent = lettuceCount;
}

let tomatoCount = 0;
function tomato() {
  tomatoCount += 1;

  let tomatoCountSpan = document.querySelector('#tomato-count');
  tomatoCountSpan.textContent = tomatoCount;
}

let oatsCount = 0;
function oat() {
  oatsCount += 1;

  let oatsCountSpan = document.querySelector('#oats-count');
  oatsCountSpan.textContent = oatsCount;
}


function showTotal() {
  alert(
    'Total lettuce: ' + lettuceCount + '\n' +
    'Total tomatos: ' + tomatoCount + '\n' +
    'Total oats: ' + oatsCount + '\n'
  );
}


function showTotalBonus() {
  document.querySelector('body').innerHTML =
    '<main>' +
      '<h1>Total lettuce: ' + lettuceCount + '</h1>' +
      '<h1>Total tomatos: ' + tomatoCount + '</h1>' +
      '<h1>Total oats: ' + oatsCount + '</h1>' +
    '</main>';
}


