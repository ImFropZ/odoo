odoo.define("custom_snippets.dynamic_snippet_blog", function (require) {
  var PublicWidget = require("web.public.widget");
  var rpc = require("web.rpc");
  var Dynamic = PublicWidget.Widget.extend({
    selector: ".dynamic_snippet_blog",
    start: function () {
      var self = this;
      console.log(self);

      rpc
        .query({
          route: "/total_product_sold",
          params: {},
        })
        .then(function (result) {
          self.$("#total_sold").text(result);
        });
    },
  });
  PublicWidget.registry.dynamic_snippet_blog = Dynamic;
  return Dynamic;
});
