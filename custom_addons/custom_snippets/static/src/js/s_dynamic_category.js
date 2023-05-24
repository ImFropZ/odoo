odoo.define("custom_snippets.s_dynamic_category", function (require) {
  "use strict";

  const publicWidget = require("web.public_widget");

  publicWidget.registery.dynamic_category = publicWidget.Widget.extend({
    selector: ".s_dynamic_category",
    // template: "custom_snippets.s_dynamic_category_card",
    // xmlDependencies: [
    //   "/custom_snippets/static/src/xml/s_dynamic_category_card.xml",
    // ],

    start: function () {
      console.log("Hello World");
      this.$el.append("Hello");
    },
  });
});
