$(document).ready(function(){
	$('.errorlist').each(function(){
		var el = $(this);
		el.hide();
		var tipel = el.parents('tr').first().find('th').first();
		conts = el.html();
		tipel.qtip({
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
				name: 'red'
			},
			show: {
				delay: 0
			}
		});
	});
});
