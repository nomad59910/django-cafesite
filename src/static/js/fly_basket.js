jQuery(document).ajaxSend(function(event, xhr, settings) {
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	function sameOrigin(url) {
		var host = document.location.host;
		var protocol = document.location.protocol;
		var sr_origin = '//' + host;
		var origin = protocol + sr_origin;

		return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
			(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||

			!(/^(\/\/|http:|https:).*/.test(url));
	}
	function safeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	}
});


$(document).ready(function() {
    var symbolRuble = '<span class="rur">a</span>';

    function updateFlyMenu(data){
        $('#fly_basket').html(data['order_total'] + " " + symbolRuble);
        if ($('#fly_basket_popup')) {
            $('#fly_basket_popup').html(data['order_total'] + " " + symbolRuble)
        }
    }

    $('body').on('click','#plus', function(){
        var count = $('#count_dish').val();
        var result_count = parseInt(count, 10) + 1;

        if (result_count > 50){
            return;
        }

        $('#count_dish').val(result_count);
        var str = $('#price_dish').html();
        var price = str

        $('#result_price_dish').html(price * result_count);
    });


    $('body').on('click','#minus', function(){
        var count = $('#count_dish').val();
        var result_count = parseInt(count, 10) - 1;

        if (result_count < 1){
            return;
        }

        $('#count_dish').val(result_count);

        var str = $('#price_dish').html();
        var price = str;

        $('#result_price_dish').html((price*result_count));
    });

    $('body').on('click','.add_basket', function(){

        $.ajax({
			url: "/api/basket/cart/add/",
			data: {
                'count' : 1,
                'productId' : this.value
            },
			type: "POST",
			dataType: "JSON",
			async: false,
			success: function(data){
                updateFlyMenu(data);

                var $block = $('.fly-block');

                $block.addClass('fly-basket-fixed-add');

                function func(phrase, who) {
                    $block.removeClass('fly-basket-fixed-add');
                }

                setTimeout(func, 1000, $block);
			}
		});
    });

    $('body').on('click','#add_pop_basket', function(){
        var count = $('#count_dish').val();

        $.ajax({
			url: "/api/basket/cart/add/",
			data: {
                'count' : count,
                'productId' : this.value
            },
			type: "POST",
			dataType: "JSON",
			async: false,
			success: function(data){
                updateFlyMenu(data);
                var $go_basket = $('#go-to-basket')
                $go_basket.addClass('go-to-menu-update')

                function func( $go_basket) {
                    $go_basket.removeClass('go-to-menu-update')
                }
                setTimeout(func, 1000, $go_basket);
			}
		});
    });

    $.get( "/api/basket/cart/get/", function(data)
    {
        updateFlyMenu(data);
    });
});
