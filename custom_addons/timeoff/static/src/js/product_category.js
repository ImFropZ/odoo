odoo.define("timeoff.hello_world", function (require) {
  "use strict";

  const publicWidget = require("web.public.widget");
  const core = require("web.core");
  const QWeb = core.qweb;

  publicWidget.registry.hello_world_widget = publicWidget.Widget.extend({
    selector: ".o_hello_world",

    start: async function () {
      const categories = await this._rpc({
        route: "/api/category",
      }).then(function (categories) {
        console.log("Hello");
        return categories;
      });
      this.$el.html(QWeb.render("timeoff.hello_world"));
    },
  });
});
