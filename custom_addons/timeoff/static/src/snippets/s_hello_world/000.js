odoo.define("timeoff.hello_world", function (require) {
  "use strict";

  const publicWidget = require("web.public.widget");
  const DynamicSnippet = require("website.s_dynamic_snippet");
  const config = require("web.config");

  const DynamicSnippetHelloWorld = DynamicSnippet.extend({
    selector: ".o_hello_world",
    /**
     * @override
     */
    init: function () {
      this._super.apply(this, arguments);
      this.template_key = "timeoff.hello_world";
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _getQWebRenderOptions: function () {
      return {
        message: "World",
      };
    },
  });

  publicWidget.registry.dynamic_snippet_hello_world = DynamicSnippetHelloWorld;

  return DynamicSnippetHelloWorld;
});
