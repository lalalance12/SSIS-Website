function confirmDeleteCollege(button) {
  var collegeCode = button.getAttribute('college-code');
  var csrfToken = button.getAttribute('csrf-token');
  if (confirm("Are you sure you want to delete College " + collegeCode + " permanently?\nCourses and Students under this College will also be deleted.")) {
      fetch(`/college/delete_college/${collegeCode}`, {
          method: 'DELETE',
          headers: {
              'X-CSRFToken': csrfToken
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.success === true) {
              window.location.reload();
          } else {
              console.error("Error: " + data.message);
          }
      });
  }
}


  function confirmDeleteCourse(button) {
    var course_code = button.getAttribute('course-code');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete Course " + course_code + " permanently?\nStudents under this course will also be deleted.")) {
        fetch(`/course/delete_course/${course_code}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.message);
            }
        });
    }
}


  function confirmDeleteStudent(button) {
      var student_id = button.getAttribute('student-id');
      var csrfToken = button.getAttribute('csrf-token');
      if (confirm("Are you sure you want to delete Student " + student_id + " permanently ?\n")) {
          fetch(`/student/delete_student/${student_id}`, {  // Updated URL
              method: 'DELETE',
              headers: {
                  'X-CSRFToken': csrfToken
              }
          }).then(response => response.json())
          .then(data => {
            if(data.success == true) {
              window.location.reload();
            } else {
              console.error("Error: " + data.message);
            }
          });
      }
  }
          
