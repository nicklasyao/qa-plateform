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

function setIfSource(param){
    href = $(param).attr('url')
    $('#holder').attr('src', href)
}

// 窗口高度初始化
window.onload = function init(){
    win_height = $('body').innerHeight() * 0.65 + 'px'
    //iframe
    $('#holder').css('min-height', win_height)
    //左侧导航栏
//    $('#left-nav').css('min-height', win_height)
//    $('#left-nav').css('background-color', '#edeff1')
}
