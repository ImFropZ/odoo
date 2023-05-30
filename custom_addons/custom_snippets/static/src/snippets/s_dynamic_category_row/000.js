console.log("LOAD from Dynamic Category Row");

odoo.define("custom_snippets.dynamic_category_row_snippet", function (require) {
  var PublicWidget = require("web.public.widget");
  var rpc = require("web.rpc");
  var core = require("web.core");
  var wUtils = require("website.utils");

  var QWeb = core.qweb;

  var Dynamic = PublicWidget.Widget.extend({
    selector: ".dynamic_snippet_category_row",
    start: function () {
      var self = this;

      rpc
        .query({
          route: "/get_product_category_row",
          params: {
            domain: wUtils.websiteDomain(this),
          },
        })
        .then(function (result) {
          console.log(result);
        });
    },
  });

  PublicWidget.registry.dynamic_snippet_category = Dynamic;
  return Dynamic;
});
