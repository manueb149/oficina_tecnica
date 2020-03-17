$(document).ready(function() {

    moment.locale('es-do')
    var start = moment();
    var end =  moment().add(7, 'days');

    function cb(start, end) {
        $('#daterangepicker span').html(start.format('D [de] MMMM [del] YYYY') + ' al ' + end.format('D [de] MMMM [del] YYYY'));
    }

    $("#daterangepicker").daterangepicker({
        opens: 'left',
        locale:{
            applyLabel: 'Aplicar',
            cancelLabel: 'Quitar',
            fromLabel: 'Desde',
            toLabel: 'Hasta',
            format: 'LL',
            daysOfWeek: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
            monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
                'Diciembre']
        }
    }, cb);
    cb(start, end);

    var tables = $("table[id^='table']").DataTable({
        "bPaginate": false,
        "bLengthChange": false,
        "bFilter": true,
    });

    $("table[id^='table'] tbody").on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
    } );

    $('#button_table_1').click(function(){
        ids = []
        data = tables.rows('.selected').data();
        dateRange = document.getElementById('daterange').innerHTML
        if(data.length > 0){
            for(i=0; i<data.length; i++){
                ids.push(data[i][0]);
            }
            ids.push(dateRange);
            $.ajax({
                type: 'GET',
                url: '/brigada_reten/brigada_semanal/seleccion/',
                data: {
                    empleados: ids
                },
                success: function(){
                    alert("Datos Seleccionados");
                    window.location.href = '/brigada_reten/brigada_semanal/seleccion/';
                },
            });
        }
    });

    // $('#dl').click(function(){
    //     $.ajax({
    //         type: 'GET',
    //         url: '/brigada_reten/brigada_semanal/seleccion/descarga',
    //         data: {
    //             data: 'OK' 
    //         },
    //         success: function(){
    //             // alert("Datos Seleccionados");
    //             // window.location.href = '/brigada_reten/brigada_semanal/seleccion/';
    //         },
    //     });
    // });
});

