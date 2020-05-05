$(document).ready(function() {
	$("#id_location").focusout(function () {
		var address = $("#id_location").val();

		var geocoder = new google.maps.Geocoder();

		geocoder.geocode( { 'address': address}, function(results, status) {

		  if (status == google.maps.GeocoderStatus.OK) {
		    var latitude = results[0].geometry.location.lat();
		    var longitude = results[0].geometry.location.lng();
		    
		    $("#id_latitude").show();
		    $("#id_latitude").show();
		    $("#id_latitude").val(latitude);
		    $("#id_longitude").val(longitude);
		   	$("#id_latitude").hide();
		    $("#id_latitude").hide();

		  } 
		  else {
		  	alert("Please enter a valid address."); 
		  	return false;
		  }
		}); 
	});

	$("#search_btn").click(function() {
		var tag = $("#tag").val();

		if (tag != "")
				window.location.href = "filter/" + tag; 
		else 
			return false;
	});
});