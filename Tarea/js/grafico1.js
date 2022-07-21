var xhr1 = new XMLHttpRequest();

xhr1.onreadystatechange = function(){
    if(xhr1.readyState===4 && xhr1.status===200){
        
        let response = xhr1.responseText;
        let y = [];
        let x = [];

        // 
        // 
       
        response = JSON.parse(response);
        for(i in response){
            x.push(response[i][0]);
            y.push(response[i][1]);
        }
            
        Highcharts.chart('contenedor-1', {

            chart: {
                type: 'line'
                
            },
               title:{
                text: 'Actividades por Día'
               },
               xAxis: {
                  title: {
                    text: 'Días'
                  },
                  categories: x
                },
               yAxis: {
                  title: {
                    text: 'Cantidad de Actividades'
                  }
               },
               series: [{
                  name: 'Actividades',
                  data: y
               }]
        });

    }
}
xhr1.open('GET', 'grafico1.py');
xhr1.send();
