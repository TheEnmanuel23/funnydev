

$(function(){
	var $body = $('body');
	var $post = $('.post-list-container .post-container');
	
	$post.hover(function(e){
		$body.css('overflow-y', 'hidden');
		var $post_zoom = $(e.currentTarget).find('.post-zoom');
		console.log($post_zoom);
		$post_zoom.toggleClass('red');
		/*
		var $background_trans = $('.post-container .post-zoom .background-trans');
		$current_post_readmore_container = $(e.currentTarget).find('.container-read-more');
		$current_post_hover = $(e.currentTarget).find('.post-zoom').find('.background-trans');

		$background_trans.toggleClass('opacity_post');
		$current_post_readmore_container.toggleClass('opacity_readmore');

		$('.post .date').toggleClass('color_gray_post');
		$('.post .title').toggleClass('color_gray_post');
		$('.post .author .createby').toggleClass('color_gray_post');
		$('.post .read-more i').toggleClass('color_gray_post');


		$current_post_hover.removeClass('opacity_post');
		$(e.currentTarget).find('.post').find('.date').removeClass('color_gray_post');
		$(e.currentTarget).find('.post').find('.title').removeClass('color_gray_post');
		$(e.currentTarget).find('.post').find('.author .createby').removeClass('color_gray_post');
		$(e.currentTarget).find('.post').find('.read-more i').removeClass('color_gray_post');
	});

	var $find_control_container = $('.find-control-container');
	var $find_icon_container = $find_control_container.find('.container-icon-search');
	var $icon_search = $find_icon_container.find('i');;



	$icon_search.click(function(){
		var $input = $find_control_container.find('.search');
		$input.fadeToggle( 'fast');
	});
	*/
});