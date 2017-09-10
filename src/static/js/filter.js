function getTypesDishes(){
    var typeDish = document.getElementById('type_dish');
    var elementsTypeDish = typeDish.getElementsByTagName('input');
    var strTypeDish = '';

    for (var i = 0; i < elementsTypeDish.length; i++){
        var input = elementsTypeDish[i];
        if (input.checked){
            if  (strTypeDish == ''){
                strTypeDish = input.value
            }
            else{
                strTypeDish = strTypeDish + ',' + input.value;
            }
        }
    }
    return strTypeDish
}

function getIngredients(){
    var ingredients = document.getElementsByClassName('ingredients');
    var strElementsIngredients = '';
    for (var i = 0; i < ingredients.length; i++){
        var elementsIngredients = ingredients[i].getElementsByTagName('input');
        for (var j = 0; j < elementsIngredients.length; j++){
            var input = elementsIngredients[j];
            if (input.checked){
                if  (strElementsIngredients == ''){
                    strElementsIngredients = input.value
                }
                else{
                    strElementsIngredients = strElementsIngredients + ',' + input.value;
                }
            }
        }
    }
    return  strElementsIngredients;
}

String.prototype.format = String.prototype.f = function () {
    var args = arguments;
    return this.replace(/\{\{|\}\}|\{(\d+)\}/g, function (m, n) {
        if (m == "{{") { return "{"; }
        if (m == "}}") { return "}"; }
        return args[n];
    });
};

function updateMenu(){
    $.ajax({
        url: "/api/product/dish/list/",
        data: {
            'type_dishes' : getTypesDishes(),
            'ingredients' : getIngredients()
        },
        type: "GET",
        dataType: "JSON",
        async: false,
        success: function(data){
            var tmpl = document.getElementById('menu-template').innerHTML;
            var html = _.template(tmpl)({items: data});

            $('#data_dish').html(html);
        }
    });
};

function isEmptyCheckbox(list){
    for (var i = 0; i < list.length; i++){
        if(list[i].checked){
            return true;
        }
    }
    return false;
}

function getFirstWord(str){
    var result_str = ""

    for (var i = 0; i < str.length; i++) {
        if (str[i] == ' '){
            break;
        }
        result_str += str[i];
    }
    return result_str;
}

$(document).ready(function() {
    $('body').on('blur','#count_dish', function(){
        if (this.value == ""){
            this.value = 1;
        }
        var str = $('#price_dish').html();
        var price = str.substr(0, str.length - 2);
        $('#result_price_dish').html((price*this.value) + " ₽");
    });


    $('body').on('click','.ingredient_type', function(){
        var elemCheck = $('.' + this.value);

        for (var i = 0; i < elemCheck.length; i++){
            elemCheck[i].checked = this.checked;
        }
        updateMenu();
    });


    $('body').on('click','div.ingred input', function(){
        var ingredients_type = $(".ingredient_type");
        var className = getFirstWord(this.className);

        for (var i = 0; i < ingredients_type.length; i++){
            if (ingredients_type[i].value == className){
                ingredients_type[i].checked = isEmptyCheckbox($('.' + className));
            }
        }
        updateMenu();
    });


    $('body').on('click','input.type-dish', function(){
        updateMenu();
    });

    $('body').on('click','div.up-or-down', function(){
        var up = $(this).find(".fa-chevron-circle-up");
        var down = $(this).find(".fa-chevron-circle-down");
        var ingreds = $(this).parent().parent().parent();


        if (up[0].style.display == 'block'){
            up[0].style.display = 'none';
            down[0].style.display = 'block';
            $(ingreds).find(".ingredients").removeClass('move-list');
        }
        else{
            down[0].style.display = 'none';
            up[0].style.display = 'block';
            $(ingreds).find(".ingredients").addClass('move-list');
        }
    });

    $(window).scroll(function() {
        var $block = $('.filter-block');

        if($(window).scrollTop() > 545) {
            $block.addClass('filter-fly');
        } else {
            $block.removeClass('filter-fly');
        }
    });

    window.onload = function () {
        modal = $(".filter-block");
        modal.css({'max-height': outerHeight -140});
    }


    $('body').on('click','#all-select', function(){
        var typeDish = document.getElementById('type_dish');
        var elementsTypeDish = typeDish.getElementsByTagName('input');
        var strTypeDish = '';

        for (var i = 0; i < elementsTypeDish.length; i++){
            var input = elementsTypeDish[i];
            input.checked = true;
        }

        var ingredients = document.getElementsByClassName('ingredients');
        var strElementsIngredients = '';
        for (var i = 0; i < ingredients.length; i++){
            var elementsIngredients = ingredients[i].getElementsByTagName('input');
            for (var j = 0; j < elementsIngredients.length; j++){
                input = elementsIngredients[j];
                input.checked = true;
            }
        }

        var ingredients_type = $(".ingredient_type" );
        var className = getFirstWord(this.className);

        for (var i = 0; i < ingredients_type.length; i++){
            ingredients_type[i].checked = true;
        }

        updateMenu();
    });

    $('body').on('click','#all-deselect', function(){
        var typeDish = document.getElementById('type_dish');
        var elementsTypeDish = typeDish.getElementsByTagName('input');
        var strTypeDish = '';

        for (var i = 0; i < elementsTypeDish.length; i++){
            var input = elementsTypeDish[i];
            input.checked = false;
        }

        var ingredients = document.getElementsByClassName('ingredients');
        var strElementsIngredients = '';
        for (var i = 0; i < ingredients.length; i++){
            var elementsIngredients = ingredients[i].getElementsByTagName('input');
            for (var j = 0; j < elementsIngredients.length; j++){
                input = elementsIngredients[j];
                input.checked = false;
            }
        }

        var ingredients_type = $(".ingredient_type" );
        var className = getFirstWord(this.className);

        for (var i = 0; i < ingredients_type.length; i++){
            ingredients_type[i].checked = false;
        }

        $('#data_dish').html("");
    });

    $(".block-type-dish").hover(function(){
        $(this).find(".only")[0].style.display = 'inline-block';
    },function(){
        $(this).find(".only")[0].style.display = 'none';
    });


    $('body').on('click','.only', function(){
        var typeDish = document.getElementById('type_dish');
        var elementsTypeDish = typeDish.getElementsByTagName('input');

        for (var i = 0; i < elementsTypeDish.length; i++){
            var input = elementsTypeDish[i];
            if (input.id == this.id) {
                input.checked = true;
            }
            else{
                input.checked = false;
            }
        }

        updateMenu();
    });
});

updateMenu();
