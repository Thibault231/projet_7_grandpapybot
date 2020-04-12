jQuery(document).ready(function() {
    initMap();
    $(".my-question").on("click", "#validate", function(){
        $("#loading").css("display", "block");
    }); 
 });