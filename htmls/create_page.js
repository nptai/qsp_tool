generate_links = (selector_name, scope, img_src) => {
  let selector = $(selector_name);
  for (let i = 0; i < 3; ++i) {
    selector.append(
      `
      <div class="group-input3">
        <label>
          ${scope.charAt(0).toUpperCase()+scope.slice(1).toLowerCase()} Link
          <div class="tool-tips">
            <i class="fas fa-info-circle"></i>
            <img src="${img_src}"/>
          </div>
        </label>
        <input name="${scope}-link[${i}][text]" placeholder="${scope} link ${i+1} text"/>
        <input name="${scope}-link[${i}][url]" placeholder="${scope} link ${i+1} url"/>
      </div>`
    );
  }
};

change_state = (state, a, b) => {
  switch (state) {
    case "2":
      a.show();
      b.hide();
      break;

    case "1":
      b.show();
      a.hide();
      break;

    default:
      a.hide();
      a.hide();
  }
}

on_change_buy_button = (obj) => {
  let state = (obj.value || obj.options[obj.selectedIndex].value);
  let bb_code = $("#buy-button-code");
  let bb_image = $("#buy-button-image");

  change_state(state, bb_image, bb_code);
};

on_change_iv = (obj, selector, id) => {
  let state = (obj.value || obj.options[obj.selectedIndex].value);
  let image = $(`${selector} #image-${id}`);
  let video = $(`${selector} #video-${id}`);

  change_state(state, video, image)
};

delete_block_iv = (selector_name, model_name, id) => {
  let selector = $(`${selector_name} #${id}`);
  selector.remove();
};

var ids = {};

add_block_iv = (selector_name, model_name) => {
  let selector = $(selector_name);
  if (!(selector_name in ids)) ids[selector_name] = 1;

  let id = ids[selector_name]++;

  selector.append(
    `
    <div class="block" id="${id}">
      <div class="block">
        <div class="group-input3">
          <label>
            Image/Video ${id}
            <div class="tool-tips">
              <i class="fas fa-info-circle"></i>
              <img src="./"/>
            </div>
          </label>
          <select name="${model_name}[${id}][type]" onchange="on_change_iv(this, '${selector_name}', '${id}')">
            <option value="0">Please Select</option>
            <option value="1">Image</option>
            <option value="2">Video</option>
          </select>
        </div>            
        <div class="group-input3">
          <div class="input-file" id="image-${id}" style="display: none;">
            <label>
              Image file
            </label>
            <div class="button">
              <div class="fake-btn">
                <i class="fas fa-upload"></i>
                Choose a file
              </div>
              <input name="${model_name}[${id}][image]" type="file"/>
            </div>
          </div>
          <div id="video-${id}" style="display: none;">
            <label>
              Video Embed Url
            </label>
            <textarea name="${model_name}[${id}][video]"></textarea>            
          </div>
        </div>`
    +
    (id > 1 ?
      `
        <div class="group-input3" id="button">
          <button class="button" type="button" onclick="delete_block_iv('${selector_name}', '${model_name}', '${id}')"> Remove Row </button>
        </div>
      </div>
      ` :
      `
        <div class="group-input3"></div>
      </div>
    `)
    +
    (selector_name === ".body.image-video" ?
      `
      <div class="block">
        <label>
          Image ${id} text Field
          <div class="tool-tips">
            <i class="fas fa-info-circle"></i>
            <img src="./"/>
          </div>
        </label>
        <script> tinymce.init({selector: ".mce"}); </script>
        <div class="mce" id="${model_name}[${id}][image-tf]"></div>
      </div>
    </div>
      ` :
      `
    </div>
    `)
  )
};

delete_video_row = (id) => {
  console.log(id);
  $(id).remove()
}

add_video_row = (selector, id) => {
  selector.append(
    `
      <div class="block" id="video-rows-${id}">
        <div>
        <label> Video Embed Url </label>        
        </div>
        <div class="block">
          <div class="group-input2">
            <textarea name="video-url-${id}"></textarea>
          </div>
          <div class="group-input2" id="button">
            <button class="button" type="button" onclick="delete_video_row('#video-rows-${id}')"> Delete Row </button>
          </div>
        </div>
      </div>
      `
  )
}

on_add_video_row = (obj) => {
  let num = parseInt(obj.value || obj.options[obj.selectedIndex].value);
  let selector = $(".block.video-rows");
  selector.empty();

  for (let i = 0; i < num; ++i) {
    add_video_row(selector, i);
  }
};
