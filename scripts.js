/Getting
$(function() {
	//when submit is clicked, gather the data on the page:
	$(".submit").on("click", function() {
		var title = $("#title").val()
		var description = $("#description").val();
		var location = $("#location").val();//GET COORDINATES
		var priority = $("#priority option:selected").text();
		myObj = {"title" : title, "description" : description, "location" : location, "priority" : priority};
		alert(myObj["location"]);
		return false;
	});


	//THIS RETURNS THE COORDINATES OF THE PING IN AN ARRAY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	function initMap() {
	  //initialize geocoder
	  var geocoder = new google.maps.Geocoder();
	  //on address submit:
		var address = $('#location').val();
		geocoder.geocode({'address': address}, function(results, status) {
			if (status === 'OK') {
		  		alert(results[0].geometry.location);
				return results[0].geometry.location;
			}
			else {
				alert('invalid address');
		  	}
		});
	}
	return false;
});
