function loadData(data){
	var keys = [];
    var value = [];
	for(var k in data){
        keys.push(k);
        value.push(data[k]);
	}
	var barChartData = {
		labels: keys,
		datasets: [
			{
				fillColor: "rgba(180,200,220,1)",
				strokeColor: "rgba(180,200,220,1)",
				data: value
			}
        ]

	};
	return barChartData
}

function drawChart(data){
		var ctx = document.getElementById("canvas").getContext("2d");
		window.myBar = new Chart(ctx).Bar(loadData(data), {
			responsive : true,
		});
	}
