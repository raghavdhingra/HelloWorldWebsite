$(document).ready(function() {
  
    // Find the initial scroll top when the page is loaded.
    var initScrollTop = $(window).scrollTop();
    
    // Set the image's vertical background position based on the scroll top when the page is loaded.
    $(parallax1).css({'background-position-y' : (initScrollTop/25)+'%'});
    
    // When the user scrolls...
    $(window).scroll(function() {
      
      // Find the new scroll top.
      var scrollTop = $(window).scrollTop();
      
      // Set the new background position.
      $(parallax1).css({'background-position-y' : (scrollTop/25)+'%'});
      
    });
    
  });
  var positionX = 0;
  // const teamInner = document.getElementById("team-member-inner-inner");
  $("#team-arrow-right").click(function(){
    if (positionX <= 2000){
      positionX+=200;
      $("#team-member-inner").animate({scrollLeft: positionX},300);
      return false;
    }
  });
  $("#team-arrow-left").click(function(){
    if (positionX > 0){
      positionX-=200;
      $("#team-member-inner").animate({scrollLeft: positionX},300);
      return false;
    }
  });