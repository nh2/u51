$(document).ready(function(){
	errors();
	liste();
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
	$('.errorlist').each(function(){
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
				text: 'Filter',
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
				width: width+2, // + double border width
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
	$('.filter span').hide();
	var filterinput = $('.listefilter');
	var qtip = filterinput.qtip(filterProperties(filterinput.width(), true));

	// filter textbox
	var table = $('.liste');
	filterinput.keyup(function() {
		showQtipOnText(qtip, this.value);
		$.uiTableFilter(table, this.value);
	});

	filterinput.focus();
}

function liste() {
	var table = $('.liste');
	var rows = $('tbody tr:not(.empty)', table);
	var newempty = $('<tr class="empty nofilter"><td /><td /><td /><td /><td /><td /><\/tr>');

	$('thead th', table).attr('title','Sortieren');

	// table sorting
	table.tablesorter({ sortList: [[0,0]] });
	table.bind('sortStart',function() {
	}).bind('sortEnd',function() {
		$('.empty').remove();
		newempty.insertBefore(rows);
	});


	var pws = $('.pw');

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
				<li class="copy">Kopieren</li>\
				<li class="show">Zeigen</li>\
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

	$('.pwmenu').hoverIntent({
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


$.fn.trSlideUp = function(speed, callback) {
	$(this).css('height',$(this).css('height')).empty().animate({ height: 'hide', opacity: 'hide' }, speed ? speed : 'normal', callback);
}

	// AJAX deletion
	$('form.loeschform').submit(function(){ return false });
	$('.loesch_button').click(function(){
		var button = $(this);
		var tr = button.parents('tr');
		var empty = tr.prev('.empty');
		$.post("/delete/", button.parents('.loeschform').serialize(), function(json){
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

