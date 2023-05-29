odoo.define(
  "custom_snippets.dynamic_category_snippet_options",
  function (require) {
    "use strict";

    const options = require("web_editor.snippets.options");
    var wUtils = require("website.utils");

    options.registry.DynamicCategoryOptions = options.Class.extend({
      logStuff: function (previewMode, widgetValue, params) {
        console.log(
          `Preview Mode : ${previewMode}\n Widget Value : ${widgetValue}\n Params : ${JSON.stringify(
            params
          )}\n${JSON.stringify(this)}`
        );
      },
    });
  }
);
