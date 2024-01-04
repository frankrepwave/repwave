function toggle_visibility(id) {
  var loader = document.getElementById("loader");
  loader.style.display="block";
  setTimeout(function () {
      var e = document.getElementById(id);
      if(e.style.display == 'block')
      e.style.display = 'none';
      else
      e.style.display = 'block';
      loader.style.display='none';
  }, 3000)
}

function generateMeetingSummary(form) {
  // const url = '/api/generate_meeting_summary?';
  // const andSign = '&';
  // const firstNameParam = 'firstName='+form.firstName.value;
  // const lastNameParam = 'lastName='+form.lastName.value;
  // const templateParam = 'template='+form.template.value;
  // const newUrl = encodeURI(url+firstNameParam+andSign+lastNameParam+andSign+templateParam+andSign+additionalInformationParam);
  // print('new URL: ' + newUrl)
  

  fetch(
    "http://127.0.0.1:5000/api/generate_meeting_summary?templateParam=StandardTemplate",
    {            
        headers: { "Content-Type": "application/json" },            
        method: "GET"
    }
   )
  .then(data => {
    alert(data.body);
    // document.getElementById("form").reset();     
  });
  return false;
}