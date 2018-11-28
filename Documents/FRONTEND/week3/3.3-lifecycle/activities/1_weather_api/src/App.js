import React, { Component } from 'react';
import './App.css';
import oaklandWeather from './oaklandweather.json';

class App extends Component {
  state = {
    description: 'Hit refresh...',
  }


  state = {
    searchBox: 'Oakland, California',
    location: oaklandWeather.name,
    temperature: Math.round(oaklandWeather.main.temp - 273),
    description: oaklandWeather.weather[0].main,
    windSpeed: Math.round(oaklandWeather.wind.speed),
    humidity: Math.round(oaklandWeather.main.humidity),
    pressure: Math.round(oaklandWeather.main.pressure),
  }


  onRefresh = () => {
    console.log('refreshing');
    
    fetch.("http://api.openweathermap.org/data/2.5/weather?q=Oakland,California&appid=0de82b6b4ba5d843dac44bbee4d02543")
    console.log('fetching'):

  }

  render() {

    // Guess what type of weather this is so we can use the
    // appropriate class to style the background conditionally based
    // on the weather that we have
    const appClasses = ['App'];
    const desc = this.state.description.toLowerCase();
    if (desc.includes('clear')) {
      appClasses.push('App--clear');
    } else if (desc.includes('cloud')) {
      appClasses.push('App--cloud');
    } else if (desc.includes('storm')) {
      appClasses.push('App--storm');
    } else if (desc.includes('rain')) {
      appClasses.push('App--rain');
    }

    return (
      <div className={appClasses.join(' ')}>
        <div className="WeatherDashboard">
          <div className="WeatherDashboard-location">
            {this.state.location}
          </div>
          <div className="WeatherDashboard-overview">
            <span className="WeatherDashboard-temperature">
              {this.state.temperature}° <span>C</span>
            </span>
            <div className="WeatherDashboard-description">{this.state.description}</div>
          </div>
          <div className="WeatherDashboard-details">
            <div className="WeatherDashboard-label">Wind</div>
            <div className="WeatherDashboard-data">{this.state.windSpeed} <span>km/h</span></div>
            <div className="WeatherDashboard-label">Humidity</div>
            <div className="WeatherDashboard-data">{this.state.humidity} <span>%</span></div>
            <div className="WeatherDashboard-label">Pressure</div>
            <div className="WeatherDashboard-data">{this.state.pressure}</div>
          </div>
          <div className="Controls">
            {/*
              <input placeholder="Enter location name"
                value={this.state.searchBox}
                />
            */}
            <button
              onClick={this.onRefresh}>Refresh</button>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
