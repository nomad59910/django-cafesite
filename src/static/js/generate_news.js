var url = '/api/news/list/?limit=4'
var is_loading = false

function substr(str, count){
    str = $(str).text()
    var result = str.substring(0, count)

    if (result.length > count){
        while(str[count] != ' '){
            result += str[count]
            count++
        }
    }

    return result;
};

function get_month(date){
    var month = new Date(date).toLocaleString('ru',{ month:  'long',});
    return month.substring(0,3);
}

function get_day(date){
    var date = new Date(date).toLocaleString('ru', { day: 'numeric',});
    if (date.length == 1){
        date = "0" + date;
    }
    return date
}

function load(){
    is_loading = true;
    $.ajax({
        url: url,
        type: "GET",
        dataType: "JSON",
        async: false,
        success: function(data){
            var tmpl = document.getElementById('news-template').innerHTML;
            var news = data['results']

            for(var i = 0; i < news.length; i++){
                news[i].month = get_month(news[i].date)
                news[i]['date_left'] = get_day(news[i].date);
            }
            var html = _.template(tmpl)({items: news})
            $('#content').html($('#content').html() + html);
            url = data['next'];
        }
    });
    is_loading = false;
};

$(document).ready(function() {
    load();

    window.onscroll = function() {
        if($(window).scrollTop()+$(window).height()>=($(document).height() - 300) && (url != undefined) && !is_loading){
            load();
        }
    }
});
