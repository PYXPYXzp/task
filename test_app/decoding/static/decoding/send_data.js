$(document).ready(function() {
    $("#decoding").bind('textchange', function () {
        var text = $('#decoding').val();
        changed_text(text)
    });


    $("#encode, #decode").click(function () {
        var id = $(this).attr("id");
        var shift = $('#shift').val();
        var text = $('#decoding').val();
        if (validate(text, shift)!= false){
            decode_text(id, shift, text);
        }
    });


    function decode_text(id, shift, text) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: '/decoding/',
            type: 'post',
            dataType: 'json',
            data: {
                type: id,
                text: text,
                shift: shift
            },
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function (data) {
                $("#result").val(data['result']);
            }
        })
    }


    function changed_text(text) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: '/change_text/',
            type: 'post',
            dataType: 'json',
            data: {text: text},
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function (data) {
                // вывод предпологаемого сдвига
                if (data['max_hit_shift'] != 0) {
                    document.getElementById("pos_shift").innerHTML =
                        JSON.stringify(data['max_hit_shift']);
                }
                $('#canvas').remove(); // удалить устаревшую диаграмму
                //добавить новый селектор в который вставим новую диаграмму с обновленными данными
                $('#canvas_container').append('<canvas id="canvas" height="150" width="600"><canvas>');
                drawChart(data['result_count_all'])
            },
            error: function () {
                alert("Ошибка: ");
            }
        });
    }

    function validate(text, shift){

        if (text.length == 0) {
            alert('Введите текст');
            return false;
        }
        if (shift.length == 0){
            alert('Введите смещение');
            return false;
        }
        if (shift.match(/^[-\+]?\d+/) === null) {
            alert('В поле "смещение" введите число');
            return false;
        }

    }
});