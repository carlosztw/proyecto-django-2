(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

/* BOTON ELIMINAR */

function confirmarEliminar(id){ 
  swal.fire({
      title: '¿Estás seguro?',
      text: "Esta orden de servicio será eliminada de la base de datos",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#4CAF50',
      cancelButtonColor: '#f44336' ,
      confirmButtonText: 'Sí',
      cancelButtonText: 'No',
      reverseButtons: true,
      allowOutsideClick: false
  }).then((result) => {
      if (result.isConfirmed) {
      swal.fire({
          title: '¡Eliminado!',
          text: 'La orden de servicio ha sido eliminada de la base de datos',
          icon: 'success',
          allowOutsideClick: false,
          confirmButtonColor: '#4CAF50'
        }).then(function() {
            window.location.href = "/eliminarservicio/"+id+"/";
        })

      } else if (
      /* Read more about handling dismissals below */
      result.dismiss === Swal.DismissReason.cancel
      ) {
      swal.fire({
          title: 'Cancelado',
          text: 'La orden de servicio no ha sido eliminado',
          icon: 'error',
          confirmButtonColor: '#4CAF50'
      })
      }
  })
}