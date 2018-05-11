header_links = (selector, img_src) => {
  for (var i = 0; i < 3; ++i) {
    $(selector).append(
        `<div class="group-input3">
          <label>
            Header Link
            <div class="tool-tips">
              <i class="fas fa-info-circle"></i>
              <img src="${img_src}"/>
            </div>
          </label>
          <input name="header-link-text-${i}" placeholder="header link one text"/>
          <input name="header-link-url-${i}" placeholder="header link one url"/>
        </div>`
    )
  }
}