var weather = require('weather-js');
 
// Options:
// search:     location name or zipcode
// degreeType: F or C
 
weather.find({search: '94610', degreeType: 'F'}, function(err, result) {
  if(err) console.log(err);
  console.log("Temp: ", result[0].current.temperature);
});

  
