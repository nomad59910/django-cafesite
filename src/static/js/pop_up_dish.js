$('body').on('click','.big-link', function(e){
    $('#description-small-btn').css("display", "");
    $('#description-small').css("display", "");

    $('#description').css("display", "");
    $('#block-content-dish').css("visibility", "hidden");
    $('#load-icon').css("visibility", "");

    var url = '/api/product/dish/' + this.id + '/'

    $.ajax({
        url: url,
        type: "GET",
        dataType: "JSON",
        async: false,
        success: function(dish){
            $('#description').html(dish.description);
            $('#description-small').html(dish.description.substring(0,100));
            $('#title_dish').html(dish.name);
            $("#image_dish").attr("src", dish.image);
            $('#price_dish').html(dish.price);
            $('#result_price_dish').html(dish.price);
            $('#add_pop_basket').attr("value", dish.id);
            $('#count_dish').val(1);

            var ingredient_names = [];
            for (var i = 0; i < dish.ingredients.length; i++) {
                ingredient_names.push(dish.ingredients[i].name)
            }

            var html = ingredient_names.join(", ");

            $('#ingredients_dish').html(html);
            $('#load-icon').css("visibility", "hidden");
            $('#block-content-dish').css("visibility", "");
        }
    });
});

$('body').on('click','#description-small-btn', function(e){
    $('#description-small-btn').css("display", "none");
    $('#description-small').css("display", "none");
    $('#description').css("display", "block");
});
