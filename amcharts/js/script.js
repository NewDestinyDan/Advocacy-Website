/**
 * ---------------------------------------
 * This demo was created using amCharts 5.
 * 
 * For more information visit:
 * https://www.amcharts.com/
 * 
 * Documentation is available at:
 * https://www.amcharts.com/docs/v5/
 * ---------------------------------------
 */

// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
var root = am5.Root.new("chartdiv");
root.dateFormatter.set("dateFormat", "MMM yyyy");

// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);


// Create chart
// https://www.amcharts.com/docs/v5/charts/xy-chart/
var chart = root.container.children.push(am5xy.XYChart.new(root, {
  panX: false,
  panY: false,
  layout: root.verticalLayout,
  paddingTop: 40
}));


// Set colors
chart.get("colors").set("colors", [
  am5.color(0x00ACAC),
  am5.color(0xF99D1C),
  am5.color(0x008888),
  am5.color(0x00d1d1),
  am5.color(0x006464),
  am5.color(0x00ACAC), // This is necessary to make the colors work
  ]);

  // Add cursor
// https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
  behavior: "none"
}));
cursor.lineY.set("visible", false);


// Add scrollbar
// https://www.amcharts.com/docs/v5/charts/xy-chart/scrollbars/
var scrollbarX = am5.Scrollbar.new(root, {
    orientation: "horizontal"
  });

  chart.set("scrollbarX", scrollbarX);

chart.bottomAxesContainer.children.push(scrollbarX);

