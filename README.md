# Personal Portfolio Contact Form ⚡️ 
> A simple contact form with Javascript with Django REST api at the backend


![GitHub stars](https://img.shields.io/github/stars/santoshrajkumar/Portfolio_Contact_form_with_Javascript_and_Django_REST_api_at_the_Backend) 
![GitHub forks](https://img.shields.io/github/forks/santoshrajkumar/Portfolio_Contact_form_with_Javascript_and_Django_REST_api_at_the_Backend)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/santoshrajkumar/Portfolio_Contact_form_with_Javascript_and_Django_REST_api_at_the_Backend/commits/master)
[![Website shields.io](https://img.shields.io/badge/website-up-yellow)](https://smrcontact.herokuapp.com/)
[![Ask Me Anything !](https://img.shields.io/badge/ask%20me-linkedin-1abc9c.svg)](https://www.linkedin.com/in/santosh-mohan-rajkumar-101180a3/)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## How to generate CSRF token in Javascript for Frontend form submission ??
> use the code snippet below:
```javascript
  function getCookie(name) {
		    var cookieValue = null;
		    if (document.cookie && document.cookie !== '') {
		        var cookies = document.cookie.split(';');
		        for (var i = 0; i < cookies.length; i++) {
		            var cookie = cookies[i].trim();
		            // Does this cookie string begin with the name we want?
		            if (cookie.substring(0, name.length + 1) === (name + '=')) {
		                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                break;
		            }
		        }
		    }
		    return cookieValue;
		}
  var csrftoken = getCookie('csrftoken');
```
> Then use the csrf token generated inside the fetch method as:
```javascript
  headers:{
        'Content-type':'application/json',
        'X-CSRFToken': csrftoken,
      },
```
