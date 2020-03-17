// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    "lengthMenu": [[-1, 10, 15, 25], ["Todos", 10, 15, 25]]
  });
});
