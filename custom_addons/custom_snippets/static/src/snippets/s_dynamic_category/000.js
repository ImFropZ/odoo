console.log("LOAD from Dynamic Category");

odoo.define("custom_snippets.dynamic_category_snippet", function (require) {
  var PublicWidget = require("web.public.widget");
  var rpc = require("web.rpc");
  var core = require("web.core");
  var wUtils = require("website.utils");

  var QWeb = core.qweb;

  var Dynamic = PublicWidget.Widget.extend({
    selector: ".dynamic_snippet_category",
    start: function () {
      var self = this;
      console.log(self);

      rpc
        .query({
          route: "/get_product_category",
          params: {
            domain: wUtils.websiteDomain(this),
          },
        })
        .then(function (result) {
          console.log(result);
          self.$("#total_sold_1").html(
            QWeb.render("custom_snippets.CatagoryContainer", {
              categories: result,
            })
          );
        });
    },
  });

  PublicWidget.registry.dynamic_snippet_category = Dynamic;
  return Dynamic;
});
