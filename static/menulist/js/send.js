$(function (){
    $("#submit").on("click", function(){ ajax_send(); });
});

function ajax_send(){
    
    var allergy_list    = [];
    $("[name='allergy[]']:checked").each(function(){
        allergy_list.push(this.value);
    })

    var param   = {
        category    : $("[name='category']").val(),
        name        : $("[name='name']").val(),
        breakfast   : $("[name='breakfast']").prop("checked"),
        lunch       : $("[name='lunch']").prop("checked"),
        dinner      : $("[name='dinner']").prop("checked"),
        takeout     : $("[name='takeout']").prop("checked"),
        price       : $("[name='price']").val(),
        allergy     : allergy_list,
    }

    $.ajax({
        url         : "", 
        contentType : 'application/json; charset=utf-8',
        type        : "POST",
        data        : JSON.stringify(param),
    }).done( function(data, status, xhr ) { 
        $("#content").html(data.content);
    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    });

}
