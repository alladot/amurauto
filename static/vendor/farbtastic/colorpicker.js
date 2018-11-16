var picker_widget = "<div id='colorpicker'></div>";

(function($) {
    $(document).ready(function() {
        var id_color = $('#id_font_color');
        $(picker_widget).appendTo(id_color.parent());
        $('#colorpicker').farbtastic($('#id_font_color'));
    });
})(jQuery);