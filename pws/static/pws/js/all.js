$(document).ready(function(){
	errors();
	pwlist();
	filter();
});

function errors() {
	function errorProperties(conts) {
		return {
			content: conts,
			position: {
				corner: {
					target: 'rightMiddle',
					tooltip: 'leftTop'
				},
				adjust: {
					y: 5
				}
			},
			style: {
				border: {
					color: '#D62222'
				},
				color: '#D62222',
				background: 'rgba(250,204,204,0.8)',
				name: 'red'
			},
			show: {
				delay: 0
			}
		}
	}
	$('ul.errorlist').each(function(){
		var el = $(this);
		el.hide();
		var tipel = el.parents('tr').first().find('th').first();
		var conts = el.html();
		tipel.qtip(errorProperties(conts));
	});
}

function filter() {
	function filterProperties(width) {
		return {
			content: {
				text: gettext('Filter'),
				// TODO find a way to assign multiple target events
				// instead of using prerender: true
				prerender: true
			},
			position: {
				corner: {
					target: 'bottomLeft',
					tooltip: 'leftTop'
				},
				adjust: {
					y: 5
				}
			},
			style: {
				border: {
					color: '#487858',
					width: 1
				},
				color: '#487858',
				background: 'rgba(224,255,184,0.8)',
				padding: 0,
				width: width + 2, // double border width
				textAlign: 'center',
				fontSize: '.8em',
				name: 'green'
			},
			show: {
				delay: 0
			}
		}
	}
	function showQtipOnText(qtip, text) {
		if(text.length > 0)
			qtip.qtip('show');
		else
			qtip.qtip('hide');
	}
	$('.filter label').hide();
	var filterinput = $('input.pwlistfilter');
	var qtip = filterinput.qtip(filterProperties(filterinput.width(), true));

	// filter textbox
	var on_hide = function(elem){ elem.prev('tr.empty').hide() };
	var on_show = function(elem){ elem.prev('tr.empty:hidden').show() };
	var exclude_filter = function(elem){ return elem.not('.empty') };
	var filtertext = filterinput.text();
	var table = $('table.pwlist');
	filterinput.keyup(function() {
		var new_filtertext = filterinput.val();
		if(filtertext != new_filtertext) {
			filtertext = new_filtertext;
			showQtipOnText(qtip, filtertext);
			$.uiTableFilter(table, filtertext, false, false, on_hide, on_show, exclude_filter);
		}
	});

	filterinput.parents('div:first').submit(function(){ return false });

	filterinput.focus();
}

function init_tablesorter() {
	var table = $('table.pwlist');
	var rows = $('tbody tr:not(.empty)', table);
	var newempty = $('<tr class="empty nofilter"><td /><td /><td /><td /><td /><td /><\/tr>');

	$('thead th', table).attr('title',gettext('Sort'));

	// table sorting
	table.tablesorter({
		sortList: [[0,0]],
		filter: function(row){ return row.not('tr.nofilter') },
		before_replace: function(table){ newempty.insertBefore($(rows)) }
	});
}

function init_passwords_on_hover() {
	var pws = $('td.pw');

	// Remove standard CSS show on hover class
	pws.removeClass('showonhover');

	// Save passwords in the nodes and hide them
	pws.each(function(){
		$(this).data('pw',$(this).text());
	}).empty();

	var pwmenu = $('\
		<div class="pwmenu">\
			<p class="pwfield">•••••</p>\
			<ul class="actions">\
				<li class="copy">'+gettext('Copy')+'</li>\
				<li class="show">'+gettext('Show')+'</li>\
			</ul>\
		</div>\
	').appendTo(pws);

	// Add hover actions to the menu

	function show() {
		var menu = $(this);
		menu.children('.actions').fadeIn('fast');
	}

	function hide() {
		var menu = $(this);
		menu.children('.actions').fadeOut('fast');
	}

	$('.pwmenu', pws).hoverIntent({
		sensitivity: 2, // number = sensitivity threshold (must be 1 or higher)
		interval: 50,   // number = milliseconds for onMouseOver polling interval
		over: show,     // function = onMouseOver callback (required)
		timeout: 100,   // number = milliseconds delay before onMouseOut
		out: hide       // function = onMouseOut callback (required)
	});

	// Copy password to clipboard
	$('.actions .copy', pwmenu).click(function(){
		copyToClipboard($(this).parents('.pw').data('pw'));
	});

	// Show plain password and hide it on unhover
	$('.actions .show', pwmenu).click(function(){
		var self = $(this).hide();
		$('<li>').addClass('plainpw').text(self.parents('.pw').data('pw')).mouseleave(function(){
			$(this).prev().show();
			$(this).remove();
		}).appendTo(self.parent());
	});
}

function init_ajax_delete() {
	$.fn.trSlideUp = function(speed, callback) {
		$(this).css('height',$(this).css('height')).empty().animate({ height: 'hide', opacity: 'hide' }, speed ? speed : 'normal', callback);
	}

	// AJAX deletion
	var deleteform = $('form.deleteform')
	deleteform.submit(function(){ return false });
	$('.delete_button', deleteform).click(function(){
		var button = $(this);
		var tr = button.parents('tr');
		var empty = tr.prev('.empty');
		$.post("/delete/", button.parents('.deleteform').serialize(), function(json){
			if(json['success']) {
				tr.css('background-color', tr.children(':first').css('background-color'));
				tr.children().fadeOut('fast', function(){
					tr.trSlideUp('fast', function(){ $(this).remove() });
					empty.trSlideUp('fast', function(){ $(this).remove() });
				});
			}
		}, 'json');
	});
}

function pwlist() {
	init_tablesorter();

	init_passwords_on_hover();

	init_ajax_delete();
}
