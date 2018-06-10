init_mce = () => {
    tinymce.init({
        selector: ".tinymce",
        theme: "modern",
        mode: "textareas",
        height: 300,
        plugins: [
            "advlist autolink lists link image charmap media print preview hr anchor pagebreak",
            "searchreplace wordcount visualblocks visualchars code fullscreen",
            "insertdatetime media nonbreaking save table contextmenu directionality",
            "emoticons template paste textcolor colorpicker textpattern"
        ],
        toolbar1: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media",
        toolbar2: "print preview | forecolor backcolor emoticons | sizeselect | fontselect |  fontsizeselect",
        fontsize_formats: "8px 10px 12px 14px 18px 24px 36px 40px 42px 45px 48px 50px 55px 60px 65px 70px 75px 80px 85px 90px 95px 100px",
        font_formats: "Fjalla One='Fjalla One', sans-serif;Vernon Adams='Francois One', sans-serif;Pacifico='Pacifico', cursive;Nunito='Nunito', sans-serif;Alfa Slab One='Alfa Slab One', cursive;Monoton='Monoton', cursive;Cinzel Decorative='Cinzel Decorative', cursive;NTR='NTR', sans-serif;Raleway='Raleway', sans-serif;Anton='Anton', sans-serif;Andale Mono=andale mono,times;Arial=arial,helvetica,sans-serif;Arial Black=arial black,avant garde;Book Antiqua=book antiqua,palatino;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Georgia=georgia,palatino;Helvetica=helvetica;Impact=impact,chicago;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco;Times New Roman=times new roman,times;Trebuchet MS=trebuchet ms,geneva;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats",
        theme_advanced_fonts: "Andale Mono=andale mono,times;" +
        "Arial=arial,helvetica,sans-serif;" +
        "Arial Black=arial black,avant garde;" +
        "Book Antiqua=book antiqua,palatino;" +
        "Comic Sans MS=comic sans ms,sans-serif;" +
        "Courier New=courier new,courier;" +
        "Georgia=georgia,palatino;" +
        "Helvetica=helvetica;" +
        "Impact=impact,chicago;" +
        "Symbol=symbol;" +
        "Tahoma=tahoma,arial,helvetica,sans-serif;" +
        "Terminal=terminal,monaco;" +
        "Times New Roman=times new roman,times;" +
        "Trebuchet MS=trebuchet ms,geneva;" +
        "Verdana=verdana,geneva;" +
        "Webdings=webdings;" +
        "Wingdings=wingdings,zapf dingbats",
        images_upload_url: "/pages/upload_image",
        images_upload_credentials: true,
        relative_urls: false,
        image_title: true,
        automatic_uploads: true,
        file_picker_types: 'image',
        file_picker_callback: function (cb, value, meta) {
            var input = document.createElement('input');
            input.setAttribute('type', 'file');
            input.setAttribute('accept', 'image/*');

            input.onchange = function () {
                var file = this.files[0];

                var reader = new FileReader();
                reader.onload = function () {
                    var id = 'blobid' + (new Date()).getTime();
                    var blobCache = tinymce.activeEditor.editorUpload.blobCache;
                    var base64 = reader.result.split(',')[1];
                    var blobInfo = blobCache.create(id, file, base64);
                    blobCache.add(blobInfo);
                    cb(blobInfo.blobUri(), {title: file.name});
                };
                reader.readAsDataURL(file);
            };

            input.click();
        }
    });
};

on_change_buy_button = (state) => {
    let code = $('#buy-button-code');
    let image = $('#buy-button-image');

    let icode = $('textarea[name="body_bb_code"]');
    let ilink = $('input[name="body_bb_link"]');
    let iimage = $('input[name="body_bb_image"]');

    switch (state) {
        case '2':
            image.show();
            code.hide();
            icode.val('');
            break;

        case '1':
            code.show();
            image.hide();
            ilink.val('');
            iimage.val('');

            break;

        default:
            code.hide();
            icode.val('');

            image.hide();
            ilink.val('');
            iimage.val('');
    }
};

on_change_body_iv = (state, id) => {
    let image = $(`.body.image-video #image-${id}`);
    let video = $(`.body.image-video #video-${id}`);

    let iimage = $(`input[name="body_iv_image_${id}"]`);
    let ivideo = $(`textarea[name="body_iv_video_${id}"]`);

    switch (state) {
        case '2':
            image.hide();
            video.show();
            iimage.val('');
            break;

        case '1':
            video.hide();
            image.show();
            ivideo.val('');
            break;

        default:
            image.hide();
            video.hide();
            iimage.val('');
            ivideo.val('');
    }
};

on_change_testimonial_iv = (state, id) => {
    let image = $(`.testimonial.image-video #image-${id}`);
    let video = $(`.testimonial.image-video #video-${id}`);

    let iimage = $(`input[name="testimonial_iv_image_${id}"]`);
    let ivideo = $(`textarea[name="testimonial_iv_video_${id}"]`);

    switch (state) {
        case '2':
            image.hide();
            video.show();
            iimage.val('');
            break;

        case '1':
            video.hide();
            image.show();
            ivideo.val('');
            break;

        default:
            image.hide();
            video.hide();
            iimage.val('');
            ivideo.val('');
    }
};

add_body_iv = () => {
    for (var i = 0; i < 10; ++i) {
        let selector = $(`.body.image-video #body_${i}`);
        if (selector.css('display') === 'none') {
            selector.show();
            break;
        }
    }
};

delete_body_iv = (id) => {
    $(`select[name="body_iv_type_${id}"]`).val("0");
    on_change_body_iv("0", id);

    $(`#body_iv_textfield_${id}_ifr`).contents().find('body').html("");
    $(`.body.image-video #body_${id}`).hide();
};

add_testimonial_iv = () => {
    for (var i = 0; i < 10; ++i) {
        let selector = $(`.testimonial.image-video #testimonial_${i}`);
        if (selector.css('display') === 'none') {
            selector.show();
            break;
        }
    }
};

delete_testimonial_iv = (id) => {
    $(`.testimonial.image-video #testimonial_${id}`).hide();
    $(`select[name="testimonial_iv_type_${id}"]`).val("0");
    $(`input[name="testimonial_iv_image_${id}"]`).val("");
    $(`textarea[name="testimonial_iv_video_${id}"]`).val("");

};

delete_video_row = (id) => {
    $(`#video-rows-${id}`).hide();
    $(`textarea[name="video_url_${id}"]`).val("");
};

on_add_video_row = (obj) => {
    let num = parseInt(obj.value || obj.options[obj.selectedIndex].value);

    for (let i = 0; i < 4; ++i) {
        if (i < num)
            $(`#video-rows-${i}`).show();
        else
            delete_video_row(i);
    }
};