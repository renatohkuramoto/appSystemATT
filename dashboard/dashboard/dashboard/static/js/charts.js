<script type="text/javascript">
    window.onload = function () {
	var options = {
		series: [{
		name: 'Cadastros do dia',
		data: {{ registros | safe }}
	  }],
		chart: {
		height: 350,
		type: 'line',
	  },
	  stroke: {
		width: 7,
		curve: 'smooth'
	  },
	  xaxis: {
		type: 'Data',
		categories: {{ datas | safe }},
	  },
	  title: {
		text: 'Cadastros da semana: {{ total }}',
		align: 'left',
		style: {
		  fontSize: "24px",
		  color: '#666'
		}
	  },
	  fill: {
		type: 'gradient',
		gradient: {
		  shade: 'dark',
		  gradientToColors: [ '#FDD835'],
		  shadeIntensity: 1,
		  type: 'horizontal',
		  opacityFrom: 1,
		  opacityTo: 1,
		  stops: [0, 100, 100, 100]
		},
	  },
	  markers: {
		size: 4,
		colors: ["#FFA41B"],
		strokeColors: "#fff",
		strokeWidth: 2,
		hover: {
		  size: 7,
		}
	  },
	  yaxis: {
		min: 0,
        max: 100,
		title: {
          text: 'Registros (Total)',
          style: {
		  fontSize: "1rem",
		  color: '#666'
		}
		},
	  };
	var chart = new ApexCharts(document.getElementById('chartContainer'), options);
	chart.render();
}
</script>