$(document).ready(function(){
	var newTimelikeHeight = 0.625*$(".timelikeContainer").width();
	$(".timelikeContainer").height(newTimelikeHeight);
	
	$(window).resize(function(){
		newTimelikeHeight = 0.625*$('.timelikeContainer').width();
		$(".timelikeContainer").height(newTimelikeHeight);
		
	});
	var newHeroUnitHeight = 0.5625*$(".heroUnit").width();
	$(".heroUnit").height(newHeroUnitHeight);
	
	$(window).resize(function(){
		newHeroUnitHeight = 0.5625*$(".heroUnit").width();
		$(".heroUnit").height(newHeroUnitHeight);
		
	});
});