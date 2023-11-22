const affirmation = document.getElementById("affirmation");
const api_url =
  "https://api.quotable.io/random?tags=inspirational|motivational";

async function getAffirmation(url) {
  const response = await fetch(url);
  var data = await response.json();
  affirmation.innerHTML = data.content;
}

getAffirmation(api_url);
