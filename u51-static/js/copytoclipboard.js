function copyToClipboard(text, callback) {

// Spawn an invisible text box (far outside the document),
// put the text in and select it so that the user can copy
// it with the platform specific key combination.

$('<input type="text" class="hidden-copy-input">').appendTo('body')
  .css({ position: 'fixed', top: -1000000, left: -1000000 })
  .val(text)
  // Remove from DOM on unfocus
  .focusout(function() { $(this).remove(); callback(); })
  .select();

}
