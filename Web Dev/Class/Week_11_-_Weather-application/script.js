document.addEventListener("DOMContentLoaded", () => {
  // variables
  // completeUrl = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}";
  // const apiKey = process.env.API_KEY; // Access the API key from the .env file
  const apiKey = "YOUR_API_KEY";
  const apiUrl = "https://api.openweathermap.org/data/2.5/weather";
  const locationInput = document.getElementById("locationInput");
  const searchButton = document.getElementById("searchButton");
  const locationElement = document.getElementById("location");
  const temperatureElement = document.getElementById("temperature");
  const descriptionElement = document.getElementById("description");

  searchButton.addEventListener("click", () => {
    const location = locationInput.value;
    if (location) {
      fetchWeather(location);
    } else {
      alert("Please enter a location!");
    }
  });

  function fetchWeather(location) {
    const url = `${apiUrl}?q=${location}&appid=${apiKey}&units=metric`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        locationElement.textContent = data.name;
        temperatureElement.textContent = `${Math.round(
          data.main.temp
        )}°C`; /*ALT + 0176*/
        descriptionElement.textContent = data.weather[0].description;
      })
      .catch((error) => console.error("Error in fetching weather data", error));
  }
});
