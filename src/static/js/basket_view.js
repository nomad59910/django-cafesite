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

String.prototype.format = String.prototype.f = function () {
	var args = arguments;
	return this.replace(/\{\{|\}\}|\{(\d+)\}/g, function (m, n) {
		if (m == "{{") { return "{"; }
		if (m == "}}") { return "}"; }
		return args[n];
	});
};

function updateBlocks(data){
	var summ = data['order_total']
	$('#summ').html(summ + " <span class='rur'>a</span>");
	$('#fly_basket').html(summ + " <span class='rur'>a</span>");

	dishs = data['products']
	if (dishs.length == 0){
		$('#basket-content').html("");
		$('#empty-basket').css({'visibility' : 'visible'});
		$('#block_order').css({'visibility' : 'hidden'});
	}

	var tmpl = document.getElementById('basket-template').innerHTML;
	var html = _.template(tmpl)({items: dishs});
	$('#basket-content').html(html);
}

function displayBasket(){
	$.ajax({
		url: "/api/basket/cart/get/",
		type: "GET",
		dataType: "JSON",
		async: false,
		success: function(data){
			updateBlocks(data);
		}
	});
}

$(document).ready(function() {
	displayBasket();

	$('body').on('click','.remove', function(){
		$.ajax({
	        url: "/api/basket/cart/remove/",
			data: {'id' : this.value},
	        type: "POST",
	        dataType: "JSON",
	        async: false,
	        success: function(data){
	            displayBasket();
	        }
	    });
	});

	$('body').on('blur','.count_dish', function(){
		if (this.value == ""){
			this.value = 1;
		}

		$.ajax({
			url: "/api/basket/cart/set/",
			data: {
				'productId' : this.id,
				'count' : this.value
			},
			type: "POST",
			dataType: "JSON",
			async: false,
			success: function(data){
				displayBasket();
			}
		});
	});

	$('body').on('click','#button-сheckout', function(){
		var name = $('#name-line').val();
		var number = $('#phone_number').val();
		var comment = $('#comment-line').val();

		if (name == ""){
			$('#incorect').html("Заполните поле 'имя'.")
			return;
		}

		if(number == ""){
			$('#incorect').html("Заполните поле 'телефон'.")
			return;
		}

		$.ajax({
			url: "/send_order/",
			data: {
				'first_name' : name,
				'phone_number' : number,
				'comment' : comment
			},
			type: "POST",
			dataType: "JSON",
			async: false,
			success: function(data){
				document.location.href = "/menu/";
			}
		});
	});
});
