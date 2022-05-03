

const DEBUGGING=1

function AJAX(method="GET",url="",data={},success,error){
	$.ajax({
	  type: method,
	  // contentType: "application/json",
	  url: url,
	  // data: JSON.stringify(data),
	  headers:{'Authorization':`Bearer ${localStorage.getItem('jwt')}`},
	  dataType: "json",
	  success: success,
	  error: error,
	});
	
}
window.AJAX=AJAX
AJAX('/api/users/profile')
function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
};

function isAdmin(){
	  $.ajax({
	    type: "GET",
	  // contentType: "application/json",
	  url: '/api/users/profile',
	  // data: JSON.stringify(data),
	  headers:{'Authorization':`Bearer ${localStorage.getItem('jwt')}`},
	  dataType: "json",
	  success: (data,textstatus,xhr)=>{
	  	if (DEBUGGING) {
		    console.log(data,'test if user is admin')
	  	}
	    localStorage.setItem('jwt.isAdmin', data.isAdmin)
	    // Swal.fire("Fetched Bookings list from database", JSON.stringify(data), 'success')
	  },
	  error: (data,textstatus,xhr)=>{
	    // alert('user not loggedin or user is not admin')
	    if (DEBUGGING=0) {
	    	console.log("Unable to Check if user is admin")
	    }
	    localStorage.removeItem('jwt')
		  window.location='./sign-in.html'
	  }
	});
}

$(document).ready(function() {
	$('[data-load]').each(function(index, el) {
		$.get($(el).attr('data-load'), function(data) {
			// console.log("LOADED SUCCESS",el)
			$(el).html(data)
		});
	});
});

if(!localStorage.getItem('jwt')){
  window.location='./sign-in.html'
  alert('you need to login before you can use admin panel')
}