// Create data
var data = [
  {
    "data_period": "Jan 2019",
    "DHS Total Unique Count": 65864,
    "HRA DV Total Unique Count": 3372,
    "HRA HASA Total Unique Count": 4945,
    "HPD Total Unique Count (105% Est.)": 2737,
    "DYCD Total Unique Count": 291
  },
  {
    "data_period": "Feb 2019",
    "DHS Total Unique Count": 68315,
    "HRA DV Total Unique Count": 3375,
    "HRA HASA Total Unique Count": 4858,
    "HPD Total Unique Count (105% Est.)": 2886,
    "DYCD Total Unique Count": 315
  },
  {
    "data_period": "Mar 2019",
    "DHS Total Unique Count": 64748,
    "HRA DV Total Unique Count": 3428,
    "HRA HASA Total Unique Count": 4836,
    "HPD Total Unique Count (105% Est.)": 2818,
    "DYCD Total Unique Count": 342
  },
  {
    "data_period": "Apr 2019",
    "DHS Total Unique Count": 64317,
    "HRA DV Total Unique Count": 3446,
    "HRA HASA Total Unique Count": 4830,
    "HPD Total Unique Count (105% Est.)": 2859,
    "DYCD Total Unique Count": 368
  },
  {
    "data_period": "May 2019",
    "DHS Total Unique Count": 62785,
    "HRA DV Total Unique Count": 13591,
    "HRA HASA Total Unique Count": 4847,
    "HPD Total Unique Count (105% Est.)": 2753,
    "DYCD Total Unique Count": 360
  },
  {
    "data_period": "Jun 2019",
    "DHS Total Unique Count": 63057,
    "HRA DV Total Unique Count": 3519,
    "HRA HASA Total Unique Count": 4800,
    "HPD Total Unique Count (105% Est.)": 2710,
    "DYCD Total Unique Count": 323
  },
  {
    "data_period": "Jul 2019",
    "DHS Total Unique Count": 63246,
    "HRA DV Total Unique Count": 3701,
    "HRA HASA Total Unique Count": 4830,
    "HPD Total Unique Count (105% Est.)": 2716,
    "DYCD Total Unique Count": 870
  },
  {
    "data_period": "Aug 2019",
    "DHS Total Unique Count": 64826,
    "HRA DV Total Unique Count": 3774,
    "HRA HASA Total Unique Count": 4815,
    "HPD Total Unique Count (105% Est.)": 2860,
    "DYCD Total Unique Count": 402
  },
  {
    "data_period": "Sep 2019",
    "DHS Total Unique Count": 64298,
    "HRA DV Total Unique Count": 3821,
    "HRA HASA Total Unique Count": 4834,
    "HPD Total Unique Count (105% Est.)": 2795,
    "DYCD Total Unique Count": 384
  },
  {
    "data_period": "Jun 2020",
    "DHS Total Unique Count": 59458,
    "HRA DV Total Unique Count": 3717,
    "HRA HASA Total Unique Count": 4449,
    "HPD Total Unique Count (105% Est.)": 1726,
    "DYCD Total Unique Count": 260
  },
  {
    "data_period": "Jul 2020",
    "DHS Total Unique Count": 59317,
    "HRA DV Total Unique Count": 3661,
    "HRA HASA Total Unique Count": 3934,
    "HPD Total Unique Count (105% Est.)": 1631,
    "DYCD Total Unique Count": 343
  },
  {
    "data_period": "Aug 2020",
    "DHS Total Unique Count": 58498,
    "HRA DV Total Unique Count": 3697,
    "HRA HASA Total Unique Count": 4381,
    "HPD Total Unique Count (105% Est.)": 1671,
    "DYCD Total Unique Count": 322
  },
  {
    "data_period": "Sep 2020",
    "DHS Total Unique Count": 59294,
    "HRA DV Total Unique Count": 3849,
    "HRA HASA Total Unique Count": 4317,
    "HPD Total Unique Count (105% Est.)": 1748,
    "DYCD Total Unique Count": 319
  },
  {
    "data_period": "Oct 2020",
    "DHS Total Unique Count": 58450,
    "HRA DV Total Unique Count": 3664,
    "HRA HASA Total Unique Count": 4265,
    "HPD Total Unique Count (105% Est.)": 1750,
    "DYCD Total Unique Count": 351
  },
  {
    "data_period": "Nov 2020",
    "DHS Total Unique Count": 58056,
    "HRA DV Total Unique Count": 3546,
    "HRA HASA Total Unique Count": 4172,
    "HPD Total Unique Count (105% Est.)": 1695,
    "DYCD Total Unique Count": 268
  },
  {
    "data_period": "Dec 2020",
    "DHS Total Unique Count": 59212,
    "HRA DV Total Unique Count": 3555,
    "HRA HASA Total Unique Count": 4068,
    "HPD Total Unique Count (105% Est.)": 1663,
    "DYCD Total Unique Count": 303
  },
  {
    "data_period": "Jan 2021",
    "DHS Total Unique Count": 57736,
    "HRA DV Total Unique Count": 3675,
    "HRA HASA Total Unique Count": 4029,
    "HPD Total Unique Count (105% Est.)": 1612,
    "DYCD Total Unique Count": 257
  },
  {
    "data_period": "Feb 2021",
    "DHS Total Unique Count": 56606,
    "HRA DV Total Unique Count": 3582,
    "HRA HASA Total Unique Count": 3972,
    "HPD Total Unique Count (105% Est.)": 1638,
    "DYCD Total Unique Count": 281
  },
  {
    "data_period": "Mar 2021",
    "DHS Total Unique Count": 56495,
    "HRA DV Total Unique Count": 3807,
    "HRA HASA Total Unique Count": 3871,
    "HPD Total Unique Count (105% Est.)": 1707,
    "DYCD Total Unique Count": 315
  },
  {
    "data_period": "Apr 2021",
    "DHS Total Unique Count": 54976,
    "HRA DV Total Unique Count": 3527,
    "HRA HASA Total Unique Count": 3699,
    "HPD Total Unique Count (105% Est.)": 1722,
    "DYCD Total Unique Count": 317
  },
  {
    "data_period": "May 2021",
    "DHS Total Unique Count": 53661,
    "HRA DV Total Unique Count": 3368,
    "HRA HASA Total Unique Count": 3588,
    "HPD Total Unique Count (105% Est.)": 1732,
    "DYCD Total Unique Count": 331
  },
  {
    "data_period": "Jun 2021",
    "DHS Total Unique Count": 52558,
    "HRA DV Total Unique Count": 3655,
    "HRA HASA Total Unique Count": 3509,
    "HPD Total Unique Count (105% Est.)": 1821,
    "DYCD Total Unique Count": 279
  },
  {
    "data_period": "Jul 2021",
    "DHS Total Unique Count": 50912,
    "HRA DV Total Unique Count": 3642,
    "HRA HASA Total Unique Count": 3469,
    "HPD Total Unique Count (105% Est.)": 1738,
    "DYCD Total Unique Count": 373
  },
  {
    "data_period": "Aug 2021",
    "DHS Total Unique Count": 50235,
    "HRA DV Total Unique Count": 3689,
    "HRA HASA Total Unique Count": 3394,
    "HPD Total Unique Count (105% Est.)": 1707,
    "DYCD Total Unique Count": 373
  },
  {
    "data_period": "Sep 2021",
    "DHS Total Unique Count": 50680,
    "HRA DV Total Unique Count": 3760,
    "HRA HASA Total Unique Count": 3362,
    "HPD Total Unique Count (105% Est.)": 1767,
    "DYCD Total Unique Count": 331
  },
  {
    "data_period": "Oct 2021",
    "DHS Total Unique Count": 52200,
    "HRA DV Total Unique Count": 3837,
    "HRA HASA Total Unique Count": 3220,
    "HPD Total Unique Count (105% Est.)": 1754,
    "DYCD Total Unique Count": 339
  },
  {
    "data_period": "Nov 2021",
    "DHS Total Unique Count": 51351,
    "HRA DV Total Unique Count": 3699,
    "HRA HASA Total Unique Count": 3304,
    "HPD Total Unique Count (105% Est.)": 1735,
    "DYCD Total Unique Count": 319
  },
  {
    "data_period": "Dec 2021",
    "DHS Total Unique Count": 51411,
    "HRA DV Total Unique Count": 3697,
    "HRA HASA Total Unique Count": 3176,
    "HPD Total Unique Count (105% Est.)": 1855,
    "DYCD Total Unique Count": 271
  },
  {
    "data_period": "Jan 2022",
    "DHS Total Unique Count": 51471,
    "HRA DV Total Unique Count": 3773,
    "HRA HASA Total Unique Count": 2946,
    "HPD Total Unique Count (105% Est.)": 2282,
    "DYCD Total Unique Count": 308
  },
  {
    "data_period": "Feb 2022",
    "DHS Total Unique Count": 51131,
    "HRA DV Total Unique Count": 3820,
    "HRA HASA Total Unique Count": 3096,
    "HPD Total Unique Count (105% Est.)": 2379,
    "DYCD Total Unique Count": 290
  },
  {
    "data_period": "Mar 2022",
    "DHS Total Unique Count": 52269,
    "HRA DV Total Unique Count": 4507,
    "HRA HASA Total Unique Count": 3085,
    "HPD Total Unique Count (105% Est.)": 2415,
    "DYCD Total Unique Count": 294
  },
  {
    "data_period": "Apr 2022",
    "DHS Total Unique Count": 52385,
    "HRA DV Total Unique Count": 3608,
    "HRA HASA Total Unique Count": 3090,
    "HPD Total Unique Count (105% Est.)": 2384,
    "DYCD Total Unique Count": 318
  },
  {
    "data_period": "May 2022",
    "DHS Total Unique Count": 52602,
    "HRA DV Total Unique Count": 3683,
    "HRA HASA Total Unique Count": 3130,
    "HPD Total Unique Count (105% Est.)": 2488,
    "DYCD Total Unique Count": 280
  },
  {
    "data_period": "Jun 2022",
    "DHS Total Unique Count": 53819,
    "HRA DV Total Unique Count": 3810,
    "HRA HASA Total Unique Count": 3094,
    "HPD Total Unique Count (105% Est.)": 2533,
    "DYCD Total Unique Count": 362}
]



