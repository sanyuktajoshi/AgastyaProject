$(document).ready(function() {
  // Hide school name field when the page is ready
  // $("input[name*='school']").hide();
});
$(".outline").on('click', function(e){
  e.preventDefault();
  let id = $(this).attr("name");
  if (id === "login") {
    $("form").animate({
      "right": null,
      "left": "440px"
    }, "swing");
		$("input[name='fullname']").fadeOut("slow").slideUp("slow");
    $("input[name='school']").fadeOut("slow").slideUp("slow");
		$(".formButton").text('Login');
    $(".formButton").attr("name","login");
  } 
  
  else if (id === "studentsignup") {
    $("form").animate({
      "left": null,
			"right": "440px"
    });
		$("input[name*='name']").fadeIn("slow").slideDown("slow");
    $("input[name*='school']").fadeIn("slow").slideDown("slow");
		$(".formButton").text('Student SignUp');
    $(".formButton").attr("name","studentsignup");
  }
  
  else if (id === "mentorsignup") {
    $("form").animate({
      "left": null,
			"right": "440px"
    });
    $("input[name*='name']").fadeIn("slow").slideDown("slow");
    $("input[name*='school']").fadeOut("slow").slideUp("slow");
		$(".formButton").text('Mentor/Sponsor Sign Up');
    $(".formButton").attr("name","mentorsignup");
  }
});