let lettuceCount = 0;

function lettuce() {
  console.log('okay lettuce is getting clicked');
  lettuceCount += 1;

  let lettuceCountSpan = document.querySelector('#lettuce-count');
  lettuceCountSpan.textContent = lettuceCount;
}

function tomato() {
  tomatoCount += 1;
}



