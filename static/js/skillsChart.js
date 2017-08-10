var options = {
		responsive: true,
		title: {
			text: 'Skills',
			display: true,
			fontSize: 20,
			fontColor: '#aaa',
			position: 'top',
			display: false
		},
		legend: {
			display: false
		},
	scale: {
		gridLines: {
			color: '#aaa',
			offsetGridLines: true
		},
		ticks: {
			display: false,
			beginAtZero: true,
			stepSize: 30,
			fontColor: "red"
		},
		angleLines: {
			color: '#aaa'
		},
		pointLabels: {
			fontColor: '#aaa',
			fontSize: 12
		}
	}
}
var data = {
    labels: ["Python", "Django", "Javascript (ES6)", "NodeJs", "HTML", "CSS", "C#"],
    datasets: [
        {
            label: "Skill",
            backgroundColor: "rgba(59,179,241,0.9)",
            borderColor: "#10587d",
            pointBackgroundColor: "#298dbf",
            pointBorderColor: "#aaa",
            pointHoverBackgroundColor: "#aaa",
            pointHoverBorderColor: "#298dbf",
            data: [45, 55, 65, 55, 60, 40, 50]
        }
    ]
};

var ctx = document.getElementById('skillsChart');

var myRadarChart = new Chart(ctx, {
    type: 'radar',
    data: data,
    options: options
});