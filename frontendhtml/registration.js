
function register(){
    var uname = document.Formfill.name.value
    var dateofbirth = document.Formfill.DOB.value
    var email = document.Formfill.Email.value
    var number = document.Formfill.number.value
    var education = document.Formfill.education.value
    var job = document.Formfill.job.value
    var experience = document.Formfill.work_experience.value
    var rurl = document.Formfill.resume_url.value

    console.log({uname,dateofbirth,email,number,education,job,experience,rurl});

    // Created a FormData object
var formData = new FormData();

// Appended our form fields to the FormData object
formData.append('ename', uname);
formData.append('date_of_birth', dateofbirth);
formData.append('email', email);
formData.append('mobnumber', number);
formData.append('education', education);
formData.append('job', job);
formData.append('experience', experience);
formData.append('resumeurl', rurl);

// Make the fetch request
fetch("http://127.0.0.1:5000/register", {
  method: "POST",
  body: formData
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
window.location.href = "details.html";
}

function getCustomerData() {
  const appNo = document.getElementById('appNo').value;

  fetch(`http://localhost:5000/getCustomers/${appNo}`)
  .then(response => {
      if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
  })
  .then(data => {
      const details = document.getElementById('customerData');
      details.innerHTML = formatData(data);
  })
  .catch(error => console.error('Error:', error));
}
