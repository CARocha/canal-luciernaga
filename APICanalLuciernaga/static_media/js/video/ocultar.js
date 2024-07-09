(function($){
    $(document).ready(function() {
        $('#change_id_categoria').hide();

        var selectField = $('#id_categoria'),
        verified_url = $('#id_url'),
        verified_inline = $('.inline-group');

        function Verificar(value) {
            if(value.toUpperCase() == 'SERIE' || value.toUpperCase()=='SERIES'){
                verified_url.parent('div').show();
                verified_inline.show();
            }else{
                verified_url.parent('div').show();
                verified_inline.hide();
            }
        }

        // Verificar(selectField.val());

        selectField.change(function() {
            //Verificar($(this).val());
            var charval = $('#id_categoria option:selected').text();
            Verificar(charval);
        }); 
    
    });

})(jQuery || django.jQuery);
    