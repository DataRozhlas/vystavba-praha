$(function() {
    $('#tabulka').DataTable({
        "order": [[ 1, "desc" ]],
        "responsive": true,
        "paging": false,
        "searching": false,
        "info": false,
        "language": {
            "url": "https://interaktivni.rozhlas.cz/tools/datatables/Czech.json" 
        },
    });

    $('#tabulka2').DataTable({
        "order": [[ 1, "desc" ]],
        "responsive": true,
        "info": false,
        "language": {
            "url": "https://interaktivni.rozhlas.cz/tools/datatables/Czech.json" 
        },
    });
} );

Highcharts.chart('graf', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Výstavba v Praze'
    },
    subtitle: {
        text: 'Data: <a href="https://www.cuzk.cz/ruian/RUIAN.aspx">RÚIAN</a>',
        useHTML: true
    },
    xAxis: {
        categories: [2012, 2013, 2014, 2015, 2016, 2017],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Počet postavených nemovitostí',
        }
    },
    tooltip: {
        enabled: false
    },
    plotOptions: {
        column: {
            dataLabels: {
                enabled: true
            }
        }
    },
    credits: {
        text: ""
    },
    legend: {
        enabled: false
    },
    series: [{
        name: 'Kč',
        data: [717, 922, 875, 926, 1038, 1148]
    }]
});