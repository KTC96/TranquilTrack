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
  // and return data as an array
  let data = jsonData.map((item) => {
    const { date_created, mood, sleep } = item;
    return [date_created, mood, sleep];
  });

  // destructured date from jsonData object
  // let date = jsonData.map(({ date_created }) => date_created);

  // displays months if there are less than 3 dates in a Diary model
  const months = ["Jan", "Feb", "Mar", "Apr", "June"];
  // logic to show labels on x-axis
  const labels =
    data[0].length < 3
      ? months
      : data[0].length < 30
      ? data[0]
      : data[0].slice(data[0].length - 30);
  // array for if there is no mood or sleep in a Diary model
  const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  // logic for showing mood on a left of chart
  const mood = data[1].length === 0 ? arr : data[1];
  // logic for showing sleep on the right of chart
  const sleep = data[2].length === 0 ? arr : data[2];

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
