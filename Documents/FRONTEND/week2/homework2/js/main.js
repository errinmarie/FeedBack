function toggleFahrenheit() {
    console.log('toggling Fahrenheit');
    document.querySelector('.Bars-Far').style.display = "flex";
    document.querySelector('.Bars-Cel').style.display = "none";  
    document.querySelector('.Bars-Precip').style.display = "none";
    document.querySelector('.Nav-Fahrenheit').style.fontWeight = "bold";
    document.querySelector('.Nav-Celcius').style.fontWeight = "normal";
    document.querySelector('.Nav-Precipitation').style.fontWeight = "normal";                                              
}

function toggleCelcius() {
    console.log('toggling Celcius');
    document.querySelector('.Bars-Far').style.display = "none";
    document.querySelector('.Bars-Cel').style.display = "flex";  
    document.querySelector('.Bars-Precip').style.display = "none";
    document.querySelector('.Nav-Fahrenheit').style.fontWeight = "normal";
    document.querySelector('.Nav-Celcius').style.fontWeight = "bold";
    document.querySelector('.Nav-Precipitation').style.fontWeight = "normal";                                                
}
        
function togglePrecipitation() {
    console.log('toggling precipitation');
    document.querySelector('.Bars-Far').style.display = "none";
    document.querySelector('.Bars-Cel').style.display = "none";  
    document.querySelector('.Bars-Precip').style.display = "flex";
    document.querySelector('.Nav-Fahrenheit').style.fontWeight = "normal";
    document.querySelector('.Nav-Celcius').style.fontWeight = "normal";
    document.querySelector('.Nav-Precipitation').style.fontWeight = "bold";                                                
}           

function doFetch() {

fetch("./data/data.json")
    .then(response => response.json())
    .then(data => {
        console.log("Got the data!");
        console.log(data);
        
        for (let datum in data) {
            let chart = document.querySelector(".Bars-Far");
            let height = (data[datum].far);
            chart.innerHTML += `
                <div class="Temp" style="height:${height}%;">
                    <p class="Text">${height}</p>
                </div>
                `;            
        }    
})
}


