/* This is a bundle that uses RequireJS to pull in dependencies.
   These dependencies are defined in the registry.xml file */


/* do not include jquery multiple times */
if (window.jQuery) {
  define('jquery', [], function() {
    return window.jQuery;
  });
}

require([
  'jquery',
], function($, dep1, logger){
  'use strict';

  // initialize only if we are in top frame
  if (window.parent === window) {
    $(document).ready(function() {
      $('body').addClass('markiezenhof-main');
    });
  }

});