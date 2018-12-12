//function resetId(param){
//$('#navbar ul li').removeClass('active')
//$(param).attr('id', 'active')
////$(param).parent().addClass('active')
//}

function resetClass(){
    $('#navbar ul li').removeClass('active')
    var flag = $('#page_flag').text()
    if (undefined != flag & ''!= flag){
        var selector = '#navbar ul li a:contains("' + flag + '")'
        console.log(selector)
        $(selector).parent().addClass('active')
    }
}