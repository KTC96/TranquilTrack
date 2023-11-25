/*
Gathers data from index.html template for sterilizing
 */
const loadJSON = (selector) => {
  return JSON.parse(document.querySelector(selector).getAttribute("data-json"));
};

/*
This function runs when the page loads
 */
window.onload = function () {
  // gets a canvas element from index.html file
  const ctx = document.getElementById("lineChart");

  // Gets element with id from index.html
  let jsonData = loadJSON("#jsonData");

  // Gathers and destructured data from db
  let date = jsonData.map(({ date_created }) => date_created);
  let mood = jsonData.map(({ mood }) => mood);
  let sleep = jsonData.map(({ sleep }) => sleep);

  // Filters all null values from array
  let filtering = (items) => items.filter((e) => e);

  // Displays months if dates less than 3
  const months = ["Jan", "Feb", "Mar", "Apr", "June"];
  // Display data based on logic
  const labels =
    date.length < 3
      ? months
      : date.length < 30
      ? date.slice(date.length - 30)
      : date;
  const moods = mood.length < 3 ? [1] : filtering(mood);
  const sleeps = sleep.length < 3 ? [2] : filtering(sleep);

  // creates charts on a canvas element
  new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        {
          data: moods,
          label: "Mood",
          // This binds the dataset to the left y-axis
          yAxisID: "left-y-axis",
        },
        {
          data: sleeps,
          label: "Sleep",
          // This binds the dataset to the right y-axis
          yAxisID: "right-y-axis",
        },
      ],
      // creates the labels on the x-axis
      labels,
    },
    // options to set with chart
    options: {
      scales: {
        // binds options to the id from above
        "left-y-axis": {
          type: "linear",
          position: "left",
          title: { display: true, text: "Mood" },
        },
        "right-y-axis": {
          type: "linear",
          position: "right",
          title: { display: true, text: "Sleep" },
        },
      },
    },
  });
};