// Attempt to load data from json file
// am5.net.load("../json/data_from_scraper.json", chart).then(function(result){
//     var data = am5.JSONParser.parse(result.response);
// });

// Create axes
// https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
var xAxis = chart.xAxes.push(am5xy.DateAxis.new(root, {
  baseInterval: {timeUnit: "month", count: 1},
  renderer: am5xy.AxisRendererX.new(root, {}),
  tooltip: am5.Tooltip.new(root, {})
}));


var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
  min: 0,
  renderer: am5xy.AxisRendererY.new(root, {})
}));

// Set up secondary X axis to show sum tooltip for
var xAxis2 = chart.xAxes.push(am5xy.DateAxis.new(root, {
  baseInterval: { timeUnit: "month", count: 1 },
  renderer: am5xy.AxisRendererX.new(root, {
    opposite: true
  }),
  tooltip: am5.Tooltip.new(root, {})
}));

// Disable labels
xAxis2.get("renderer").labels.template.set("forceHidden", true);


// Configure tooltip content using adapter
xAxis2.get("tooltip").label.adapters.add("text", function(text, target) {
  var sum = 0;
  chart.series.each(function(series) {
    var dataItem = series.get("tooltipDataItem");
    var dataName = series.get("name");
    if (dataItem && dataName != undefined) {
      sum += dataItem.get("valueY");
    }
  });
  return "Total: [bold]" + root.numberFormatter.format(sum) + "[/]";
});


