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

  let jsonData = loadJSON("#jsonData");

  // Gathers data from a Diary model
  let data = jsonData.map((item) => {
    const { date_created, mood, sleep } = item;
    return [date_created, mood, sleep];
  });

  // destructured date from jsonData object
  // let date = jsonData.map(({ date_created }) => date_created);

  const months = ["Jan", "Feb", "Mar", "Apr", "June"];
  const labels =
    data[0].length < 3
      ? months
      : data[0].length < 30
      ? data[0]
      : data[0].slice(data[0].length - 30);
  const mood = [];
  const sleep = [];

  // creates charts on a canvas element
  new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        {
          data: mood,
          label: "Mood",
          // This binds the dataset to the left y-axis
          yAxisID: "left-y-axis",
        },
        {
          data: sleep,
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
