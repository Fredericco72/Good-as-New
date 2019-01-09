
var nav_home = "<li><a href='/'>         <i class='fa fa-home fa-5x'>     </i></a></li>" +
               "<li><a href='/customers'><i class='fa fa-user fa-5x'>     </i></a></li>" +
               "<li><a href='/sale'>     <i class='fa fa-euro-sign fa-5x'></i></a></li>" +
               "<li><a href='/purchase'> <i class='fa fa-couch fa-5x'>    </i></a></li>";

$(document).ready(function(){
  $(".nav-home").html(nav_home);
  console.log("Document Loaded");
})