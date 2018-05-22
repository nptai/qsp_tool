setTimeout(function () {
  jQuery(document).ready(function () {
    $('.tooltip').tooltipster();
    $('#add_new_testi').click(function () {
      var divCount = Number(jQuery('.testi-row-check .test-row').length + Number(1));
      var newDiv = '<div class="test-row brdr-btm logo-upload logo-upload-full test-row' + divCount + '">' +
        '<label  class="label-upload">Image/Video</label>' +
        '<select name="testi_img_video" id="testi_img_video' + divCount + '" onchange="return Testimonail(' + divCount + ');">' +
        '<option>Please select</option>' +
        '<option value="image">Image</option>' +
        '<option value="video">Video</option>' +
        '</select>' +
        '<div class="box testi-image-tag' + divCount + '" style="display:none">' +
        '<input type="file" multiple="" data-multiple-caption="{count} files selected" class="inputfile inputfile-1" id="testi_image' + divCount + '" name="testi_image[]">' +
        '<label for="testi_image' + divCount + '"><svg viewBox="0 0 20 17" height="17" width="20" xmlns="http://www.w3.org/2000/svg">' +
        '<path d="M10 0l-5.2 4.9h3.3v5.1h3.8v-5.1h3.3l-5.2-4.9zm9.3 11.5l-3.2-2.1h-2l3.4 2.6h-3.5c-.1 0-.2.1-.2.1l-.8 2.3h-6l-.8-2.2c-.1-.1-.1-.2-.2-.2h-3.6l3.4-2.6h-2l-3.2 2.1c-.4.3-.7 1-.6 1.5l.6 3.1c.1.5.7.9 1.2.9h16.3c.6 0 1.1-.4 1.3-.9l.6-3.1c.1-.5-.2-1.2-.7-1.5z"/></svg> <span>Choose a file</span></label>' +
        '</div>' +
        '<label id="testi-lable' + divCount + '" style="display:none">Video Embed Url</label>' +
        '<textArea name="testi_video[]" id="testi_video' + divCount + '" rows="5" cols="50" style="display:none"></textArea>' +
        '<input onclick="return DeleteTestimonial(' + divCount + ')" class="Publish" style="float:right;" value="Delete Row" type="button"> '
      '</div>';
      $('.testi-row-check').append(newDiv);
      jQuery('.jumbotron1').find('script').each(function (i) {
        eval(jQuery(this).text());
      });
    });


    tinymce.init({
      //selector: "textarea",
      theme: "modern",
      mode: "specific_textareas",
      editor_selector: "mceEditor",
      height: 300,
      paste_data_images: true,
      style_formats_merge: true,
      file_browser_callback_types: 'file image media',
      plugins: [
        "advlist autolink lists link image charmap print preview hr anchor pagebreak",
        "searchreplace wordcount visualblocks visualchars code fullscreen",
        "insertdatetime media nonbreaking save table contextmenu directionality",
        "emoticons template paste textcolor colorpicker textpattern"
      ],
      toolbar1: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
      toolbar2: "print preview media | forecolor backcolor emoticons | sizeselect | bold italic | fontselect |  fontsizeselect",
      fontsize_formats: "8px 10px 12px 14px 18px 24px 36px 40px 42px 45px 48px 50px 55px 60px 65px 70px 75px 80px 85px 90px 95px 100px",
      font_formats: "Fjalla One='Fjalla One', sans-serif;Vernon Adams='Francois One', sans-serif;Pacifico='Pacifico', cursive;Nunito='Nunito', sans-serif;Alfa Slab One='Alfa Slab One', cursive;Monoton='Monoton', cursive;Cinzel Decorative='Cinzel Decorative', cursive;NTR='NTR', sans-serif;Raleway='Raleway', sans-serif;Anton='Anton', sans-serif;Andale Mono=andale mono,times;Arial=arial,helvetica,sans-serif;Arial Black=arial black,avant garde;Book Antiqua=book antiqua,palatino;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Georgia=georgia,palatino;Helvetica=helvetica;Impact=impact,chicago;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco;Times New Roman=times new roman,times;Trebuchet MS=trebuchet ms,geneva;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats",
      image_advtab: true,
      images_upload_url: 'https://quicksalespage.co/pages/uploadimages',
      images_upload_base_path: 'https://quicksalespage.co/images/',
      images_upload_credentials: true,
      relative_urls: false,
      remove_script_host: true,
      document_base_url: "https://quicksalespage.co/images/",
      convert_urls: false,
      images_upload_handler: function (blobInfo, success, failure) {
        var xhr, formData;
        xhr = new XMLHttpRequest();
        xhr.withCredentials = false;
        xhr.open('POST', 'https://quicksalespage.co/pages/uploadimages');

        xhr.onload = function () {
          var json;

          if (xhr.status != 200) {
            failure('HTTP Error: ' + xhr.status);
            return;
          }

          json = JSON.parse(xhr.responseText);

          if (!json || typeof json.location != 'string') {
            failure('Invalid JSON: ' + xhr.responseText);
            return;
          }
          success(json.location);
        };
        unlinkImage();
        formData = new FormData();
        formData.append('file', blobInfo.blob(), blobInfo.filename());
        formData.append('filepath', 'https://quicksalespage.co/');
        formData.append('_csrf', 'uTokGJU1Nq-JnSXSiVx4mAYT8YsZWACqK70NUMwfniMNrhYYNrf7zfc8zmbwZbww0t5N1yLOW1ye0V_8f0kQDw==');
        xhr.send(formData);
      },
      file_picker_callback: function (callback, value, meta) {
        if (value.search("https:") != -1) {
          document.getElementById('Removeimg').value = value;
        }
        if (meta.filetype == 'image') {
          $('#upload').trigger('click');
          $('#upload').on('change', function () {
            var file = this.files[0];
            var reader = new FileReader();
            reader.onload = function (e) {
              callback(e.target.result, {
                alt: ''
              });
            };
            reader.readAsDataURL(file);
          });
        }
      },
      templates: [{
        title: 'Test template 1',
        content: 'Test 1'
      }, {
        title: 'Test template 2',
        content: 'Test 2'
      }]
    });
  });
}, 1600);
setTimeout(function () {
  jQuery(document).ready(function () {
    jQuery("#add_more_image").click(function () {
      var i = Number(jQuery('.more_images_container .form-section').length + Number(1));
      var data = '<div class="form-section" id="more_img_row' + i + '">' +
        '<div class="logo-upload">' +
        '<label>Image Upload</label>' +
        '<div class="box">' +
        '<input type="file" multiple="" data-multiple-caption="{count} files selected" class="inputfile inputfile-1" id="testimonial_more_images-' + i + '" name="testimonial_more_images[]">' +
        '<label for="testimonial_more_images-' + i + '">' +
        '<svg viewBox="0 0 20 17" height="17" width="20" xmlns="http://www.w3.org/2000/svg"></svg> ' +
        '<span>Choose a file</span></label>' +
        '</div>' +
        '</div>' +
        '<div class="logo-upload">' +
        '<input class="Publish" id="remove" onclick="DeleteMoreImg(' + i + ')" type="button" value="Remove">' +
        '</div>' +
        '</div>';
      jQuery(".more_images_container").append(data);
      jQuery('.jumbotron1').find('script').each(function (i) {
        eval(jQuery(this).text());
      });
    });

    jQuery("#add_more_videos").click(function () {
      var i = Number(jQuery('.more_videos_container .form-section').length + Number(1));
      var data = '<div class="form-section brdr-btm" id="more_video_row' + i + '">' +
        '<div class="logo-upload">' +
        '<label>Video Embed</label>' +
        '<textarea id="testimonial_morevideo_embed' + i + '" cols="50" rows="5" name="testimonial_morevideo_embed[]"></textarea>' +
        '</div>' +
        '<div class="logo-upload">' +
        '<input id="remove" onclick="DeleteMoreVideos(' + i + ')" class="Publish" type="button" value="Remove">' +
        '</div>' +
        '</div>';
      jQuery(".more_videos_container").append(data);
      jQuery('.jumbotron1').find('script').each(function (i) {
        eval(jQuery(this).text());
      });
    });
    jQuery('#add_new_row').click(function (e) {
      var j = Number(jQuery('.all_new_rows .image-container').length + Number(1));
      if (j <= 15) {
        var counting = '';
        switch (j) {
          case 1:
            counting = "two";
            break;
          case 2:
            counting = "three";
            break;
          case 3:
            counting = "four";
      …