$(".col-md-4").mouseover(function(){
  $(this).find("h2").css("color","#F26743");
  $(this).find(".read-more").removeClass("flyIn");
  $(this).find(".read-more").addClass("fly");
  
}).mouseout(function(){
  $("h2").css("color","#fff");
  $(this).find(".read-more").removeClass("fly");
  $(this).find(".read-more").addClass("flyIn");
});


$(".username-wrapper").on({
    mouseenter: function () {
        $(".verified").css("opacity", "1");
        $(".verified").css("top", "130%");
    },
    mouseleave: function () {
        $(".verified").css("opacity", "0");
        $(".verified").css("top", "150%");
    }
});
