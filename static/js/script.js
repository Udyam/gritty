// Collapse menu

$('.button-collapse').sideNav({menuWidth: 240, activationWidth: 70});

// Responsive font using fittext.js

window.fitText( document.getElementsByTagName('body')[0], 8.0);

// Selecting registration tab or login tab depending upon the url

var url = document.URL; // get the current url of the document
var ele_reg = document.getElementById('reg');
var ele_log = document.getElementById('log');
if ( url.indexOf('register') > -1 ) // it is a register page
{
	
	ele_reg.click(); // manually clicking
}
else if ( url.indexOf('login') > -1 )
{
	
	ele_log.click();
}

// Sending post data over button click

var btn = document.getElementById('submit');
function foo(e) // event
{
	var ele = document.getElementsByClassName('active')[0]; // login or register
	var form = null;
	var req = new XMLHttpRequest();
	var post_data = new Object();

	if ( ele.id == 'log' ) // login form
	{
		form = document.querySelector('#login form');
		var postData = new Object();
		post_data['testId'] = form.testId.value;
		post_data['token'] = form.csrfmiddlewaretoken.value;
		req.open('POST','/accounts/login',true);
		req.send();
	}
	else // must be register
	{
		form = document.querySelector('#register form');
		console.log(form);
		var postData = new Object();
		post_data['email'] = form.email.value;
		post_data['userName'] = form.userName.value;
		post_data['token'] = form.csrfmiddlewaretoken.value;
		req.open('POST','/accounts/register',true);
		req.send();
	}
	console.log(post_data);
}
btn.addEventListener('click',foo,false);
