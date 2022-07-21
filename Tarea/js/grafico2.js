var xhr2 = new XMLHttpRequest();

xhr2.onreadystatechange = function(){
    if(xhr2.readyState===4 && xhr2.status===200){
        
        let response = xhr2.responseText;
        let grafico2 = [];
        let x = [];
        // 
        // 
        response = JSON.parse(response);
        for(i in response){
            x.push(response[i][0]);
            grafico2.push(response[i]);
        }

        Highcharts.chart('contenedor-2', {

            chart: {
                type: 'pie'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
               title:{
                text: 'Total de Actividades por Tipo'
               },
               series: [{
                  name: 'Porcentaje',
                  data: grafico2
               }]
        });

    }
}
xhr2.open('GET', 'grafico2.py');
xhr2.send();



