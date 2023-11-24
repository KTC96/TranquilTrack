/*
Gathers data from index.html template for sterilizing
 */
function loadJSON(selector) {
  return JSON.parse(document.querySelector(selector).getAttribute("data-json"));
}

window.onload = function () {
  // gets a canvas element from index.html file
  const ctx = document.getElementById("lineChart");

  let jsonData = loadJSON("#jsonData");

  let date = jsonData.map((item) => item.date_created);

  // creates charts on a canvas element
  new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        {
          data: [20, 50, 100, 75, 25, 0],
          label: "Left dataset",

          // This binds the dataset to the left y-axis
          yAxisID: "left-y-axis",
        },
        {
          data: [0.1, 0.5, 1.0, 2.0, 1.5, 10],
          label: "Right dataset",

          // This binds the dataset to the right y-axis
          yAxisID: "right-y-axis",
        },
      ],
      labels: date,
    },
    // options to set with chart
    options: {
      scales: {
        "left-y-axis": {
          type: "linear",
          position: "left",
          title: { display: true, text: "Left Y Axis" },
        },
        "right-y-axis": {
          type: "linear",
          position: "right",
          title: { display: true, text: "Right Y Axis" },
        },
      },
    },
  });
};
