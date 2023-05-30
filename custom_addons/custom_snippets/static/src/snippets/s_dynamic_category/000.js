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
      // Label setup
      var label = self.$el.attr("data-label");
      if (label) {
        self.$("#dynamic-category-label").removeClass("d-none");
        self.$("#dynamic-category-label").text(label);
      } else {
        self.$("#dynamic-category-label").addClass("d-none");
      }

      // Search domain setup
      var websiteIdDomain = wUtils.websiteDomain(this);
      var domain = [...websiteIdDomain];

      self.$el
        .attr("data-category-names")
        .split(",")
        .filter((val) => val !== "")
        .forEach((val) => {
          val = val.trim();
          domain.push(["name", "not ilike", val]);
        });

      rpc
        .query({
          route: "/get_product_category",
          params: {
            domain,
          },
        })
        .then(function (result) {
          self.$("#dynamic-cateogry-container").html(
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
