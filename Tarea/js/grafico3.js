var xhr3 = new XMLHttpRequest();

xhr3.onreadystatechange = function(){
    if(xhr3.readyState===4 && xhr3.status===200){
        
        let response = xhr3.responseText;
        let grafico31 = [];
        let grafico32 = [];
        let grafico33 = [];
        let mes11 = [];
        let mes21 = [];
        let mes31 = [];
        let mes41 = [];
        let mes51 = [];
        let mes61 = [];
        let mes71 = [];
        let mes81 = [];
        let mes91 = [];
        let mes101 = [];
        let mes111 = [];
        let mes121 = [];
        let mes12 = [];
        let mes22 = [];
        let mes32 = [];
        let mes42 = [];
        let mes52 = [];
        let mes62 = [];
        let mes72 = [];
        let mes82 = [];
        let mes92 = [];
        let mes102 = [];
        let mes112 = [];
        let mes122 = [];
        let mes13 = [];
        let mes23 = [];
        let mes33 = [];
        let mes43 = [];
        let mes53 = [];
        let mes63 = [];
        let mes73 = [];
        let mes83 = [];
        let mes93 = [];
        let mes103 = [];
        let mes113 = [];
        let mes123 = [];
        // 
        // 
        response = JSON.parse(response);
        
        grafico31.push(response[0]); //mañana
        grafico32.push(response[1]); //mediodia
        grafico33.push(response[2]); //tarde
        
        for(g in grafico31){
            let mes = grafico31[g][0];
            
            if(mes!=null) {
                if(mes[0] == "1") {
                    mes11.push(mes[1]);
                  }
                  if(mes[0] == "2") {
                      mes21.push(mes[1]);
                  }
                  if(mes[0] == "3") {
                      mes31.push(mes[1]);
                  }
                  if(mes[0] == "4") {
                      mes41.push(mes[1]);
                  }
                  if(mes[0] == "5") {
                      mes51.push(mes[1]);
                  }
                  if(mes[0] == "6") {
                      mes61.push(mes[1]);
                  }
                  if(mes[0] == "7") {
                      mes71.push(mes[1]);
                  }
                  if(mes[0] == "8") {
                      mes81.push(mes[1]);
                  }
                  if(mes[0] == "9") {
                      mes91.push(mes[1]);
                  }
                  if(mes[0] == "10") {
                      mes101.push(mes[1]);
                  }
                  if(mes[0] == "11") {
                      mes111.push(mes[1]);
                  }
                  if(mes[0] == "12") {
                      mes121.push(mes[1]);
                  }    
            }
        }

        for(g in grafico32){
            let mes = grafico32[g][0];

            if(mes!=null) {
                if(mes[0] == "1") {
                    mes12.push(mes[1]);
                  }
                  if(mes[0] == "2") {
                      mes22.push(mes[1]);
                  }
                  if(mes[0] == "3") {
                      mes32.push(mes[1]);
                  }
                  if(mes[0] == "4") {
                      mes42.push(mes[1]);
                  }
                  if(mes[0] == "5") {
                      mes52.push(mes[1]);
                  }
                  if(mes[0] == "6") {
                      mes62.push(mes[1]);
                  }
                  if(mes[0] == "7") {
                      mes72.push(mes[1]);
                  }
                  if(mes[0] == "8") {
                      mes82.push(mes[1]);
                  }
                  if(mes[0] == "9") {
                      mes92.push(mes[1]);
                  }
                  if(mes[0] == "10") {
                      mes102.push(mes[1]);
                  }
                  if(mes[0] == "11") {
                      mes112.push(mes[1]);
                  }
                  if(mes[0] == "12") {
                      mes122.push(mes[1]);
                  }  
            }
              
        }

        for(g in grafico33){
            let mes = grafico33[g][0];

            if(mes!=null) {
                if(mes[0] == "1") {
                    mes13.push(mes[1]);
                  }
                  if(mes[0] == "2") {
                      mes23.push(mes[1]);
                  }
                  if(mes[0] == "3") {
                      mes33.push(mes[1]);
                  }
                  if(mes[0] == "4") {
                      mes43.push(mes[1]);
                  }
                  if(mes[0] == "5") {
                      mes53.push(mes[1]);
                  }
                  if(mes[0] == "6") {
                      mes63.push(mes[1]);
                  }
                  if(mes[0] == "7") {
                      mes73.push(mes[1]);
                  }
                  if(mes[0] == "8") {
                      mes83.push(mes[1]);
                  }
                  if(mes[0] == "9") {
                      mes93.push(mes[1]);
                  }
                  if(mes[0] == "10") {
                      mes103.push(mes[1]);
                  }
                  if(mes[0] == "11") {
                      mes113.push(mes[1]);
                  }
                  if(mes[0] == "12") {
                      mes123.push(mes[1]);
                  }  
            }
              
        }
        
        

        Highcharts.chart('contenedor-3', {
            chart: {
                type: 'column'
                
            },
               title:{
                text: 'Actividades por Horario'
               },
               
               xAxis: {
                categories:['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                title: {
                    text: 'Meses'
                }
                     
               },
               yAxis: {
                  title: {
                    text: 'Cantidad de Actividades'
                  },
                  
               },
               series: [{
                name: 'Mañana',
                data: [mes11, mes21, mes31, mes41, mes51, mes61, mes71, mes81, mes91, mes101, mes111, mes121]
              }, {
                name: 'Mediodía',
                data: [mes12, mes22, mes32, mes42, mes52, mes62, mes72, mes82, mes92, mes102, mes112, mes122]
              }, {
                name: 'Tarde',
                data: [mes13, mes23, mes33, mes43, mes53, mes63, mes73, mes83, mes93, mes103, mes113, mes123]
              }
            ],
               plotOptions: {
                bar: {
                  dataLabels: {
                    enabled: true
                  }
                }
               }
        });

    }
}
xhr3.open('GET', 'grafico3.py');
xhr3.send();


