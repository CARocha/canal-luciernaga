window.addEventListener("load", function() {
    (function($) {
        var value_tipo = $("#id_tipo").val();
        if (value_tipo == "1") {
            $(".field-titulo").hide();
            $(".field-descripcion").hide();
            $(".field-youtube_link").hide();
        } else {
            $(".inline-related").hide();
        }
        $("#id_tipo").change(function () {
            var value_tipo = $("#id_tipo").val();
            if (value_tipo == "2") {
                $(".field-titulo").show();
                $(".field-descripcion").show();
                $(".field-youtube_link").show();
                $(".inline-related").hide();

            } else {
                $(".field-titulo").hide();
                $(".field-descripcion").hide();
                $(".field-youtube_link").hide();
                $(".inline-related").show();
            }
        });
    })(django.jQuery);
});