odoo.define("custom_snippets.dynamic_category_snippet", function (require) {
  var PublicWidget = require("web.public.widget");
  var rpc = require("web.rpc");
  var Dynamic = PublicWidget.Widget.extend({
    selector: ".dynamic_snippet_category",
    start: function () {
      var self = this;
      console.log(self);

      self.$("#total_sold_1").text("Hello World");
    },
  });
  PublicWidget.registry.dynamic_snippet_blog = Dynamic;
  return Dynamic;
});
