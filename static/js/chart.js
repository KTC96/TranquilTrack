const ctx = document.getElementById("lineChart");

new Chart(ctx, {
  type: "line",
  data: {
    datasets: [
      {
        data: [20, 50, 100, 75, 25, 0],
        label: "Left dataset",

        // This binds the dataset to the left y axis
        yAxisID: "left-y-axis",
      },
      {
        data: [0.1, 0.5, 1.0, 2.0, 1.5, 0],
        label: "Right dataset",

        // This binds the dataset to the right y axis
        yAxisID: "right-y-axis",
      },
    ],
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
  },
  options: {
    scales: {
      "left-y-axis": {
        type: "linear",
        position: "left",
      },
      "right-y-axis": {
        type: "linear",
        position: "right",
      },
    },
  },
});