// Add legend
// https://www.amcharts.com/docs/v5/charts/xy-chart/legend-xy-series/
var legend = chart.children.push(am5.Legend.new(root, {
  centerX: am5.p50,
  x: am5.p50
}));


// Adding checkboxes to legend
legend.markers.template.setup = function(marker) {
    var check = am5.Graphics.new(root, {
      fill: am5.color(0x000000),
      fillOpacity: 1,
      width: 20,
      height: 20,
      layer: 50,
      svgPath: "M15.75 2.527c-.61-.468-1.46-.328-1.902.32l-6.325 9.255L4.04 8.328a1.3 1.3 0 0 0-1.922-.062 1.505 1.505 0 0 0-.062 2.043s4.234 4.695 4.843 5.168c.61.468 1.457.328 1.903-.32L16.05 4.55c.445-.653.308-1.555-.301-2.024Zm0 0"
    });
    
    check.states.create("disabled", {
      fillOpacity: 0
    });
    
    marker.children.push(check);
}
  

// Add series
// https://www.amcharts.com/docs/v5/charts/xy-chart/series/
function makeSeries(name, fieldName, hidden) {
  if (hidden) {
    var series = chart.series.push(am5xy.ColumnSeries.new(root, {
      xAxis: xAxis2,
      yAxis: yAxis,
      stacked: true,
      valueYField: fieldName,
      valueXField: "data_period"
    }));

    series.data.processor = am5.DataProcessor.new(root, {
      dateFields: ["data_period"],
      dateFormat: "MMM yyyy"
    });
    
    // series.strokes.template.setAll({
    //   forceHidden: true
    // });

    series.data.setAll(data);
  }
  else {
    var series = chart.series.push(am5xy.ColumnSeries.new(root, {
      name: name,
      stacked: true,
      xAxis: xAxis,
      yAxis: yAxis,
      valueYField: fieldName,
      valueXField: "data_period",
      tooltip: am5.Tooltip.new(root, {
        pointerOrientation: "horizontal",
        labelText: "{name}: [bold]{valueY}[/]"
      })
    }));

    // series.columns.template.setAll({
    //   tooltipText: "{valueX.formatDate()}\n{name}\n{valueY}",
    //   tooltipY: am5.percent(10)
    // });
    
    
    legend.data.push(series);
    series.appear();
    
    series.data.processor = am5.DataProcessor.new(root, {
      dateFields: ["data_period"],
      dateFormat: "MMM yyyy"
    });

    series.data.setAll(data);
  }
  
}

xAxis.data.setAll(data);



makeSeries("DHS", "DHS Total Unique Count");
makeSeries("HRA DV", "HRA DV Total Unique Count");
makeSeries("HRA HASA", "HRA HASA Total Unique Count");
makeSeries("HPD (Est.)", "HPD Total Unique Count (105% Est.)");
makeSeries("DYCD", "DYCD Total Unique Count");

makeSeries(undefined, "DHS Total Unique Count", true);


// Make stuff animate on load
// https://www.amcharts.com/docs/v5/concepts/animations/
chart.appear(1000, 100);

